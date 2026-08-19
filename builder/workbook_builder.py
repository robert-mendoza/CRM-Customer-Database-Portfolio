"""Production workbook orchestration for the CRM Customer Database Builder."""

from __future__ import annotations

from pathlib import Path

from openpyxl import Workbook

from builder.activity_log import build_activity_log
from builder.constants import WORKBOOK
from builder.cover import build_cover
from builder.customer_database import build_customer_database
from builder.data_quality import build_data_quality_report
from builder.dashboard import build_dashboard
from builder.instructions import build_instructions
from builder.validation_lists_sheet import build_validation_lists


def build_workbook(output_path: Path) -> Path:
    """Build and save the current CRM workbook."""
    if not isinstance(output_path, Path):
        raise TypeError("output_path must be a pathlib.Path instance.")
    if output_path.name == "":
        raise ValueError("output_path must include a filename.")

    output_path = output_path.resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    workbook = Workbook()
    workbook.remove(workbook.active)

    build_cover(workbook, WORKBOOK)
    build_validation_lists(workbook)
    build_customer_database(workbook)
    build_dashboard(workbook)
    build_data_quality_report(workbook)
    build_activity_log(workbook)
    build_instructions(workbook)

    workbook.save(output_path)
    return output_path


__all__ = ["build_workbook"]
