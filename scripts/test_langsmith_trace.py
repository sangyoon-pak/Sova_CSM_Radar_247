#!/usr/bin/env python3
"""Run a single agent invocation to verify LangSmith tracing. Check smith.langchain.com after."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import os

print("LangSmith config:")
print("  LANGSMITH_TRACING:", os.environ.get("LANGSMITH_TRACING"))
print("  LANGSMITH_API_KEY:", "set" if os.environ.get("LANGSMITH_API_KEY") else "NOT SET")
print("  LANGSMITH_PROJECT:", os.environ.get("LANGSMITH_PROJECT", "default"))
print()

from src.agent.email_agent import run_agent

print("Invoking agent (this should create a trace)...")
out = run_agent("Hello, what can you do?")
print("Output:", out[:200] + "..." if len(out) > 200 else out)
print()
print("Done. Check https://smith.langchain.com → Projects → email_draft_agent (or 'default')")
