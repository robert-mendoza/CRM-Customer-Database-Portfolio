"""Activity Log worksheet builder for the CRM Customer Database Builder.

Project:
    CRM Customer Database Builder

Author:
    Robert Mendoza
"""

from __future__ import annotations

from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet

from builder.constants import SheetNames
from builder.styles import styles
from builder.utils import apply_headers, apply_title, create_excel_table


ACTIVITY_LOG_HEADERS: tuple[str, ...] = (
    "Activity ID",
    "Timestamp",
    "Customer ID",
    "Activity Type",
    "Description",
    "User",
)

ACTIVITY_LOG_TABLE_NAME = "ActivityLogTable"
_ACTIVITY_LOG_HEADER_ROW = 4


def build_activity_log(workbook: Workbook) -> Worksheet:
    """Build the empty Activity Log worksheet and table structure.

    Args:
        workbook: Target openpyxl workbook.

    Returns:
        The completed Activity Log worksheet.

    Raises:
        TypeError: If ``workbook`` is not an openpyxl Workbook instance.
        ValueError: If the Activity Log worksheet already exists.
    """
    if not isinstance(workbook, Workbook):
        raise TypeError("workbook must be an openpyxl Workbook instance.")

    worksheet_name = SheetNames.activity_log
    if worksheet_name in workbook.sheetnames:
        raise ValueError(f"Worksheet '{worksheet_name}' already exists.")

    worksheet = workbook.create_sheet(title=worksheet_name)
    apply_title(worksheet, "Activity Log")
    apply_headers(
        worksheet,
        ACTIVITY_LOG_HEADERS,
        row=_ACTIVITY_LOG_HEADER_ROW,
        enable_filter=True,
    )

    create_excel_table(
        worksheet=worksheet,
        table_name=ACTIVITY_LOG_TABLE_NAME,
        start_row=_ACTIVITY_LOG_HEADER_ROW,
        end_row=_ACTIVITY_LOG_HEADER_ROW,
        start_column=1,
        end_column=len(ACTIVITY_LOG_HEADERS),
    )

    worksheet.column_dimensions["A"].width = 18
    worksheet.column_dimensions["B"].width = 22
    worksheet.column_dimensions["C"].width = 18
    worksheet.column_dimensions["D"].width = 20
    worksheet.column_dimensions["E"].width = 40
    worksheet.column_dimensions["F"].width = 20
    worksheet.sheet_view.zoomScale = 100
    worksheet.freeze_panes = "A5"

    return worksheet


__all__ = [
    "ACTIVITY_LOG_HEADERS",
    "ACTIVITY_LOG_TABLE_NAME",
    "build_activity_log",
]
