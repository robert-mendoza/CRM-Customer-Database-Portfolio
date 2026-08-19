"""
Formatting utilities for the CRM Dataset Build Framework.

This module contains reusable helper functions for formatting timestamps,
durations, and generated file headers.
"""

from __future__ import annotations

from datetime import datetime, timedelta

from merge_engine.constants import (
    AUTO_GENERATED_WARNING,
    FRAMEWORK_NAME,
    FRAMEWORK_VERSION,
    OUTPUT_HEADER_TEMPLATE,
    TIMESTAMP_FORMAT,
)


# ==========================================================================
# Timestamp Utilities
# ==========================================================================

def format_timestamp(
    timestamp: datetime | None = None,
) -> str:
    """
    Format a datetime using the framework timestamp format.

    Args:
        timestamp:
            Datetime instance to format.
            If omitted, the current local time is used.

    Returns:
        Formatted timestamp.
    """

    if timestamp is None:
        timestamp = datetime.now()

    return timestamp.strftime(
        TIMESTAMP_FORMAT,
    )


# ==========================================================================
# Duration Utilities
# ==========================================================================

def format_duration(
    duration: timedelta | int | float,
) -> str:
    """
    Convert a duration into HH:MM:SS format.

    Args:
        duration:
            A datetime.timedelta object or the number of elapsed seconds.

    Returns:
        Human-readable duration string.

    Examples:
        00:00:03
        00:05:27
        01:18:45
    """

    if isinstance(duration, (int, float)):
        duration = timedelta(seconds=duration)

    total_seconds = int(duration.total_seconds())

    hours, remainder = divmod(
        total_seconds,
        3600,
    )

    minutes, seconds = divmod(
        remainder,
        60,
    )

    return (
        f"{hours:02d}:"
        f"{minutes:02d}:"
        f"{seconds:02d}"
    )


# ==========================================================================
# Output Header
# ==========================================================================

def generate_output_header(
    dataset_name: str,
    *,
    generated_on: datetime | None = None,
) -> str:
    """
    Generate the standard header for generated dataset files.

    Args:
        dataset_name:
            Dataset name.

        generated_on:
            Optional generation timestamp.
            If omitted, the current local time is used.

    Returns:
        Formatted multi-line file header.
    """

    return OUTPUT_HEADER_TEMPLATE.format(
        framework_name=FRAMEWORK_NAME,
        framework_version=FRAMEWORK_VERSION,
        dataset_name=dataset_name,
        generated_on=format_timestamp(generated_on),
        warning=AUTO_GENERATED_WARNING,
    )