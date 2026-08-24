"""Unit and integration tests for the Activity Log builder."""

from __future__ import annotations

from pathlib import Path

from openpyxl import Workbook, load_workbook

from builder.activity_log import ACTIVITY_LOG_HEADERS, ACTIVITY_LOG_TABLE_NAME, build_activity_log
from builder.constants import SheetNames


def test_activity_log_builds_empty_sheet(tmp_path: Path) -> None:
    """Verify the Activity Log sheet contract when no records exist."""
    workbook = Workbook()
    workbook.remove(workbook.active)

    worksheet = build_activity_log(workbook)

    assert worksheet.title == SheetNames.activity_log

    assert [
        worksheet.cell(row=4, column=index).value
        for index in range(1, len(ACTIVITY_LOG_HEADERS) + 1)
    ] == list(ACTIVITY_LOG_HEADERS)

    assert ACTIVITY_LOG_TABLE_NAME in worksheet.tables
    assert worksheet.tables[ACTIVITY_LOG_TABLE_NAME].ref == "A4:F4"
    assert worksheet.max_row == 4
    assert worksheet.max_column == 6
    assert worksheet.freeze_panes == "A5"

    output = tmp_path / "activity_log.xlsx"
    workbook.save(output)

    reopened = load_workbook(output, data_only=False)

    assert SheetNames.activity_log in reopened.sheetnames
    reopened_worksheet = reopened[SheetNames.activity_log]
    assert ACTIVITY_LOG_TABLE_NAME in reopened_worksheet.tables
    assert reopened_worksheet.tables[ACTIVITY_LOG_TABLE_NAME].ref == "A4:F4"


def test_activity_log_requires_openpyxl_workbook() -> None:
    """Verify invalid input is rejected."""
    try:
        build_activity_log(None)
    except TypeError:
        pass
    else:
        raise AssertionError("Expected TypeError was not raised.")
