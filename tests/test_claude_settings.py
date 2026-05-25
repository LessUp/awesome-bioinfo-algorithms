"""Regression tests for Claude hook wiring."""

from __future__ import annotations

import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def _iter_hook_commands() -> list[str]:
    settings = json.loads((PROJECT_ROOT / ".claude" / "settings.json").read_text(encoding="utf-8"))
    commands: list[str] = []

    for entries in settings.get("hooks", {}).values():
        for entry in entries:
            for hook in entry.get("hooks", []):
                command = hook.get("command")
                if isinstance(command, str) and command.startswith("python3 "):
                    commands.append(command.removeprefix("python3 ").strip())

    return commands


def test_claude_hook_commands_point_to_existing_scripts() -> None:
    missing = [command for command in _iter_hook_commands() if not (PROJECT_ROOT / command).is_file()]

    assert missing == []


def test_claude_settings_do_not_register_trellis_hooks_without_trellis_runtime() -> None:
    assert not (PROJECT_ROOT / ".trellis").exists()
    assert _iter_hook_commands() == []
