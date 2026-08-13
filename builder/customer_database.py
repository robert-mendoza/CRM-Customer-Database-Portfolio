"""Customer database worksheet builder.

This module creates the primary customer database worksheet for the
CRM Customer Database Builder.

Project:
    CRM Customer Database Builder

Author:
    Robert Mendoza
"""

from __future__ import annotations

from collections.abc import Sequence

from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet

from builder.constants import SheetNames
from builder.utils import (
    apply_headers,
    apply_title,
    create_excel_table,
)


CUSTOMER_HEADERS: tuple[str, ...] = (
    "Customer ID",
    "Company Name",
    "Contact Name",
    "Email Address",
    "Phone Number",
    "Industry",
    "Customer Type",
    "Customer Status",
    "Lead Source",
    "Priority",
)

CUSTOMER_TABLE_NAME = "CustomerDatabaseTable"


def build_customer_database(
    workbook: Workbook,
    headers: Sequence[str] = CUSTOMER_HEADERS,
) -> Worksheet:
    """Create and initialize the customer database worksheet.

    Args:
        workbook: Target workbook.
        headers: Ordered customer database column headers.

    Returns:
        The initialized customer database worksheet.

    Raises:
        TypeError: If workbook is not an openpyxl Workbook instance.
        ValueError: If headers are empty or contain duplicate values.
    """
    if not isinstance(workbook, Workbook):
        raise TypeError("workbook must be an openpyxl Workbook instance.")

    normalized_headers = tuple(
        str(header).strip()
        for header in headers
    )

    if not normalized_headers:
        raise ValueError(
            "Customer database headers cannot be empty."
        )

    if any(not header for header in normalized_headers):
        raise ValueError(
            "Customer database headers cannot contain empty values."
        )

    if len(normalized_headers) != len(set(normalized_headers)):
        raise ValueError(
            "Customer database headers must be unique."
        )

    worksheet_name = SheetNames.customer_database

    if worksheet_name in workbook.sheetnames:
        worksheet = workbook[worksheet_name]
    else:
        worksheet = workbook.create_sheet(worksheet_name)

    content_start_row = apply_title(
        worksheet,
        title="Customer Database",
        subtitle="CRM customer and contact records",
    )

    apply_headers(
        worksheet,
        normalized_headers,
        row=content_start_row,
        enable_filter=True,
    )

    table_end_column = len(normalized_headers)

    create_excel_table(
        worksheet,
        table_name=CUSTOMER_TABLE_NAME,
        start_row=content_start_row,
        end_row=content_start_row,
        start_column=1,
        end_column=table_end_column,
    )

    return worksheet


__all__ = [
    "CUSTOMER_HEADERS",
    "CUSTOMER_TABLE_NAME",
    "build_customer_database",
]