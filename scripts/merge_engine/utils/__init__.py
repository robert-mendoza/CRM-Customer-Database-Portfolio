"""
Shared utility package for the CRM Dataset Build Framework.

The utility package contains reusable helper functions grouped by
functional area.

Modules
-------
filesystem
    File and directory operations.

importer
    Dynamic Python module importing.

formatter
    Timestamp and output formatting.

dataset
    Dataset filename helpers.

validation
    Generic validation helpers.

text
    Text formatting helpers.
"""

from __future__ import annotations

# Filesystem

from .filesystem import (
    ensure_directory,
    file_exists,
    safe_read_text,
    safe_write_text,
)

# Import Helpers

from .importer import (
    extract_dataset_variable,
    import_python_module,
)

# Formatter

from .formatter import (
    format_duration,
    format_timestamp,
    generate_output_header,
)

# Dataset Helpers

from .dataset import (
    build_dataset_filename,
    build_output_filename,
    chunk_records,
)

# Validation

from .validation import (
    validate_python_version,
)

# Text Helpers

from .text import (
    indent_text,
    normalize_line_endings,
    pluralize,
)

__all__ = [

    # Filesystem

    "ensure_directory",
    "file_exists",
    "safe_read_text",
    "safe_write_text",

    # Importer

    "import_python_module",
    "extract_dataset_variable",

    # Formatter

    "format_timestamp",
    "format_duration",
    "generate_output_header",

    # Dataset

    "build_dataset_filename",
    "build_output_filename",
    "chunk_records",

    # Validation

    "validate_python_version",

    # Text

    "pluralize",
    "indent_text",
    "normalize_line_endings",
]