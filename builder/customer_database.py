"""Customer database worksheet builder.

This module creates the primary customer database worksheet
for the CRM Customer Database Builder.

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
    apply_title,
    create_excel_table,
)
from builder.validation_names import (
    build_validation_defined_names,
)


CUSTOMER_HEADERS: tuple[str, ...] = (
    "Customer ID",
    "First Name",
    "Last Name",
    "Email",
    "Phone",
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
    formula: str,
    column: str,
    prompt_title: str,
) -> DataValidation:
    """Create and apply a list validation to a worksheet column.

    Args:
        worksheet: Target worksheet.
        formula: Excel formula referencing a validation list.
        column: Excel column letter.
        prompt_title: Input prompt title.

    Returns:
        The configured DataValidation object.

    Raises:
        ValueError: If formula is empty.
    """
    if not formula:
        raise ValueError(
            f"Validation formula for column {column} cannot be empty."
        )

    validation = DataValidation(
        type="list",
        formula1=formula,
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
    """Build the customer database worksheet.

    Args:
        workbook: Target workbook.
        headers: Customer database column headers.

    Returns:
        The completed customer database worksheet.
    """
    worksheet = workbook.create_sheet(
        title=SheetNames.customer_database,
    )

    apply_title(
        worksheet,
        "Customer Database",
    )

    for column_index, header in enumerate(headers, start=1):
        worksheet.cell(
            row=4,
            column=column_index,
            value=header,
        )

    create_excel_table(
        worksheet=worksheet,
        table_name=CUSTOMER_TABLE_NAME,
        start_row=4,
        end_row=4,
        start_column=1,
        end_column=len(headers),
    )

    _create_list_validation(
        worksheet=worksheet,
        formula="=Industries",
        column="F",
        prompt_title="Industry",
    )

    _create_list_validation(
        worksheet=worksheet,
        formula="=CustomerTypes",
        column="G",
        prompt_title="Customer Type",
    )

    _create_list_validation(
        worksheet=worksheet,
        formula="=CustomerStatuses",
        column="H",
        prompt_title="Customer Status",
    )

    _create_list_validation(
        worksheet=worksheet,
        formula="=LeadSources",
        column="I",
        prompt_title="Lead Source",
    )

    _create_list_validation(
        worksheet=worksheet,
        formula="=Priorities",
        column="J",
        prompt_title="Priority",
    )

    build_validation_defined_names(workbook)

    return worksheet


__all__ = [
    "CUSTOMER_HEADERS",
    "CUSTOMER_TABLE_NAME",
    "build_customer_database",
]