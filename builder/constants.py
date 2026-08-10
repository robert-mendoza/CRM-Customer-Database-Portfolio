"""
builder/constants.py

Global constants for the Customer Data Management Workbook Builder.

This module contains workbook-wide configuration values shared across
all worksheet builders. It intentionally contains no workbook logic
or formatting code.

Author: Robert Mendoza
Project: Customer Data Management Workbook Builder
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class WorkbookConfig:
    """Workbook information."""

    title: str = "Customer Data Management Workbook"
    company: str = "Veridata Business Solutions"
    version: str = "1.0"
    author: str = "Robert Mendoza"
    filename: str = "Customer_Data_Management_Workbook.xlsx"


@dataclass(frozen=True)
class SheetNames:
    """Worksheet names."""

    cover: str = "01_Cover"
    dashboard: str = "02_Dashboard"
    customer_database: str = "03_Customer_Database"
    validation_lists: str = "04_Validation_Lists"
    data_quality: str = "05_Data_Quality_Report"
    activity_log: str = "06_Activity_Log"
    instructions: str = "07_Instructions"
    config: str = "99_Config"


@dataclass(frozen=True)
class Layout:
    """Default workbook layout settings."""

    font_name: str = "Calibri"
    font_size: int = 11

    title_font_size: int = 18
    subtitle_font_size: int = 14

    header_row: int = 1
    default_row_height: int = 20
    default_column_width: int = 18

    worksheet_zoom: int = 100


@dataclass(frozen=True)
class Theme:
    """Workbook color palette."""

    primary_blue: str = "1F4E78"
    light_blue: str = "D9EAF7"

    green: str = "70AD47"
    red: str = "C00000"

    gray: str = "D9D9D9"

    white: str = "FFFFFF"
    black: str = "000000"


# ------------------------------------------------------------------
# Public configuration instances
# ------------------------------------------------------------------

WORKBOOK = WorkbookConfig()

SHEETS = SheetNames()

LAYOUT = Layout()

THEME = Theme()