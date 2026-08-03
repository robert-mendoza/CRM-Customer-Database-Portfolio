"""
CRM Customer Database Portfolio

Reference Data Validator
Version: 1.1
"""

from collections import Counter
from importlib import import_module


# ==========================================================
# DATASETS
# ==========================================================

DATASETS = {
    "Companies": (
        "data.companies",
        "COMPANIES",
    ),
    "Industries": (
        "data.industries",
        "INDUSTRIES",
    ),
    "Locations": (
        "data.locations",
        "LOCATIONS",
    ),
    "Job Titles": (
        "data.job_titles",
        "JOB_TITLES",
    ),
    "First Names": (
        "data.first_names",
        "FIRST_NAMES",
    ),
    "Last Names": (
        "data.last_names",
        "LAST_NAMES",
    ),
}


# ==========================================================
# DISPLAY HELPERS
# ==========================================================

def divider():
    print("-" * 60)


def heading():
    print()
    print("=" * 60)
    print("CRM CUSTOMER DATABASE PORTFOLIO")
    print("Reference Data Validator v1.1")
    print("=" * 60)
    print()


# ==========================================================
# IMPORT
# ==========================================================

def load_dataset(module_name, variable_name):
    module = import_module(module_name)
    return getattr(module, variable_name)


# ==========================================================
# VALIDATION
# ==========================================================

def validate_dataset(dataset):

    result = {
        "records": 0,
        "duplicates": [],
        "blank": [],
        "status": "PASS",
    }

    if not isinstance(dataset, list):
        result["status"] = "FAIL"
        return result

    result["records"] = len(dataset)

    if len(dataset) == 0:
        result["status"] = "FAIL"
        return result

    values = []

    for item in dataset:

        if isinstance(item, str):

            value = item.strip()

            if value == "":
                result["blank"].append(item)

            values.append(value)

        elif isinstance(item, dict):

            values.append(str(item))

        elif isinstance(item, tuple):

            values.append(str(item))

        else:

            values.append(str(item))

    counter = Counter(values)

    result["duplicates"] = sorted(
        value
        for value, count in counter.items()
        if count > 1
    )

    if result["duplicates"]:
        result["status"] = "FAIL"

    if result["blank"]:
        result["status"] = "FAIL"

    return result


# ==========================================================
# PRINT RESULT
# ==========================================================

def print_result(name, result):

    divider()

    print(name)

    print(f"Records      : {result['records']}")
    print(f"Duplicates   : {len(result['duplicates'])}")
    print(f"Blank Values : {len(result['blank'])}")
    print(f"Status       : {result['status']}")

    if result["duplicates"]:

        print()
        print("Duplicate Entries:")

        for item in result["duplicates"]:
            print(f"  - {item}")

    if result["blank"]:

        print()
        print("Blank Entries:")

        for item in result["blank"]:
            print(f"  - {repr(item)}")


# ==========================================================
# MAIN
# ==========================================================

def main():

    heading()

    total_records = 0
    total_duplicates = 0
    total_blank = 0

    overall_status = "PASS"

    for dataset_name, (module_name, variable_name) in DATASETS.items():

        try:

            dataset = load_dataset(
                module_name,
                variable_name,
            )

        except Exception as error:

            divider()

            print(dataset_name)

            print("Status : FAIL")
            print(error)

            overall_status = "FAIL"

            continue

        result = validate_dataset(dataset)

        total_records += result["records"]
        total_duplicates += len(result["duplicates"])
        total_blank += len(result["blank"])

        if result["status"] == "FAIL":
            overall_status = "FAIL"

        print_result(dataset_name, result)

    divider()

    print("SUMMARY")

    print(f"Datasets        : {len(DATASETS)}")
    print(f"Total Records   : {total_records}")
    print(f"Duplicates      : {total_duplicates}")
    print(f"Blank Values    : {total_blank}")
    print(f"Overall Status  : {overall_status}")

    divider()

    print()

    if overall_status == "PASS":
        print("Reference datasets successfully validated.")
    else:
        print("Validation completed with errors.")

    print()


if __name__ == "__main__":
    main()