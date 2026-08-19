"""
Summary report generator for the CRM Dataset Build Framework.

This module generates a human-readable summary report describing the
results of a completed dataset build. It summarizes build statistics,
validation results, and output information.

Responsibilities:
    * Generate build summary reports.
    * Persist summary reports.
    * Log summary generation.

The summary generator does not load datasets, validate records,
merge datasets, or write dataset source files.
"""

from __future__ import annotations

from pathlib import Path

from .exceptions import ReportGenerationError
from .logger import BuildLogger
from .models import (
    DatasetStatistics,
    ValidationReport,
)

__all__ = [
    "SummaryGenerator",
]


class SummaryGenerator:
    """
    Generates summary reports for completed dataset builds.

    The summary report provides a concise overview of the build
    execution, including validation results, dataset statistics,
    and output information.
    """

    def __init__(
        self,
        logger: BuildLogger,
    ) -> None:
        """
        Initialize the summary generator.

        Args:
            logger:
                Shared framework logger.

        Raises:
            TypeError:
                If ``logger`` is not an instance of
                ``BuildLogger``.
        """
        if not isinstance(logger, BuildLogger):
            raise TypeError(
                "logger must be an instance of BuildLogger."
            )

        self._logger = logger
            def generate(
        self,
        statistics: DatasetStatistics,
        validation_report: ValidationReport,
        output_file: Path,
    ) -> Path:
        """
        Generate the build summary report.

        Args:
            statistics:
                Build statistics collected during execution.

            validation_report:
                Validation results produced by the validator.

            output_file:
                Destination summary report.

        Returns:
            Path to the generated summary report.

        Raises:
            TypeError:
                If any supplied argument has an invalid type.

            ReportGenerationError:
                If summary generation fails.
        """
        if not isinstance(statistics, DatasetStatistics):
            raise TypeError(
                "statistics must be an instance of "
                "DatasetStatistics."
            )

        if not isinstance(
            validation_report,
            ValidationReport,
        ):
            raise TypeError(
                "validation_report must be an instance of "
                "ValidationReport."
            )

        if not isinstance(output_file, Path):
            raise TypeError(
                "output_file must be an instance of Path."
            )

        self._logger.section(
            "Summary Report"
        )

        self._logger.info(
            f"Generating '{output_file.name}'."
        )

        report_text = self._build_report(
            statistics,
            validation_report,
        )

        self._write_report(
            output_file,
            report_text,
        )

        self._log_summary(
            output_file,
        )

        return output_file
        def _build_report(
        self,
        statistics: DatasetStatistics,
        validation_report: ValidationReport,
    ) -> str:
        """
        Build the summary report text.

        Args:
            statistics:
                Dataset build statistics.

            validation_report:
                Validation report.

        Returns:
            Human-readable summary report.
        """
        from datetime import datetime

        from .constants import (
            FRAMEWORK_NAME,
            FRAMEWORK_VERSION,
            TIMESTAMP_FORMAT,
        )

        lines = [
            FRAMEWORK_NAME,
            f"Framework Version : {FRAMEWORK_VERSION}",
            f"Generated On      : "
            f"{datetime.now().strftime(TIMESTAMP_FORMAT)}",
            "",
            "Build Statistics",
            "----------------",
            f"Files Loaded      : {statistics.files_loaded}",
            f"Files Failed      : {statistics.files_failed}",
            f"Records Loaded    : {statistics.records_loaded}",
            f"Records Written   : {statistics.records_written}",
            f"Warnings          : {statistics.warning_count}",
            f"Errors            : {statistics.error_count}",
            "",
            "Validation",
            "----------",
            f"Issues            : {len(validation_report.issues)}",
            f"Warnings          : "
            f"{validation_report.warning_count}",
            f"Errors            : "
            f"{validation_report.error_count}",
            "",
            f"Build Successful  : {statistics.success}",
        ]

        return "\n".join(lines)

    def _write_report(
        self,
        output_file: Path,
        report_text: str,
    ) -> None:
        """
        Write the summary report to disk.

        Args:
            output_file:
                Destination report file.

            report_text:
                Report contents.

        Raises:
            ReportGenerationError:
                If writing fails.
        """
        from .constants import ENCODING

        try:
            output_file.parent.mkdir(
                parents=True,
                exist_ok=True,
            )

            output_file.write_text(
                report_text,
                encoding=ENCODING,
            )

        except OSError as exc:
            raise ReportGenerationError(
                f"Unable to write summary report: "
                f"{output_file}"
            ) from exc

    def _log_summary(
        self,
        output_file: Path,
    ) -> None:
        """
        Log summary generation results.

        Args:
            output_file:
                Generated summary report.
        """
        self._logger.section(
            "Summary Generation Complete"
        )

        self._logger.info(
            f"Summary report : {output_file}"
        )

        self._logger.success(
            "Summary report generated successfully."
        )