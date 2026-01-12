#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEVEL_DIRS = [
    ROOT / "01_Beginner",
    ROOT / "02_Advanced",
    ROOT / "03_Expert",
]


def read_text(path: Path, *, strip: bool = True) -> str:
    text = path.read_text(encoding="utf-8")
    return text.strip() if strip else text


def load_levels_inline() -> list[dict[str, object]]:
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
                            "code": read_text(step_file, strip=False),
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


def format_step_markdown(step_file: Path) -> str:
    language = step_file.suffix.lstrip(".") or "text"
    code = read_text(step_file, strip=False)
    return f"```{language}\n{code}\n```"


def load_levels_hugo(content_root: Path) -> list[dict[str, object]]:
    levels: list[dict[str, object]] = []
    if content_root.exists():
        shutil.rmtree(content_root)
    for level_dir in LEVEL_DIRS:
        projects: list[dict[str, object]] = []
        for project_dir in sorted([p for p in level_dir.iterdir() if p.is_dir()]):
            todo_path = project_dir / "TODO.md"
            tipps_path = project_dir / "TIPPS.md"
            steps_dir = project_dir / "steps"
            project_root = content_root / level_dir.name / project_dir.name
            project_root.mkdir(parents=True, exist_ok=True)

            todo_output = project_root / "todo.md"
            tipps_output = project_root / "tipps.md"
            if todo_path.exists():
                todo_output.write_text(read_text(todo_path), encoding="utf-8")
            if tipps_path.exists():
                tipps_output.write_text(read_text(tipps_path), encoding="utf-8")

            steps: list[dict[str, str]] = []
            if steps_dir.exists():
                for step_file in sorted([p for p in steps_dir.iterdir() if p.is_file()]):
                    step_output = project_root / "steps" / f"{step_file.stem}.md"
                    step_output.parent.mkdir(parents=True, exist_ok=True)
                    step_output.write_text(format_step_markdown(step_file), encoding="utf-8")
                    steps.append(
                        {
                            "id": step_file.stem,
                            "filename": step_file.name,
                            "path": step_output,
                        }
                    )
            projects.append(
                {
                    "id": project_dir.name,
                    "title": project_dir.name.replace("_", " "),
                    "todo_path": todo_output if todo_path.exists() else "",
                    "tipps_path": tipps_output if tipps_path.exists() else "",
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


def build_inline_payload() -> dict[str, object]:
    return {"levels": load_levels_inline()}


def build_hugo_payload() -> dict[str, object]:
    hugo_root = ROOT / "site-hugo"
    content_root = hugo_root / "content_sources"
    levels = load_levels_hugo(content_root)
    for level in levels:
        for project in level["projects"]:
            if project.get("todo_path"):
                project["todo_path"] = (
                    Path(project["todo_path"]).relative_to(hugo_root).as_posix()
                )
            if project.get("tipps_path"):
                project["tipps_path"] = (
                    Path(project["tipps_path"]).relative_to(hugo_root).as_posix()
                )
            for step in project["steps"]:
                step["path"] = Path(step["path"]).relative_to(hugo_root).as_posix()
    return {"levels": levels}


def write_astro() -> None:
    payload = build_inline_payload()
    write_payload(ROOT / "site-astro" / "src" / "data" / "content.json", payload)


def write_nextjs() -> None:
    payload = build_inline_payload()
    write_payload(ROOT / "site-nextjs" / "data" / "content.json", payload)


def write_hugo() -> None:
    payload = build_hugo_payload()
    write_payload(ROOT / "site-hugo" / "data" / "content.json", payload)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate site content data for each site builder."
    )
    parser.add_argument(
        "--site",
        choices=["astro", "nextjs", "hugo", "all"],
        default="all",
        help="Site builder to update",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.site == "astro":
        write_astro()
        return
    if args.site == "nextjs":
        write_nextjs()
        return
    if args.site == "hugo":
        write_hugo()
        return
    write_astro()
    write_nextjs()
    write_hugo()


if __name__ == "__main__":
    main()
