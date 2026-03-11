#!/usr/bin/env python3
"""Run the Email Draft Agent server."""
from dotenv import load_dotenv

load_dotenv()  # Load .env into os.environ so LangSmith and other libs see LANGSMITH_*, etc.

import uvicorn

from src.config import settings

if __name__ == "__main__":
    uvicorn.run(
        "src.main:app",
        host=settings.host,
        port=settings.port,
        reload=True,
    )
