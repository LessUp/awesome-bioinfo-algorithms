"""
Translation helper for Awesome Bioinformatics Algorithms.
Provides utilities for translating algorithm descriptions to English.
"""

from pathlib import Path
from typing import Any, Optional

import yaml

from .algorithm_registry import AlgorithmRegistry


def translate_text(text: str, source_lang: str = "zh", target_lang: str = "en") -> str:
    """
    Translate text from source language to target language.

    This is a placeholder that returns the original text with a prefix.
    For actual translation, integrate with a translation API.

    Args:
        text: Text to translate
        source_lang: Source language code
        target_lang: Target language code

    Returns:
        Translated text (or placeholder if no API configured)
    """
    # Placeholder: return original text marked for translation
    # In production, this would call a translation API
    return text


def get_missing_translations(base_dir: Path) -> list[dict[str, Any]]:
    """
    Find algorithms missing English translations.

    Args:
        base_dir: Project root directory

    Returns:
        List of dicts with algo_id, file_path, missing_fields
    """
    algorithms_dir = base_dir / "data" / "algorithms"
    missing = []

    for yaml_file in algorithms_dir.glob("*.yaml"):
        with open(yaml_file, encoding="utf-8") as f:
            data = yaml.safe_load(f)

        if not data or "algorithms" not in data:
            continue

        for algo in data["algorithms"]:
            algo_id = algo.get("id", "unknown")
            missing_fields = []

            if not algo.get("description_en"):
                missing_fields.append("description_en")
            if not algo.get("purpose_en"):
                missing_fields.append("purpose_en")

            if missing_fields:
                missing.append(
                    {
                        "id": algo_id,
                        "file": str(yaml_file),
                        "missing": missing_fields,
                        "description": algo.get("description", ""),
                        "purpose": algo.get("purpose", ""),
                    }
                )

    return missing


def generate_translation_template(base_dir: Path, output_path: Optional[Path] = None) -> Path:
    """
    Generate a YAML template file with all missing translations.

    Args:
        base_dir: Project root directory
        output_path: Optional output path, defaults to translations.yaml

    Returns:
        Path to generated template file
    """
    missing = get_missing_translations(base_dir)
    output_path = output_path or (base_dir / "translations_template.yaml")

    template_data: dict[str, Any] = {
        "_comment": "Translation template - fill in the English translations",
        "algorithms": [],
    }

    for item in missing:
        entry = {
            "id": item["id"],
            "description_en": "",  # To be filled
            "purpose_en": "",  # To be filled
            "_original_description": item["description"],
            "_original_purpose": item["purpose"],
        }
        template_data["algorithms"].append(entry)

    with open(output_path, "w", encoding="utf-8") as f:
        yaml.dump(template_data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)

    return output_path


def apply_translations(base_dir: Path, translations_path: Path) -> tuple[int, int]:
    """
    Apply translations from a YAML file to algorithm data files.

    Args:
        base_dir: Project root directory
        translations_path: Path to translations YAML file

    Returns:
        Tuple of (success_count, error_count)
    """
    with open(translations_path, encoding="utf-8") as f:
        translations = yaml.safe_load(f)

    if not translations or "algorithms" not in translations:
        return 0, 0

    # Build lookup by algorithm ID
    trans_map = {t["id"]: t for t in translations["algorithms"]}

    algorithms_dir = base_dir / "data" / "algorithms"
    success = 0
    errors = 0

    for yaml_file in algorithms_dir.glob("*.yaml"):
        with open(yaml_file, encoding="utf-8") as f:
            data = yaml.safe_load(f)

        if not data or "algorithms" not in data:
            continue

        modified = False
        for algo in data["algorithms"]:
            algo_id = algo.get("id")
            if algo_id in trans_map:
                trans = trans_map[algo_id]

                if trans.get("description_en") and not algo.get("description_en"):
                    algo["description_en"] = trans["description_en"]
                    modified = True

                if trans.get("purpose_en") and not algo.get("purpose_en"):
                    algo["purpose_en"] = trans["purpose_en"]
                    modified = True

                success += 1

        if modified:
            with open(yaml_file, "w", encoding="utf-8") as f:
                yaml.dump(data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)

    return success, errors


def cmd_translate_status() -> int:
    """Command: Show translation status."""
    base_dir = Path(__file__).resolve().parent.parent
    missing = get_missing_translations(base_dir)

    registry = AlgorithmRegistry()
    registry.load_all()
    total = len(registry._algorithms)

    print("🌐 Translation Status")
    print("=" * 50)
    print(f"Total algorithms: {total}")
    print(f"Missing English translations: {len(missing)}")
    print(f"Complete: {total - len(missing)} ({(total - len(missing)) / total * 100:.1f}%)")
    print()

    if missing:
        print("Missing translations by file:")
        by_file: dict[str, int] = {}
        for item in missing:
            file_name = str(Path(item["file"]).name)
            by_file[file_name] = by_file.get(file_name, 0) + 1

        for file, count in sorted(by_file.items(), key=lambda x: -x[1]):
            print(f"  {file}: {count}")

    return 0


def cmd_translate_generate() -> int:
    """Command: Generate translation template."""
    base_dir = Path(__file__).resolve().parent.parent
    output_path = generate_translation_template(base_dir)

    missing = get_missing_translations(base_dir)
    print(f"📝 Generated translation template: {output_path}")
    print(f"   Contains {len(missing)} algorithms needing translation")
    print()
    print("Next steps:")
    print("1. Edit the template file and fill in English translations")
    print("2. Run: python -m awesome_bioinfo translate apply")

    return 0


def cmd_translate_apply(translations_file: Optional[str] = None) -> int:
    """Command: Apply translations from file."""
    base_dir = Path(__file__).resolve().parent.parent

    if translations_file:
        trans_path = Path(translations_file)
    else:
        trans_path = base_dir / "translations_template.yaml"

    if not trans_path.exists():
        print(f"Error: Translation file not found: {trans_path}")
        print("Run: python -m awesome_bioinfo translate generate")
        return 1

    success, errors = apply_translations(base_dir, trans_path)

    print(f"✅ Applied translations: {success} algorithms updated")
    if errors:
        print(f"❌ Errors: {errors}")

    return 0
