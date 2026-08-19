"""
Merge Utility
CRM Customer Database Portfolio

Merge Location Reference Datasets

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

OUTPUT_FILE = DATA_FOLDER / "company.py"

PART_FILES = [
    "companies_part1A",
    "companies_part1B",
    "companies_part2A",
    "companies_part2B",
]

LINE = "=" * 60


# =============================================================================
# Console
# =============================================================================

def banner():

    print(LINE)
    print("CRM CUSTOMER DATABASE PORTFOLIO")
    print("Company Merge Utility v1.0")
    print(LINE)
    print()


# =============================================================================
# Dataset Loader
# =============================================================================

def load_locations():

    records = []

    for module_name in PART_FILES:

        module = importlib.import_module(f"data.{module_name}")

        records.extend(module.LOCATIONS)

    return records


# =============================================================================
# Validation
# =============================================================================

def validate_duplicates(records):

    duplicates = []

    seen = set()

    for record in records:

        key = (
            record["city"].strip().lower(),
            record["state"].strip().lower(),
            record["country"].strip().lower()
        )

        if key in seen:
            duplicates.append(record)
        else:
            seen.add(key)

    return duplicates


# =============================================================================
# Output Generator
# =============================================================================

def write_output(records):

    records = sorted(
        records,
        key=lambda item: (
            item["country"],
            item["state"],
            item["city"]
        )
    )

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:

        file.write('"""\n')
        file.write("Location Reference Data\n")
        file.write("CRM Customer Database Portfolio\n\n")
        file.write("AUTO-GENERATED FILE\n")
        file.write("DO NOT EDIT MANUALLY\n")
        file.write('"""\n\n')

        file.write("LOCATIONS = [\n\n")

        for record in records:

            file.write("    {\n")
            file.write(f'        "city": "{record["city"]}",\n')
            file.write(f'        "state": "{record["state"]}",\n')
            file.write(f'        "country": "{record["country"]}"\n')
            file.write("    },\n\n")

        file.write("]\n")


# =============================================================================
# Main
# =============================================================================

def main():

    banner()

    records = load_locations()

    duplicates = validate_duplicates(records)

    print(f"Part Files       : {len(PART_FILES)}")
    print(f"Total Records    : {len(records)}")
    print()

    if duplicates:

        print("Duplicate Locations Found")
        print()

        for record in duplicates:

            print(
                f'- {record["city"]}, '
                f'{record["state"]}, '
                f'{record["country"]}'
            )

        return 1

    write_output(records)

    print("Duplicates       : 0")
    print("Status           : SUCCESS")
    print(f"Output           : {OUTPUT_FILE.name}")

    return 0


if __name__ == "__main__":
    sys.exit(main())