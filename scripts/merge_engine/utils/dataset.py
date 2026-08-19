"""
Dataset utility functions for the CRM Dataset Build Framework.

This module contains reusable helper functions for working with dataset
filenames, output filenames, and record collections.
"""

from __future__ import annotations

from itertools import islice
from pathlib import Path
from typing import Iterable, Iterator, TypeVar

from merge_engine.constants import DEFAULT_OUTPUT_EXTENSION

T = TypeVar("T")


# ==========================================================================
# Filename Helpers
# ==========================================================================

def build_dataset_filename(
    dataset_name: str,
    part_suffix: str,
    *,
    extension: str = DEFAULT_OUTPUT_EXTENSION,
) -> str:
    """
    Build a dataset source filename.

    Example:
        companies_part1A.py

    Args:
        dataset_name:
            Dataset name.

        part_suffix:
            Dataset part suffix.

        extension:
            File extension.

    Returns:
        Dataset filename.
    """

    return f"{dataset_name}_{part_suffix}{extension}"


def build_output_filename(
    dataset_name: str,
    *,
    extension: str = DEFAULT_OUTPUT_EXTENSION,
) -> str:
    """
    Build an output dataset filename.

    Example:
        company.py
        customer.py
        product.py

    Args:
        dataset_name:
            Dataset name.

        extension:
            File extension.

    Returns:
        Output filename.
    """

    if dataset_name.endswith("ies"):
        stem = dataset_name[:-3] + "y"

    elif dataset_name.endswith("s"):
        stem = dataset_name[:-1]

    else:
        stem = dataset_name

    return f"{stem}{extension}"


# ==========================================================================
# Chunk Helpers
# ==========================================================================

def chunk_records(
    records: Iterable[T],
    chunk_size: int,
) -> Iterator[list[T]]:
    """
    Yield records in fixed-size chunks.

    Args:
        records:
            Iterable of records.

        chunk_size:
            Maximum records per chunk.

    Yields:
        Lists containing up to chunk_size records.

    Raises:
        ValueError:
            If chunk_size is less than 1.
    """

    if chunk_size < 1:
        raise ValueError(
            "chunk_size must be greater than zero."
        )

    iterator = iter(records)

    while True:

        chunk = list(
            islice(
                iterator,
                chunk_size,
            )
        )

        if not chunk:
            break

        yield chunk


# ==========================================================================
# Path Helpers
# ==========================================================================

def build_dataset_path(
    directory: Path,
    dataset_name: str,
    part_suffix: str,
) -> Path:
    """
    Build a dataset source path.

    Args:
        directory:
            Base directory.

        dataset_name:
            Dataset name.

        part_suffix:
            Dataset part suffix.

    Returns:
        Complete dataset path.
    """

    return directory / build_dataset_filename(
        dataset_name,
        part_suffix,
    )


def build_output_path(
    directory: Path,
    dataset_name: str,
) -> Path:
    """
    Build an output dataset path.

    Args:
        directory:
            Base directory.

        dataset_name:
            Dataset name.

    Returns:
        Output file path.
    """

    return directory / build_output_filename(
        dataset_name,
    )