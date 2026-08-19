"""
Dataset merger for the CRM Dataset Build Framework.

This module merges validated dataset records into a single unified
dataset while preserving record integrity and ordering.

Responsibilities:
    * Merge validated records.
    * Preserve record ordering.
    * Detect merge conflicts.
    * Produce the merged dataset.

The merger does not load datasets, validate records, or write output
files.
"""

from __future__ import annotations

from .exceptions import (
    MergeConflictError,
    MergeError,
)
from .logger import BuildLogger
from .models import (
    LoadedDataset,
    Record,
)

__all__ = [
    "DatasetMerger",
]


class DatasetMerger:
    """
    Merge validated datasets into a unified collection of records.

    The merger assumes that incoming datasets have already passed
    validation. It performs merge-specific processing only.
    """

    def __init__(
        self,
        logger: BuildLogger,
    ) -> None:
        """
        Initialize the dataset merger.

        Args:
            logger:
                Shared framework logger.

        Raises:
            TypeError:
                If ``logger`` is not a BuildLogger instance.
        """
        if not isinstance(logger, BuildLogger):
            raise TypeError(
                "logger must be an instance of BuildLogger."
            )

        self._logger = logger
            def merge(
        self,
        dataset: LoadedDataset,
    ) -> list[Record]:
        """
        Merge a validated dataset into a unified record collection.

        Args:
            dataset:
                Loaded and validated dataset.

        Returns:
            Merged dataset records.

        Raises:
            TypeError:
                If ``dataset`` is not a LoadedDataset instance.

            MergeConflictError:
                If merge conflicts are detected.
        """
        if not isinstance(dataset, LoadedDataset):
            raise TypeError(
                "dataset must be an instance of LoadedDataset."
            )

        self._logger.section(
            "Dataset Merge"
        )

        self._logger.info(
            f"Merging '{dataset.config.name}'."
        )

        self._detect_merge_conflicts(
            dataset,
        )

        merged_records = self._merge_records(
            dataset,
        )

        self._log_summary(
            merged_records,
        )

        return merged_records