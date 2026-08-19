"""
Configuration for the Companies dataset.

This module defines the dataset configuration used by the CRM Dataset
Build Framework when building the master company dataset.
"""

from __future__ import annotations

from merge_engine.constants import (
    DATA_DIR,
    DATASET_PART_SUFFIXES,
    DEFAULT_RECORDS_PER_PART,
    DEFAULT_TOTAL_RECORDS,
)

from merge_engine.models import (
    DatasetConfig,
    PartFile,
)


# ==========================================================================
# Internal Helpers
# ==========================================================================

_PART_DESCRIPTIONS = (
    "Technology and Software Companies",
    "Financial and Professional Services",
    "Healthcare and Manufacturing Companies",
    "Retail, Logistics, and Energy Companies",
)


def _build_part_files() -> tuple[PartFile, ...]:
    """
    Build the list of dataset source files.

    Returns:
        Tuple containing the four source dataset definitions.
    """

    return tuple(
        PartFile(
            name=f"Part {suffix}",
            path=DATA_DIR / f"companies_{suffix}.py",
            expected_records=DEFAULT_RECORDS_PER_PART,
            description=description,
        )
        for suffix, description in zip(
            DATASET_PART_SUFFIXES,
            _PART_DESCRIPTIONS,
            strict=True,
        )
    )


# ==========================================================================
# Public Dataset Configuration
# ==========================================================================

COMPANIES_CONFIG = DatasetConfig(
    name="Companies",

    variable_name="COMPANIES",

    input_files=_build_part_files(),

    output_file=DATA_DIR / "company.py",

    expected_records=DEFAULT_TOTAL_RECORDS,

    id_field="company_id",

    required_fields=(
        "company_id",
        "company_name",
        "industry",
        "country",
    ),
)