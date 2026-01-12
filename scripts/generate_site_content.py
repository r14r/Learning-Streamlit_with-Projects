#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEVEL_DIRS = [
    ROOT / "01_Beginner",
    ROOT / "02_Advanced",
    ROOT / "03_Expert",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


def load_levels() -> list[dict[str, object]]:
    levels: list[dict[str, object]] = []
    for level_dir in LEVEL_DIRS:
        projects: list[dict[str, object]] = []
        for project_dir in sorted([p for p in level_dir.iterdir() if p.is_dir()]):
            todo_path = project_dir / "TODO.md"
            tipps_path = project_dir / "TIPPS.md"
            steps_dir = project_dir / "steps"
            steps: list[dict[str, str]] = []
            if steps_dir.exists():
                for step_file in sorted([p for p in steps_dir.iterdir() if p.is_file()]):
                    steps.append(
                        {
                            "id": step_file.stem,
                            "filename": step_file.name,
                            "code": read_text(step_file),
                        }
                    )
            projects.append(
                {
                    "id": project_dir.name,
                    "title": project_dir.name.replace("_", " "),
                    "todo": read_text(todo_path) if todo_path.exists() else "",
                    "tipps": read_text(tipps_path) if tipps_path.exists() else "",
                    "steps": steps,
                }
            )
        levels.append(
            {
                "id": level_dir.name,
                "title": level_dir.name.replace("_", " "),
                "projects": projects,
            }
        )
    return levels


def write_payload(target: Path, payload: dict[str, object]) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def main() -> None:
    payload = {"levels": load_levels()}
    write_payload(ROOT / "site-nextjs" / "data" / "content.json", payload)
    write_payload(ROOT / "site-astro" / "src" / "data" / "content.json", payload)
    write_payload(ROOT / "site-hugo" / "data" / "content.json", payload)


if __name__ == "__main__":
    main()
