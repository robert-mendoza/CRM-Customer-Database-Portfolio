"""
CRM Dataset Build Framework.

Public package interface.

This package provides the core components used to build, validate,
merge, and generate CRM datasets.
"""

from __future__ import annotations

# ==========================================================================
# Package Metadata
# ==========================================================================

from .constants import (
    FRAMEWORK_NAME,
    FRAMEWORK_VERSION,
)

__title__ = FRAMEWORK_NAME
__version__ = FRAMEWORK_VERSION

# ==========================================================================
# Core Models
# ==========================================================================

from .models import (
    Record,
    Severity,
    PartFile,
    DatasetConfig,
    LoadedDataset,
    DatasetStatistics,
    ValidationIssue,
    ValidationReport,
    BuildResult,
)

# ==========================================================================
# Exceptions
# ==========================================================================

from .exceptions import (
    DatasetBuildError,

    ConfigurationError,

    DatasetNotFoundError,
    DatasetImportError,
    DatasetVariableError,
    DatasetFormatError,

    DatasetValidationError,
    RecordCountError,
    DuplicateRecordError,
    DuplicateIdentifierError,
    MissingFieldError,
    EmptyFieldError,
    InvalidFieldError,
    InvalidDataTypeError,
    InvalidSchemaError,

    MergeError,
    MergeConflictError,

    OutputWriteError,
    OutputDirectoryError,

    ReportGenerationError,

    LoggingError,
)

# ==========================================================================
# Public API
# ==========================================================================

__all__ = [

    # Package metadata
    "__title__",
    "__version__",

    # Framework metadata
    "FRAMEWORK_NAME",
    "FRAMEWORK_VERSION",

    # Models
    "Record",
    "Severity",
    "PartFile",
    "DatasetConfig",
    "LoadedDataset",
    "DatasetStatistics",
    "ValidationIssue",
    "ValidationReport",
    "BuildResult",

    # Base exception
    "DatasetBuildError",

    # Configuration
    "ConfigurationError",

    # Loader
    "DatasetNotFoundError",
    "DatasetImportError",
    "DatasetVariableError",
    "DatasetFormatError",

    # Validation
    "DatasetValidationError",
    "RecordCountError",
    "DuplicateRecordError",
    "DuplicateIdentifierError",
    "MissingFieldError",
    "EmptyFieldError",
    "InvalidFieldError",
    "InvalidDataTypeError",
    "InvalidSchemaError",

    # Merge
    "MergeError",
    "MergeConflictError",

    # Writer
    "OutputWriteError",
    "OutputDirectoryError",

    # Reports
    "ReportGenerationError",

    # Logging
    "LoggingError",
]