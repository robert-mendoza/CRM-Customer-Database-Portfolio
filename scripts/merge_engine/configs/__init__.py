"""
Dataset configuration package.

This package exposes all dataset configurations supported by the
CRM Dataset Build Framework.
"""

from __future__ import annotations

from types import MappingProxyType

from .companies import COMPANIES_CONFIG

DATASET_CONFIGS = MappingProxyType(
    {
        "companies": COMPANIES_CONFIG,
    }
)

__all__ = [
    "COMPANIES_CONFIG",
    "DATASET_CONFIGS",
]