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
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.worksheet.worksheet import Worksheet

from builder.constants import SheetNames
from builder.utils import (
    apply_headers,
    apply_title,
    create_excel_table,
)
from builder.validation_lists import (
    CUSTOMER_STATUSES,
    CUSTOMER_TYPES,
    INDUSTRIES,
    LEAD_SOURCES,
    PRIORITIES,
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

_VALIDATION_START_ROW = 5
_VALIDATION_END_ROW = 1004


def _create_list_validation(
    worksheet: Worksheet,
    values: Sequence[str],
    column: str,
    prompt_title: str,
) -> DataValidation:
    """Create and apply a list validation to a worksheet column.

    Args:
        worksheet: Target worksheet.
        values: Allowed values.
        column: Excel column letter.
        prompt_title: Input prompt title.

    Returns:
        The configured DataValidation object.

    Raises:
        ValueError: If values is empty.
    """
    if not values:
        raise ValueError(
            f"Validation values for column {column} cannot be empty."
        )

    escaped_values = ",".join(
        value.replace('"', '""')
        for value in values
    )

    validation = DataValidation(
        type="list",
        formula1=f'"{escaped_values}"',
        allow_blank=True,
    )

    validation.errorTitle = "Invalid value"
    validation.error = "Select a value from the drop-down list."
    validation.promptTitle = prompt_title
    validation.prompt = "Select a value from the drop-down list."
    validation.showErrorMessage = True
    validation.showInputMessage = True

    validation.add(
        f"{column}{_VALIDATION_START_ROW}:{column}{_VALIDATION_END_ROW}"
    )

    worksheet.add_data_validation(validation)

    return validation


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

    _create_list_validation(
        worksheet,
        INDUSTRIES,
        "F",
        "Industry",
    )

    _create_list_validation(
        worksheet,
        CUSTOMER_TYPES,
        "G",
        "Customer Type",
    )

    _create_list_validation(
        worksheet,
        CUSTOMER_STATUSES,
        "H",
        "Customer Status",
    )

    _create_list_validation(
        worksheet,
        LEAD_SOURCES,
        "I",
        "Lead Source",
    )

    _create_list_validation(
        worksheet,
        PRIORITIES,
        "J",
        "Priority",
    )

    return worksheet


__all__ = [
    "CUSTOMER_HEADERS",
    "CUSTOMER_TABLE_NAME",
    "build_customer_database",
]