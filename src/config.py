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
    rag_embedding_provider: str = Field("openrouter", validation_alias="RAG_EMBEDDING_PROVIDER")
    rag_embedding_model: str = Field(
        "openai/text-embedding-3-large",
        validation_alias="RAG_EMBEDDING_MODEL",
    )

    # Knowledge base
    knowledge_base_path: str = Field(
        "knowledge-base",
        validation_alias="KNOWLEDGE_BASE_PATH",
    )

    # RC / scope-aware ranking (optional)
    # When enabled and RC_SCOPE_LABELS is set, the retrieval pipeline can
    # down-rank snippets whose primary documentation category differs from
    # the user's inferred scope.
    rc_scope_enable: bool = Field(True, validation_alias="RC_SCOPE_ENABLE")
    rc_scope_field: str = Field("product", validation_alias="RC_SCOPE_FIELD")
    # Comma-separated list. Example (for current Appier KB):
    #   RC_SCOPE_LABELS=aiqua,airis,botbonnie,enterprise,aixon,aideal,ai_agent
    rc_scope_labels: str = Field("", validation_alias="RC_SCOPE_LABELS")
    rc_scope_penalty: int = Field(100, validation_alias="RC_SCOPE_PENALTY")
    # Optional: regex used to infer a doc scope label from filename.
    # Should include a capture group for the label, e.g.:
    #   ^\d+_(?P<scope>[a-z0-9]+)_.*\.md$
    rc_scope_filename_regex: str = Field("", validation_alias="RC_SCOPE_FILENAME_REGEX")

    # Gmail (gog) — uses gog CLI + keyring stored under GOG_HOME (when set)
    gog_home: str = Field("", validation_alias="GOG_HOME")
    gog_account: str = Field("", validation_alias="GOG_ACCOUNT")
    gog_keyring_backend: str = Field("file", validation_alias="GOG_KEYRING_BACKEND")
    gog_keyring_password: str = Field("", validation_alias="GOG_KEYRING_PASSWORD")
    xdg_config_home: str = Field("", validation_alias="XDG_CONFIG_HOME")

    # Server
    host: str = Field("127.0.0.1", validation_alias="HOST")
    port: int = Field(8000, validation_alias="PORT")

    # Scheduler
    scheduler_timezone: str = Field("Asia/Seoul", validation_alias="SCHEDULER_TIMEZONE")

    # Database
    database_path: str = Field("./data/agent.db", validation_alias="DATABASE_PATH")

    # LangSmith (read from .env via pydantic; worker may not inherit os.environ)
    langsmith_api_key: str | None = Field(None, validation_alias="LANGSMITH_API_KEY")
    langsmith_project: str = Field("email_draft_agent", validation_alias="LANGSMITH_PROJECT")

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
        """Resolve GOG_HOME to absolute path (e.g. email_draft_agent/scripts/.local)."""
        if not self.gog_home:
            return None
        p = Path(self.gog_home)
        if not p.is_absolute():
            root = Path(__file__).parent.parent
            p = (root / p).resolve()
        return p if p.exists() else None

settings = Settings()
