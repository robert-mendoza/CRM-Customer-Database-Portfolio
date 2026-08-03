"""
Dataset loading services.

This module loads one or more dataset part files defined by a DatasetConfig
instance and combines them into a single LoadedDataset.

Responsibilities
----------------
* Import dataset modules.
* Read the configured dataset variable.
* Validate the basic dataset structure.
* Merge records from all input files.
* Return a LoadedDataset instance.

The loader intentionally performs only structural validation. Business rule
validation is handled by validator.py.
"""

from __future__ import annotations

from types import ModuleType
from typing import Any

from .exceptions import (
    DatasetConfigurationError,
    DatasetImportError,
    DatasetValidationError,
)
from .logger import BuildLogger
from .models import (
    DatasetConfig,
    LoadedDataset,
    PartFile,
)
from .utils.importer import import_python_module


class DatasetLoader:
    """
    Loads dataset records from one or more Python modules.
    """

    def __init__(
        self,
        logger: BuildLogger,
    ) -> None:
        """
        Initialize the dataset loader.

        Args:
            logger:
                Shared framework logger.
        """

        self._logger = logger

    # ==========================================================
    # Public API
    # ==========================================================

    def load(
        self,
        config: DatasetConfig,
    ) -> LoadedDataset:
        """
        Load all dataset parts defined by the configuration.

        Args:
            config:
                Dataset configuration.

        Returns:
            Fully populated LoadedDataset.
        """

        self._logger.section(
            f"Loading dataset: {config.name}"
        )

        records: list[dict[str, Any]] = []

        for part in config.input_files:
            records.extend(
                self._load_part(
                    part,
                    config,
                )
            )
        self._logger.success(
            (
                f"Loaded {len(records):,} records "
                f"from {len(config.input_files)} part file(s)."
            )
        )

        return LoadedDataset(
            config=config,
            records=records,
        )

    # ==========================================================
    # Private Methods
    # ==========================================================

    def _load_part(
        self,
        part: PartFile,
        config: DatasetConfig,
    ) -> list[dict[str, Any]]:
        """
        Load a single dataset part.

        Args:
            part:
                Dataset part definition.

            config:
                Parent dataset configuration.

        Returns:
            Dataset records loaded from the part file.
        """

        self._logger.info(
            f"Loading part: {part.name}"
        )

        module = self._import_module(
            part,
        )

        dataset = self._extract_dataset(
            module,
            config,
            part,
        )

        self._validate_dataset(
            dataset,
            part,
        )

        self._logger.info(
            (
                f"{part.name}: "
                f"{len(dataset):,} record(s)"
            )
        )

        return dataset

    def _import_module(
        self,
        part: PartFile,
    ) -> ModuleType:
        """
        Import a dataset module.

        Args:
            part:
                Dataset part definition.

        Returns:
            Imported Python module.

        Raises:
            DatasetImportError:
                If the module cannot be imported.
        """

        self._logger.info(
            f"Importing {part.path}"
        )

        try:
            return import_python_module(
                part.path,
            )

        except Exception as exc:
            raise DatasetImportError(
                (
                    f"Unable to import "
                    f"'{part.path}'."
                )
            ) from exc

    def _extract_dataset(
        self,
        module: ModuleType,
        config: DatasetConfig,
        part: PartFile,
    ) -> list[dict[str, Any]]:
        """
        Read the configured dataset variable.

        Args:
            module:
                Imported module.

            config:
                Dataset configuration.

            part:
                Dataset part.

        Returns:
            Dataset records.

        Raises:
            DatasetConfigurationError:
                If the configured variable is missing or invalid.
        """

        variable_name = config.variable_name

        if not hasattr(
            module,
            variable_name,
        ):
            raise DatasetConfigurationError(
                (
                    f"{part.name} does not define "
                    f"'{variable_name}'."
                )
            )

        dataset = getattr(
            module,
            variable_name,
        )

        if not isinstance(
            dataset,
            list,
        ):
            raise DatasetConfigurationError(
                (
                    f"'{variable_name}' in "
                    f"{part.name} "
                    "must be a list."
                )
            )

        return dataset
scripts/merge_engine/loader.py