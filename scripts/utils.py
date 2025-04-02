import json
from pathlib import Path


class ModManager:
    mod_filename: str = "mods.json"
    root = Path.cwd()

    @classmethod
    def mods_path(cls) -> Path:
        return cls.root / "db" / cls.mod_filename

    @classmethod
    def load(cls) -> dict:
        with open(cls.mods_path(), "r", encoding="utf-8") as f:
            return json.load(f)

    @classmethod
    def export(cls, mods: dict) -> None:
        assert mods, "Mods not loaded"

        with open(cls.mods_path(), "w", encoding="utf-8") as f:
            json.dump(mods, f, indent=4, ensure_ascii=False)
