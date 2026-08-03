"""
Core data models for the CRM Dataset Build Framework.

These dataclasses define the shared structures used throughout the
framework, including configuration, loading, validation,
statistics, and build results.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import StrEnum
from pathlib import Path
from typing import Any

# ----------------------------------------------------------------------
# Type Aliases
# ----------------------------------------------------------------------

Record = dict[str, Any]

# ----------------------------------------------------------------------
# Enums
# ----------------------------------------------------------------------


class Severity(StrEnum):
    """
    Validation severity levels.
    """

    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"


# ----------------------------------------------------------------------
# Configuration Models
# ----------------------------------------------------------------------


@dataclass(frozen=True, slots=True)
class PartFile:
    """
    Represents a single dataset source file.
    """

    name: str
    path: Path
    expected_records: int
    description: str = ""


@dataclass(frozen=True, slots=True)
class DatasetConfig:
    """
    Configuration required to build a dataset.
    """

    name: str

    variable_name: str

    input_files: tuple[PartFile, ...]

    output_file: Path

    expected_records: int

    id_field: str

    required_fields: tuple[str, ...]


# ----------------------------------------------------------------------
# Loader Models
# ----------------------------------------------------------------------


@dataclass(slots=True)
class LoadedDataset:
    """
    Represents a dataset after loading but before validation.
    """

    config: DatasetConfig

    records: list[Record]

    source_files: tuple[PartFile, ...]

    loaded_at: datetime = field(default_factory=datetime.now)

    @property
    def record_count(self) -> int:
        """
        Returns the number of loaded records.
        """
        return len(self.records)


# ----------------------------------------------------------------------
# Statistics
# ----------------------------------------------------------------------


@dataclass(slots=True)
class DatasetStatistics:
    """
    Statistics collected during the dataset build.
    """

    files_loaded: int = 0

    files_failed: int = 0

    records_loaded: int = 0

    records_written: int = 0

    duplicate_ids: int = 0

    duplicate_names: int = 0

    missing_fields: int = 0

    empty_fields: int = 0

    warning_count: int = 0

    error_count: int = 0

    started_at: datetime | None = None

    finished_at: datetime | None = None

    def add_warning(self) -> None:
        """
        Increment the warning counter.
        """
        self.warning_count += 1

    def add_error(self) -> None:
        """
        Increment the error counter.
        """
        self.error_count += 1

    @property
    def success(self) -> bool:
        """
        Returns True when the build completed without errors.
        """
        return self.error_count == 0

    @property
    def duration_seconds(self) -> float:
        """
        Returns the build duration in seconds.
        """
        if self.started_at is None or self.finished_at is None:
            return 0.0

        return (
            self.finished_at - self.started_at
        ).total_seconds()


# ----------------------------------------------------------------------
# Validation Models
# ----------------------------------------------------------------------


@dataclass(frozen=True, slots=True)
class ValidationIssue:
    """
    Represents a single validation issue.
    """

    severity: Severity

    message: str

    file_name: str | None = None

    record_id: str | None = None

    field_name: str | None = None

    value: Any = None


@dataclass(slots=True)
class ValidationReport:
    """
    Collection of validation issues.
    """

    issues: list[ValidationIssue] = field(default_factory=list)

    @property
    def info_count(self) -> int:
        return sum(
            issue.severity is Severity.INFO
            for issue in self.issues
        )

    @property
    def warning_count(self) -> int:
        return sum(
            issue.severity is Severity.WARNING
            for issue in self.issues
        )

    @property
    def error_count(self) -> int:
        return sum(
            issue.severity is Severity.ERROR
            for issue in self.issues
        )

    @property
    def has_warnings(self) -> bool:
        return self.warning_count > 0

    @property
    def has_errors(self) -> bool:
        return self.error_count > 0

    @property
    def passed(self) -> bool:
        return not self.has_errors

    def add_issue(self, issue: ValidationIssue) -> None:
        """
        Add a validation issue.
        """
        self.issues.append(issue)

    def extend(self, issues: list[ValidationIssue]) -> None:
        """
        Add multiple validation issues.
        """
        self.issues.extend(issues)

    def clear(self) -> None:
        """
        Remove all validation issues.
        """
        self.issues.clear()


# ----------------------------------------------------------------------
# Build Result
# ----------------------------------------------------------------------


@dataclass(frozen=True, slots=True)
class BuildResult:
    """
    Final result returned by the build engine.
    """

    success: bool

    output_file: Path

    statistics: DatasetStatistics

    validation_report: ValidationReport

    started_at: datetime

    finished_at: datetime

    @property
    def duration_seconds(self) -> float:
        """
        Returns the total build duration.
        """
        return (
            self.finished_at - self.started_at
        ).total_seconds()