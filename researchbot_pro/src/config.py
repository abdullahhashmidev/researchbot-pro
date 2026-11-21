"""
Configuration Manager
---------------------
Sab environment variables ek jagah manage hoti hain.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# Project root (src/ ka parent). Relative paths ki jagah is se absolute paths banate hain,
# taake app kisi bhi working directory se chale to outputs same jagah save hon.
BASE_DIR = Path(__file__).resolve().parent.parent


class Config:
    """Application-wide configuration"""

    # ── LLM ─────────────────────────────────────────
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")
    MODEL_NAME: str = os.getenv("MODEL_NAME", "groq/llama-3.3-70b-versatile")

    # ── Output ──────────────────────────────────────
    OUTPUT_DIR: str = str(Path(os.getenv("OUTPUT_DIR", BASE_DIR / "outputs")).resolve())

    @classmethod
    def validate(cls) -> None:
        """App start hone se pehle config validate karo."""
        if not cls.GROQ_API_KEY:
            raise ValueError(
                "\n❌  GROQ_API_KEY is missing!\n"
                "    Steps to fix:\n"
                "    1. Go to https://console.groq.com  (free)\n"
                "    2. Create an API key\n"
                "    3. Add it to your .env file:\n"
                "       GROQ_API_KEY=your_key_here\n"
            )
        os.makedirs(cls.OUTPUT_DIR, exist_ok=True)


config = Config()
