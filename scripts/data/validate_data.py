"""
Reference Data Validator
CRM Customer Database Portfolio

Version : 2.0

Module 1
---------
Core Configuration
"""

from pathlib import Path
import importlib
import sys


# =============================================================================
# Project Path Fix
# =============================================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


# =============================================================================
# Configuration
# =============================================================================

DATA_FOLDER = PROJECT_ROOT / "data"

LINE = "=" * 60


DATASETS = {

    "Companies": (
        "companies",
        "COMPANIES"
    ),

    "Industries": (
        "industries",
        "INDUSTRIES"
    ),

    "Locations": (
        "locations",
        "LOCATIONS"
    ),

    "Job Titles": (
        "job_titles",
        "JOB_TITLES"
    ),

    "First Names": (
        "first_names",
        "FIRST_NAMES"
    ),

    "Last Names": (
        "last_names",
        "LAST_NAMES"
    ),

}


# =============================================================================
# Console
# =============================================================================

def banner():

    print(LINE)
    print("CRM CUSTOMER DATABASE PORTFOLIO")
    print("Reference Data Validator v2.0")
    print(LINE)
    print()


# =============================================================================
# Helper Functions
# =============================================================================

def load_dataset(module_name, variable_name):
    """
    Dynamically import a dataset module and return its variable.
    """

    module = importlib.import_module(f"data.{module_name}")

    return getattr(module, variable_name)


def count_blank_strings(dataset):

    blank_count = 0

    for item in dataset:

        if isinstance(item, str):

            if not item.strip():

                blank_count += 1

    return blank_count


def count_blank_dictionary_fields(dataset):

    blank_count = 0

    for record in dataset:

        if not isinstance(record, dict):

            continue

        for value in record.values():

            if isinstance(value, str):

                if not value.strip():

                    blank_count += 1

    return blank_count


def count_duplicates(dataset):

    seen = set()

    duplicates = 0

    for item in dataset:

        if isinstance(item, dict):

            key = tuple(sorted(item.items()))

        else:

            key = item

        if key in seen:

            duplicates += 1

        else:

            seen.add(key)

    return duplicates


# =============================================================================
# Main
# =============================================================================

def main():

    banner()

    print("Checking reference datasets...")
    print()

    for dataset_name, (module_name, variable_name) in DATASETS.items():

        try:

            dataset = load_dataset(
                module_name,
                variable_name
            )

            print(
                f"PASS : {dataset_name:<15}"
                f"{len(dataset):>5} records"
            )

        except Exception as error:

            print(
                f"FAIL : {dataset_name:<15}"
                f"{error}"
            )

    print()
    print(LINE)
    print("Module 1 completed successfully.")
    print("Ready for Module 2 - Dataset Validation")
    print(LINE)

    return 0


if __name__ == "__main__":

    sys.exit(main())