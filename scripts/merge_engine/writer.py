"""
Dataset writer for the CRM Dataset Build Framework.

This module writes merged dataset records to the configured output
Python source file. It is responsible only for persisting the final
dataset and does not perform loading, validation, or merge logic.

Responsibilities:
    * Generate the output dataset source.
    * Create output directories when required.
    * Write the generated dataset file.
    * Log write operations.

The writer assumes that all incoming records have already been
validated and merged.
"""

from __future__ import annotations

from pathlib import Path

from .exceptions import (
    OutputDirectoryError,
    OutputWriteError,
)
from .logger import BuildLogger
from .models import (
    DatasetConfig,
    Record,
)

__all__ = [
    "DatasetWriter",
]


class DatasetWriter:
    """
    Writes merged datasets to the configured output file.

    The writer is the final stage of the dataset build pipeline. It
    receives merged records and persists them using the repository's
    configured output format.
    """

    def __init__(
        self,
        logger: BuildLogger,
    ) -> None:
        """
        Initialize the dataset writer.

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
            def write(
        self,
        config: DatasetConfig,
        records: list[Record],
    ) -> Path:
        """
        Write the merged dataset to the configured output file.

        Args:
            config:
                Dataset configuration.

            records:
                Merged dataset records.

        Returns:
            Path to the generated output file.

        Raises:
            TypeError:
                If the supplied arguments are invalid.

            OutputDirectoryError:
                If the output directory cannot be prepared.

            OutputWriteError:
                If writing the output file fails.
        """
        if not isinstance(config, DatasetConfig):
            raise TypeError(
                "config must be an instance of DatasetConfig."
            )

        if not isinstance(records, list):
            raise TypeError(
                "records must be a list of Record objects."
            )

        self._logger.section(
            "Dataset Writer"
        )

        self._logger.info(
            f"Writing '{config.output_file.name}'."
        )

        self._ensure_output_directory(
            config.output_file.parent,
        )

        source = self._build_output_source(
            config,
            records,
        )

        self._write_output_file(
            config.output_file,
            source,
        )

        self._log_summary(
            config.output_file,
            len(records),
        )

        return config.output_file
        def _ensure_output_directory(
        self,
        directory: Path,
    ) -> None:
        """
        Ensure that the output directory exists.

        Args:
            directory:
                Output directory.

        Raises:
            OutputDirectoryError:
                If the directory cannot be created.
        """
        try:
            directory.mkdir(
                parents=True,
                exist_ok=True,
            )
        except OSError as exc:
            raise OutputDirectoryError(
                f"Unable to create output directory: {directory}"
            ) from exc

    def _build_output_source(
        self,
        config: DatasetConfig,
        records: list[Record],
    ) -> str:
        """
        Build the Python source for the output dataset.

        Args:
            config:
                Dataset configuration.

            records:
                Merged dataset records.

        Returns:
            Complete Python source code.
        """
        from datetime import datetime
        from pprint import pformat

        from .constants import (
            AUTO_GENERATED_WARNING,
            FRAMEWORK_NAME,
            FRAMEWORK_VERSION,
            OUTPUT_HEADER_TEMPLATE,
            TIMESTAMP_FORMAT,
        )

        header = OUTPUT_HEADER_TEMPLATE.format(
            framework_name=FRAMEWORK_NAME,
            framework_version=FRAMEWORK_VERSION,
            dataset_name=config.name,
            generated_on=datetime.now().strftime(
                TIMESTAMP_FORMAT,
            ),
            warning=AUTO_GENERATED_WARNING,
        )

        body = (
            f"{config.variable_name} = "
            f"{pformat(records, sort_dicts=False)}\n"
        )

        return header + "\n" + body

    def _write_output_file(
        self,
        output_file: Path,
        source: str,
    ) -> None:
        """
        Write the generated source to disk.

        Args:
            output_file:
                Destination file.

            source:
                Generated Python source.

        Raises:
            OutputWriteError:
                If writing fails.
        """
        from .constants import ENCODING

        try:
            output_file.write_text(
                source,
                encoding=ENCODING,
            )
        except OSError as exc:
            raise OutputWriteError(
                f"Failed to write output file: {output_file}"
            ) from exc

    def _log_summary(
        self,
        output_file: Path,
        record_count: int,
    ) -> None:
        """
        Log the writer summary.

        Args:
            output_file:
                Generated output file.

            record_count:
                Number of records written.
        """
        self._logger.section(
            "Writer Summary"
        )

        self._logger.info(
            f"Output file : {output_file}"
        )

        self._logger.info(
            f"Records     : {record_count}"
        )

        self._logger.success(
            "Dataset written successfully."
        )