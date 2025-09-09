import os
from pathlib import Path


SAVE_FILE: Path = Path.home() / "coolpassword.cpsave"
KEY_FILE: Path = Path.home() / "coolpassword.cpkey"

MAIN_DIR: Path = Path.home() / ".coolpassword"

LOGER_FILE: Path = MAIN_DIR / "loger"
MASTER_KEY_FILE: Path = MAIN_DIR / "master_key"
SITES_FILE: Path = MAIN_DIR / "sites"
SEED_FILE: Path = MAIN_DIR / "seed"


def init_dir():
    if not MAIN_DIR.exists():
        os.mkdir(MAIN_DIR)
