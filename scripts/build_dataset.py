"""
Build orchestrator for the CRM Dataset Build Framework.

This module coordinates the complete dataset build pipeline by
invoking the loader, validator, merger, writer, and summary
generator in the correct order.

Responsibilities:
    * Coordinate the dataset build workflow.
    * Share framework services between components.
    * Collect build statistics.
    * Produce the final BuildResult.

The builder does not implement loading, validation, merging,
writing, or report generation logic directly.
"""

from __future__ import annotations

from datetime import datetime

from .loader import DatasetLoader
from .logger import BuildLogger
from .merger import DatasetMerger
from .models import (
    BuildResult,
    DatasetConfig,
    DatasetStatistics,
)
from .summary import SummaryGenerator
from .validator import DatasetValidator
from .writer import DatasetWriter

__all__ = [
    "DatasetBuilder",
]


class DatasetBuilder:
    """
    Coordinates execution of the CRM Dataset Build Framework.

    This class is the orchestration layer of the framework. It
    coordinates the frozen merge engine modules without duplicating
    their responsibilities.
    """

    def __init__(
        self,
        logger: BuildLogger | None = None,
    ) -> None:
        """
        Initialize the dataset builder.

        Args:
            logger:
                Optional shared framework logger. If omitted,
                a new BuildLogger instance is created.
        """
        self._logger = (
            logger
            if logger is not None
            else BuildLogger()
        )

        self._loader = DatasetLoader(
            self._logger,
        )

        self._validator = DatasetValidator(
            self._logger,
        )

        self._merger = DatasetMerger(
            self._logger,
        )

        self._writer = DatasetWriter(
            self._logger,
        )

        self._summary = SummaryGenerator(
            self._logger,
        )"""
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
        def build(
        self,
        config: DatasetConfig,
    ) -> BuildResult:
        """
        Execute the complete dataset build pipeline.

        Args:
            config:
                Dataset configuration.

        Returns:
            Final build result.
        """
        started_at = datetime.now()

        statistics = DatasetStatistics(
            started_at=started_at,
        )

        self._logger.section(
            f"Building Dataset: {config.name}"
        )

        loaded_dataset = self._loader.load(
            config,
        )

        statistics.files_loaded = (
            len(loaded_dataset.source_files)
        )

        statistics.records_loaded = (
            loaded_dataset.record_count
        )

        validation_report = (
            self._validator.validate(
                loaded_dataset,
            )
        )

        merged_records = self._merger.merge(
            loaded_dataset.records,
        )

        statistics.records_written = (
            len(merged_records)
        )

        self._writer.write(
            config,
            merged_records,
        )

        self._summary.generate(
            statistics,
            validation_report,
            config.output_file.with_suffix(
                ".summary.txt",
            ),
        )

        finished_at = datetime.now()

        statistics.finished_at = finished_at

        return BuildResult(
            success=statistics.success,
            output_file=config.output_file,
            statistics=statistics,
            validation_report=validation_report,
            started_at=started_at,
            finished_at=finished_at,
        )
    def build(
        self,
        config: DatasetConfig,
    ) -> BuildResult:
        """
        Execute the complete dataset build pipeline.

        Args:
            config:
                Dataset configuration.

        Returns:
            Final build result.
        """
        started_at = datetime.now()

        statistics = DatasetStatistics(
            started_at=started_at,
        )

        self._logger.section(
            f"Building Dataset: {config.name}"
        )

        loaded_dataset = self._loader.load(
            config,
        )

        statistics.files_loaded = (
            len(loaded_dataset.source_files)
        )

        statistics.records_loaded = (
            loaded_dataset.record_count
        )

        validation_report = (
            self._validator.validate(
                loaded_dataset,
            )
        )

        merged_records = self._merger.merge(
            loaded_dataset.records,
        )

        statistics.records_written = (
            len(merged_records)
        )

        self._writer.write(
            config,
            merged_records,
        )

        self._summary.generate(
            statistics,
            validation_report,
            config.output_file.with_suffix(
                ".summary.txt",
            ),
        )

        finished_at = datetime.now()

        statistics.finished_at = finished_at

        return BuildResult(
            success=statistics.success,
            output_file=config.output_file,
            statistics=statistics,
            validation_report=validation_report,
            started_at=started_at,
            finished_at=finished_at,
        )