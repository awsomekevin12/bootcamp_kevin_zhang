import os
from pathlib import Path
from dotenv import load_dotenv
from typing import Optional

# Load the .env file
load_dotenv()

def get_key(name: str, default: Optional[str] = None) -> Optional[str]:
    """Safely gets a key from the environment variables."""
    return os.getenv(name, default)

# Define project paths
PROJECT_ROOT = Path.cwd()
DATA_DIR = PROJECT_ROOT / "data"