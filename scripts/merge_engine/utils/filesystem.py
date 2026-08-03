"""
Filesystem utilities for the CRM Dataset Build Framework.

This module provides reusable helper functions for common filesystem
operations such as creating directories, reading and writing text files,
copying files, deleting files, and checking file existence.
"""

from __future__ import annotations

import shutil
from pathlib import Path

from merge_engine.constants import ENCODING


# ==========================================================================
# Directory Utilities
# ==========================================================================

def ensure_directory(directory: Path) -> Path:
    """
    Create a directory and all missing parent directories.

    If the directory already exists, no action is taken.

    Args:
        directory:
            Directory to create.

    Returns:
        The directory path.
    """

    directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    return directory


# ==========================================================================
# File Utilities
# ==========================================================================

def file_exists(path: Path) -> bool:
    """
    Determine whether a file exists.

    Args:
        path:
            File path.

    Returns:
        True if the file exists, otherwise False.
    """

    return path.is_file()


def safe_read_text(
    path: Path,
    encoding: str = ENCODING,
) -> str:
    """
    Read the contents of a text file.

    Args:
        path:
            File to read.

        encoding:
            Text encoding.

    Returns:
        File contents.

    Raises:
        FileNotFoundError:
            If the file does not exist.
    """

    if not path.is_file():
        raise FileNotFoundError(path)

    return path.read_text(
        encoding=encoding,
    )


def safe_write_text(
    path: Path,
    content: str,
    encoding: str = ENCODING,
) -> None:
    """
    Write text to a file.

    The parent directory is created automatically if necessary.

    Args:
        path:
            Destination file.

        content:
            Text to write.

        encoding:
            Output encoding.
    """

    ensure_directory(path.parent)

    path.write_text(
        content,
        encoding=encoding,
    )


def backup_file(
    source: Path,
    destination: Path,
) -> Path:
    """
    Create a backup copy of a file.

    Args:
        source:
            Existing source file.

        destination:
            Backup destination.

    Returns:
        Destination path.

    Raises:
        FileNotFoundError:
            If the source file does not exist.
    """

    if not source.is_file():
        raise FileNotFoundError(source)

    ensure_directory(destination.parent)

    shutil.copy2(
        source,
        destination,
    )

    return destination


def delete_file(path: Path) -> bool:
    """
    Delete a file if it exists.

    Args:
        path:
            File to delete.

    Returns:
        True if the file was deleted.
        False if the file did not exist.
    """

    if not path.is_file():
        return False

    path.unlink()

    return True