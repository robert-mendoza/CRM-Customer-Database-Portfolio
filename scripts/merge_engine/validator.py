"""
Dataset validator for the CRM Dataset Build Framework.

This module validates loaded datasets before merge operations. It
performs structural and business-rule validation while preserving the
original dataset records.

Responsibilities:
    * Validate loaded datasets.
    * Verify expected record counts.
    * Validate required fields.
    * Detect empty required fields.
    * Detect duplicate identifiers.
    * Detect duplicate records.
    * Produce a ValidationReport.

The validator does not modify dataset records, merge datasets, or write
output files.
"""

from __future__ import annotations

from .exceptions import (
    DuplicateIdentifierError,
    DuplicateRecordError,
    EmptyFieldError,
    InvalidDataTypeError,
    InvalidFieldError,
    InvalidSchemaError,
    MissingFieldError,
    RecordCountError,
)
from .logger import BuildLogger
from .models import (
    DatasetConfig,
    LoadedDataset,
    Record,
    Severity,
    ValidationIssue,
    ValidationReport,
)

__all__ = [
    "DatasetValidator",
]


class DatasetValidator:
    """
    Validates loaded datasets before merge operations.

    The validator performs structural and business-rule validation
    against the supplied dataset configuration and produces a
    ValidationReport containing all detected validation issues.
    """

    def __init__(
        self,
        logger: BuildLogger,
    ) -> None:
        """
        Initialize the dataset validator.

        Args:
            logger:
                Shared framework logger.

        Raises:
            TypeError:
                If ``logger`` is not an instance of ``BuildLogger``.
        """
        if not isinstance(logger, BuildLogger):
            raise TypeError(
                "logger must be an instance of BuildLogger."
            )

        self._logger = logger