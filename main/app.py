"""Application entry point for the password generator."""

from __future__ import annotations

# Link do streamlit: https://passwordgeneratorufg.streamlit.app/

import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent

for entry in (str(SCRIPT_DIR), str(PROJECT_ROOT)):
    if entry in sys.path:
        sys.path.remove(entry)

sys.path.insert(0, str(PROJECT_ROOT))

from app.models.interface import build_interface


build_interface()
