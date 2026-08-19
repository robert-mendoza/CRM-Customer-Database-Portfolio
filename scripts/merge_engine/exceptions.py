"""
Custom exceptions for the CRM Dataset Build Framework.

All framework-specific exceptions inherit from DatasetBuildError.
"""

from __future__ import annotations


# ==========================================================================
# Base Exception
# ==========================================================================

class DatasetBuildError(Exception):
    """
    Base exception for all framework errors.
    """

    pass


# ==========================================================================
# Configuration Exceptions
# ==========================================================================

class ConfigurationError(DatasetBuildError):
    """
    Raised when a dataset configuration is invalid.
    """

    pass


# ==========================================================================
# Loader Exceptions
# ==========================================================================

class DatasetNotFoundError(DatasetBuildError):
    """
    Raised when a dataset file cannot be found.
    """

    pass


class DatasetImportError(DatasetBuildError):
    """
    Raised when a dataset module cannot be imported.
    """

    pass


class DatasetVariableError(DatasetBuildError):
    """
    Raised when the expected dataset variable does not exist.
    """

    pass


class DatasetFormatError(DatasetBuildError):
    """
    Raised when the dataset has an invalid format.
    """

    pass


# ==========================================================================
# Validation Exceptions
# ==========================================================================

class DatasetValidationError(DatasetBuildError):
    """
    Base exception for validation failures.
    """

    pass


class RecordCountError(DatasetValidationError):
    """
    Raised when the record count is incorrect.
    """

    pass


class DuplicateRecordError(DatasetValidationError):
    """
    Raised when duplicate records are detected.
    """

    pass


class DuplicateIdentifierError(DatasetValidationError):
    """
    Raised when duplicate IDs are detected.
    """

    pass


class MissingFieldError(DatasetValidationError):
    """
    Raised when a required field is missing.
    """

    pass


class EmptyFieldError(DatasetValidationError):
    """
    Raised when a required field is empty.
    """

    pass


class InvalidFieldError(DatasetValidationError):
    """
    Raised when a field contains invalid data.
    """

    pass


class InvalidDataTypeError(DatasetValidationError):
    """
    Raised when an unexpected data type is encountered.
    """

    pass


class InvalidSchemaError(DatasetValidationError):
    """
    Raised when the dataset schema does not match expectations.
    """

    pass


# ==========================================================================
# Merge Exceptions
# ==========================================================================

class MergeError(DatasetBuildError):
    """
    Base exception for merge operations.
    """

    pass


class MergeConflictError(MergeError):
    """
    Raised when datasets cannot be merged safely.
    """

    pass


# ==========================================================================
# Writer Exceptions
# ==========================================================================

class OutputWriteError(DatasetBuildError):
    """
    Raised when writing the output file fails.
    """

    pass


class OutputDirectoryError(DatasetBuildError):
    """
    Raised when the output directory is invalid.
    """

    pass


# ==========================================================================
# Report Exceptions
# ==========================================================================

class ReportGenerationError(DatasetBuildError):
    """
    Raised when report generation fails.
    """

    pass


# ==========================================================================
# Logging Exceptions
# ==========================================================================

class LoggingError(DatasetBuildError):
    """
    Raised when logging cannot be initialized or written.
    """

    pass