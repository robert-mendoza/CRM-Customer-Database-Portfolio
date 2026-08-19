"""
Merge Utility
CRM Customer Database Portfolio

Merge Industry Reference Datasets

Version : 1.0
"""

from pathlib import Path
import importlib
import sys

# =============================================================================
# Configuration
# =============================================================================

PROJECT_ROOT = Path(__file__).resolve().parent

DATA_FOLDER = PROJECT_ROOT / "data"

OUTPUT_FILE = DATA_FOLDER / "industries.py"

PART_FILES = [
    "industries_part1A",
    "industries_part1B",
]

LINE = "=" * 60


# =============================================================================
# Console
# =============================================================================

def banner():

    print(LINE)
    print("CRM CUSTOMER DATABASE PORTFOLIO")
    print("Industry Merge Utility v1.0")
    print(LINE)
    print()


# =============================================================================
# Validation
# =============================================================================

def load_industries():

    industries = []

    for module_name in PART_FILES:

        module = importlib.import_module(f"data.{module_name}")

        industries.extend(module.INDUSTRIES)

    return industries


def validate_duplicates(records):

    duplicates = []

    seen = set()

    for item in records:

        value = item.strip().lower()

        if value in seen:

            duplicates.append(item)

        else:

            seen.add(value)

    return duplicates


# =============================================================================
# Output
# =============================================================================

def write_output(records):

    records = sorted(records)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:

        file.write('"""\n')
        file.write("Industry Reference Data\n")
        file.write("CRM Customer Database Portfolio\n\n")
        file.write("AUTO-GENERATED FILE\n")
        file.write("DO NOT EDIT MANUALLY\n")
        file.write('"""\n\n')

        file.write("INDUSTRIES = [\n\n")

        for item in records:

            file.write(f'    "{item}",\n')

        file.write("\n]\n")


# =============================================================================
# Main
# =============================================================================

def main():

    banner()

    records = load_industries()

    duplicates = validate_duplicates(records)

    print(f"Part Files       : {len(PART_FILES)}")
    print(f"Total Records    : {len(records)}")
    print()

    if duplicates:

        print("Duplicate Industries Found")
        print()

        for item in duplicates:

            print(f" - {item}")

        return 1

    write_output(records)

    print("Duplicates       : 0")
    print("Status           : SUCCESS")
    print(f"Output           : {OUTPUT_FILE.name}")

    return 0


if __name__ == "__main__":
    sys.exit(main())