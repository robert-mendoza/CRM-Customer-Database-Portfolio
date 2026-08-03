"""
Import utilities for the CRM Dataset Build Framework.

This module provides helper functions for dynamically importing Python
modules and extracting dataset variables from them.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path
from types import ModuleType
from typing import Any

from merge_engine.exceptions import (
    DatasetFormatError,
    DatasetImportError,
    DatasetNotFoundError,
    DatasetVariableError,
)
from merge_engine.models import Record


# ==========================================================================
# Module Import
# ==========================================================================

def import_python_module(path: Path) -> ModuleType:
    """
    Import a Python module from a file path.

    Args:
        path:
            Path to the Python source file.

    Returns:
        Imported module.

    Raises:
        DatasetNotFoundError:
            If the source file does not exist.

        DatasetImportError:
            If the module cannot be imported.
    """

    if not path.is_file():
        raise DatasetNotFoundError(
            f"Dataset file does not exist: {path}"
        )

    module_name = path.stem

    spec = importlib.util.spec_from_file_location(
        module_name,
        path,
    )

    if spec is None or spec.loader is None:
        raise DatasetImportError(
            f"Unable to create import specification for '{path}'."
        )

    module = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(module)

    except Exception as exc:
        raise DatasetImportError(
            f"Failed to import '{path}'."
        ) from exc

    return module


# ==========================================================================
# Dataset Extraction
# ==========================================================================

def extract_dataset_variable(
    module: ModuleType,
    variable_name: str,
) -> list[Record]:
    """
    Extract a dataset variable from an imported module.

    Args:
        module:
            Imported Python module.

        variable_name:
            Dataset variable name (for example, COMPANIES).

    Returns:
        List of dataset records.

    Raises:
        DatasetVariableError:
            If the variable is missing.

        DatasetFormatError:
            If the dataset structure is invalid.
    """

    if not hasattr(module, variable_name):
        raise DatasetVariableError(
            f"Module '{module.__name__}' "
            f"does not define '{variable_name}'."
        )

    records: Any = getattr(module, variable_name)

    if not isinstance(records, list):
        raise DatasetFormatError(
            f"'{variable_name}' must be a list."
        )

    for index, record in enumerate(records, start=1):

        if not isinstance(record, dict):
            raise DatasetFormatError(
                f"Record {index} in '{variable_name}' "
                f"is not a dictionary."
            )

    return records