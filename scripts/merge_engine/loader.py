"""
Dataset loader for the CRM Dataset Build Framework.

This module is responsible for loading dataset records from one or more
Python source files into a single ``LoadedDataset`` instance.

Responsibilities:
    * Validate loader configuration.
    * Import dataset modules.
    * Extract dataset variables.
    * Aggregate records.
    * Return a LoadedDataset instance.

The loader intentionally does not perform business-rule validation,
duplicate detection, schema validation, merge operations, or output
generation.
"""

from __future__ import annotations

from .exceptions import ConfigurationError
from .logger import BuildLogger
from .models import (
    DatasetConfig,
    LoadedDataset,
    PartFile,
    Record,
)
from .utils.importer import (
    extract_dataset_variable,
    import_python_module,
)

__all__ = [
    "DatasetLoader",
]


class DatasetLoader:
    """
    Loads dataset records from configured source files.

    The loader coordinates configuration validation, module importing,
    dataset extraction, and record aggregation. Validation of dataset
    contents is intentionally delegated to the validator module.
    """

    def __init__(
        self,
        logger: BuildLogger,
    ) -> None:
        """
        Initialize the dataset loader.

        Args:
            logger:
                Framework logger.

        Raises:
            TypeError:
                If ``logger`` is not a ``BuildLogger`` instance.
        """
        if not isinstance(logger, BuildLogger):
            raise TypeError(
                "logger must be an instance of BuildLogger."
            )

        self._logger = logger
            def load(
        self,
        config: DatasetConfig,
    ) -> LoadedDataset:
        """
        Load and aggregate records from all configured dataset parts.

        Args:
            config:
                Dataset build configuration.

        Returns:
            A populated ``LoadedDataset`` instance.

        Raises:
            ConfigurationError:
                If the supplied configuration is invalid.
        """
        self._validate_configuration(config)

        self._logger.section(
            f"Loading dataset: {config.name}"
        )

        records: list[Record] = []

        for part in config.input_files:
            records.extend(
                self._load_part(
                    part=part,
                    config=config,
                )
            )

        loaded_dataset = LoadedDataset(
            config=config,
            records=records,
            source_files=config.input_files,
        )

        self._log_summary(loaded_dataset)

        return loaded_dataset

    def _validate_configuration(
        self,
        config: DatasetConfig,
    ) -> None:
        """
        Validate the loader configuration.

        This method performs structural validation only. Dataset content
        validation is handled by the validator module.

        Args:
            config:
                Dataset configuration.

        Raises:
            ConfigurationError:
                If the configuration is incomplete or invalid.
        """
        if not isinstance(config, DatasetConfig):
            raise ConfigurationError(
                "config must be an instance of DatasetConfig."
            )

        if not config.name.strip():
            raise ConfigurationError(
                "Configuration name cannot be empty."
            )

        if not config.variable_name.strip():
            raise ConfigurationError(
                "Dataset variable name cannot be empty."
            )

        if not config.input_files:
            raise ConfigurationError(
                "At least one input file must be configured."
            )

        for part in config.input_files:

            if not isinstance(part, PartFile):
                raise ConfigurationError(
                    "All input files must be PartFile instances."
                )

            if not part.name.strip():
                raise ConfigurationError(
                    "Part file name cannot be empty."
                )

            if part.path.suffix.lower() != ".py":
                raise ConfigurationError(
                    f"'{part.path}' is not a Python source file."
                )
                def _load_part(
        self,
        part: PartFile,
        config: DatasetConfig,
    ) -> list[Record]:
        """
        Load records from a single dataset source file.

        This method imports the configured Python module, extracts the
        dataset variable defined by the configuration, and returns the
        resulting records.

        Args:
            part:
                Dataset source file definition.

            config:
                Dataset build configuration.

        Returns:
            The records extracted from the dataset module.

        Raises:
            DatasetNotFoundError:
                If the dataset file does not exist.

            DatasetImportError:
                If the dataset module cannot be imported.

            DatasetVariableError:
                If the configured dataset variable is missing.

            DatasetFormatError:
                If the extracted dataset has an invalid structure.
        """
        self._logger.info(
            f"Loading '{part.name}' "
            f"from '{part.path.name}'."
        )

        module = import_python_module(
            part.path,
        )

        records = extract_dataset_variable(
            module=module,
            variable_name=config.variable_name,
        )

        self._logger.success(
            f"Loaded {len(records)} records "
            f"from '{part.name}'."
        )

        return records

    def _log_summary(
        self,
        dataset: LoadedDataset,
    ) -> None:
        """
        Log a summary of the completed loading operation.

        Args:
            dataset:
                The loaded dataset.
        """
        self._logger.section(
            "Dataset loading completed"
        )

        self._logger.info(
            f"Dataset name : {dataset.config.name}"
        )

        self._logger.info(
            f"Source files : {len(dataset.source_files)}"
        )

        self._logger.info(
            f"Records loaded : {dataset.record_count}"
        )