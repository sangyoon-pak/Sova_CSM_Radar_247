"""Configuration from environment."""
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """App settings from env."""

    # LLM
    openai_api_key: str | None = Field(None, validation_alias="OPENAI_API_KEY")
    openrouter_api_key: str | None = Field(None, validation_alias="OPENROUTER_API_KEY")
    openrouter_base_url: str = Field(
        "https://openrouter.ai/api/v1", validation_alias="OPENROUTER_BASE_URL"
    )
    llm_model: str = Field("gpt-4o", validation_alias="LLM_MODEL")

    # Knowledge base
    knowledge_base_path: str = Field(
        "knowledge-base",
        validation_alias="KNOWLEDGE_BASE_PATH",
    )

    # Gmail (gog) — use openclaw_project credentials when GOG_HOME points there
    gog_home: str = Field("", validation_alias="GOG_HOME")
    gog_account: str = Field("", validation_alias="GOG_ACCOUNT")
    gog_keyring_backend: str = Field("file", validation_alias="GOG_KEYRING_BACKEND")
    gog_keyring_password: str = Field("", validation_alias="GOG_KEYRING_PASSWORD")
    xdg_config_home: str = Field("", validation_alias="XDG_CONFIG_HOME")

    # Server
    host: str = Field("127.0.0.1", validation_alias="HOST")
    port: int = Field(8000, validation_alias="PORT")

    # Allowlisted client domains
    client_domains: str = Field(
        "@client1.com,@client2.com", validation_alias="CLIENT_DOMAINS"
    )

    # Scheduler
    scheduler_timezone: str = Field("Asia/Seoul", validation_alias="SCHEDULER_TIMEZONE")

    # Database
    database_path: str = Field("./data/agent.db", validation_alias="DATABASE_PATH")

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "extra": "ignore",
    }

    @property
    def kb_path_resolved(self) -> Path:
        p = Path(self.knowledge_base_path)
        if not p.is_absolute():
            root = Path(__file__).parent.parent
            p = (root / p).resolve()
        return p

    @property
    def gog_home_resolved(self) -> Path | None:
        """Resolve GOG_HOME to absolute path. Points to openclaw_project/scripts/.local for shared credentials."""
        if not self.gog_home:
            return None
        p = Path(self.gog_home)
        if not p.is_absolute():
            root = Path(__file__).parent.parent
            p = (root / p).resolve()
        return p if p.exists() else None

    @property
    def allowlist(self) -> list[str]:
        return [d.strip() for d in self.client_domains.split(",") if d.strip()]


settings = Settings()
