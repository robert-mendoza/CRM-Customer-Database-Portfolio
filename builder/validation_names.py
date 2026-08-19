"""Workbook defined names for CRM validation lists.

Project:
    CRM Customer Database Builder

Author:
    Robert Mendoza
"""

from __future__ import annotations

from openpyxl import Workbook
from openpyxl.workbook.defined_name import DefinedName

from builder.constants import SheetNames


VALIDATION_DEFINED_NAMES: tuple[tuple[str, str], ...] = (
    ("CustomerStatuses", "'04_Validation_Lists'!$A$2:$A$4"),
    ("CustomerTypes", "'04_Validation_Lists'!$B$2:$B$5"),
    ("Industries", "'04_Validation_Lists'!$C$2:$C$10"),
    ("LeadSources", "'04_Validation_Lists'!$D$2:$D$7"),
    ("Priorities", "'04_Validation_Lists'!$E$2:$E$5"),
)


def build_validation_defined_names(workbook: Workbook) -> None:
    """Create defined names for the validation-list ranges.

    Args:
        workbook: Target workbook.

    Raises:
        TypeError: If workbook is not an openpyxl Workbook instance.
        ValueError: If the validation worksheet does not exist.
    """
    if not isinstance(workbook, Workbook):
        raise TypeError("workbook must be an openpyxl Workbook instance.")

    worksheet_name = SheetNames.validation_lists

    if worksheet_name not in workbook.sheetnames:
        raise ValueError(
            f"Worksheet {worksheet_name!r} must exist before "
            "defined names are created."
        )

    for name, reference in VALIDATION_DEFINED_NAMES:
        workbook.defined_names.add(
            DefinedName(
                name,
                attr_text=reference,
            )
        )


__all__ = [
    "VALIDATION_DEFINED_NAMES",
    "build_validation_defined_names",
]