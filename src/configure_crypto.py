"""Encrypt / decrypt Configure fields at rest (Fernet).

Set ``CONFIGURE_ENCRYPTION_KEY`` to a Fernet key (``python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"``).
When unset, values are stored **plaintext** in the database (same as before encryption existed).
"""
from __future__ import annotations

from cryptography.fernet import Fernet, InvalidToken

from src.config import settings

_ENC_PREFIX = "enc:v1:"


def _fernet() -> Fernet | None:
    key = (getattr(settings, "configure_encryption_key", None) or "").strip()
    if not key:
        return None
    try:
        return Fernet(key.encode("ascii"))
    except Exception:
        return None


def encryption_enabled() -> bool:
    return _fernet() is not None


def encrypt_configure_value(plain: str) -> str:
    if not plain:
        return ""
    f = _fernet()
    if f is None:
        return plain
    token = f.encrypt(plain.encode("utf-8"))
    return _ENC_PREFIX + token.decode("ascii")


def decrypt_configure_value(stored: str) -> str:
    if not stored:
        return ""
    if not stored.startswith(_ENC_PREFIX):
        return stored
    f = _fernet()
    if f is None:
        return stored
    try:
        raw = stored[len(_ENC_PREFIX) :].encode("ascii")
        return f.decrypt(raw).decode("utf-8")
    except (InvalidToken, ValueError, UnicodeDecodeError):
        return stored
