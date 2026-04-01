#!/usr/bin/env python3
"""Run the Email Draft Agent server."""
from pathlib import Path

from dotenv import load_dotenv

# Load project-root .env into os.environ so workers always see OPENROUTER_*, LANGSMITH_*, etc.
_ROOT = Path(__file__).resolve().parent
load_dotenv(_ROOT / ".env")

import uvicorn

from src.config import settings

if __name__ == "__main__":
    uvicorn.run(
        "src.main:app",
        host=settings.host,
        port=settings.port,
        reload=False,
    )
