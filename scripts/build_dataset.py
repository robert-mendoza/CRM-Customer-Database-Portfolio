"""
Main entry point for the CRM Dataset Build Framework.

Example:

    python build_dataset.py companies
"""

from __future__ import annotations

import sys
from pathlib import Path

from merge_engine.configs import DATASET_CONFIGS


def print_banner() -> None:
    print()
    print("=" * 70)
    print("CRM Dataset Build Framework")
    print("=" * 70)
    print()


def print_usage() -> None:
    print(
        "Usage:\n"
        "    python build_dataset.py <dataset>\n"
    )

    print("Available datasets:")

    for dataset in DATASET_CONFIGS:
        print(f"    • {dataset}")


def get_dataset_name() -> str:
    """
    Returns the dataset name from the command line.
    """

    if len(sys.argv) != 2:
        print_usage()
        raise SystemExit(1)

    return sys.argv[1].lower()


def validate_dataset(dataset_name: str) -> None:
    """
    Ensures the requested dataset exists.
    """

    if dataset_name not in DATASET_CONFIGS:

        print()

        print(f"Unknown dataset: {dataset_name}")

        print()

        print_usage()

        raise SystemExit(1)


def main() -> int:
    """
    Application entry point.
    """

    print_banner()

    dataset_name = get_dataset_name()

    validate_dataset(dataset_name)

    config = DATASET_CONFIGS[dataset_name]

    print(f"Dataset : {config.name}")

    print(f"Records : {config.expected_records}")

    print()

    print("Framework initialized successfully.")

    print()

    #
    # Sprint 2
    #

    # loader = DatasetLoader(config)

    # dataset = loader.load()

    # validator = DatasetValidator(dataset)

    # report = validator.validate()

    # merger = DatasetMerger(dataset)

    # merged = merger.merge()

    # writer = DatasetWriter(config)

    # writer.write(merged)

    # summary.generate(...)

    return 0


if __name__ == "__main__":

    raise SystemExit(main())