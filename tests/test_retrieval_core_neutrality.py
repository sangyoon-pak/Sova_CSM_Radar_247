from pathlib import Path


def _read(path: str) -> str:
    return Path(path).read_text(encoding="utf-8").lower()


def test_doc_search_has_no_vendor_specific_strings():
    text = _read("src/agent/tools/doc_search.py")
    forbidden = [
        "appier",
        "aiqua",
        "airis",
        "botbonnie",
        "aixon",
        "aideal",
        "ai_agent",
    ]
    for token in forbidden:
        assert token not in text, f"Found vendor-specific token in doc_search.py: {token}"


def test_search_agent_has_no_vendor_specific_strings():
    text = _read("src/agent/tools/search_agent.py")
    forbidden = [
        "appier",
        "aiqua",
        "airis",
        "botbonnie",
        "aixon",
        "aideal",
        "ai_agent",
    ]
    for token in forbidden:
        assert token not in text, f"Found vendor-specific token in search_agent.py: {token}"

