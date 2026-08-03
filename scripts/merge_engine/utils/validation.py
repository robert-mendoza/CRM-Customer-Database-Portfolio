"""
Validation utilities for the CRM Dataset Build Framework.

This module provides reusable helper functions for validating the
runtime environment and dataset records.
"""

from __future__ import annotations

import sys
from typing import Iterable

from merge_engine.constants import PYTHON_MINIMUM_VERSION
from merge_engine.exceptions import (
    EmptyFieldError,
    InvalidDataTypeError,
    MissingFieldError,
)
from merge_engine.models import Record


# ==========================================================================
# Python Runtime Validation
# ==========================================================================

def validate_python_version() -> None:
    """
    Validate the current Python interpreter version.

    Raises:
        RuntimeError:
            If the running Python version is lower than the
            framework requirement.
    """

    if sys.version_info < PYTHON_MINIMUM_VERSION:

        required = ".".join(
            map(str, PYTHON_MINIMUM_VERSION)
        )

        current = ".".join(
            map(str, sys.version_info[:3])
        )

        raise RuntimeError(
            f"Python {required} or later is required "
            f"(current: {current})."
        )


# ==========================================================================
# Record Validation
# ==========================================================================

def validate_required_fields(
    record: Record,
    required_fields: Iterable[str],
) -> None:
    """
    Ensure all required fields exist and contain values.

    Args:
        record:
            Dataset record.

        required_fields:
            Required field names.

    Raises:
        MissingFieldError:
            If a required field is missing.

        EmptyFieldError:
            If a required field contains None or an empty string.
    """

    for field in required_fields:

        if field not in record:
            raise MissingFieldError(
                f"Missing required field: '{field}'."
            )

        value = record[field]

        if value is None:
            raise EmptyFieldError(
                f"Field '{field}' cannot be None."
            )

        if isinstance(value, str):

            if not value.strip():

                raise EmptyFieldError(
                    f"Field '{field}' cannot be empty."
                )


# ==========================================================================
# Record Structure Validation
# ==========================================================================

def validate_record_structure(
    record: Record,
) -> None:
    """
    Validate a single dataset record.

    Args:
        record:
            Dataset record.

    Raises:
        InvalidDataTypeError:
            If the record is not a dictionary.
    """

    if not isinstance(record, dict):

        raise InvalidDataTypeError(
            "Each dataset record must be a dictionary."
        )