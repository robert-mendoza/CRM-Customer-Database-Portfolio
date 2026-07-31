"""
Project Configuration
CRM Customer Database Portfolio

This module contains all project configuration values.
"""

from pathlib import Path

# =============================================================================
# Project Paths
# =============================================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

OUTPUT_FOLDER = PROJECT_ROOT / "workbook"

OUTPUT_FILE = OUTPUT_FOLDER / "CRM_Customer_Database_Portfolio_v1.1.xlsx"

# =============================================================================
# Workbook Settings
# =============================================================================

WORKBOOK_TITLE = "CRM Customer Database Portfolio"

WORKSHEET_NAME = "Customers"

TABLE_NAME = "tblCustomers"

TOTAL_RECORDS = 100

# =============================================================================
# Header Names
# =============================================================================

HEADERS = [
    "Customer ID",
    "First Name",
    "Last Name",
    "Company",
    "Job Title",
    "Industry",
    "Email",
    "Phone",
    "Country",
    "City",
        "Date Created",
    "Last Contact",
    "Next Follow-up",
    "Contract Value",
    "Payment Status",
    "Priority",
    "Preferred Contact",
    "Notes"
]

# =============================================================================
# Excel Formatting
# =============================================================================

HEADER_BACKGROUND = "1F4E78"

HEADER_FONT = "FFFFFF"

TABLE_STYLE = "TableStyleMedium2"

DATE_FORMAT = "yyyy-mm-dd"

CURRENCY_FORMAT = '$#,##0.00'

FREEZE_PANE = "A2"

# =============================================================================
# Lists
# =============================================================================

CUSTOMER_STATUS = [
    "Active",
    "Prospect",
    "Inactive"
]

PRIORITY = [
    "High",
    "Medium",
    "Low"
]

PAYMENT_STATUS = [
    "Paid",
    "Pending",
    "Overdue"
]

LEAD_SOURCE = [
    "LinkedIn",
    "Website",
    "Referral",
    "Conference",
    "Cold Call",
    "Email Campaign"
]

PREFERRED_CONTACT = [
    "Email",
    "Phone",
    "Microsoft Teams",
    "Zoom"
]

INDUSTRIES = [
    "Software",
    "Finance",
    "Healthcare",
    "Retail",
    "Manufacturing",
    "Logistics",
    "Telecommunications",
    "Education"
]

COUNTRIES = [
    "United States",
    "Canada",
    "Australia",
    "United Kingdom",
    "Singapore",
    "Philippines",
    "Germany",
    "Japan"
]

ACCOUNT_MANAGERS = [
    "Robert Mendoza",
    "Anna Cruz",
    "John Reyes",
    "Maria Santos",
    "David Lim",
    "Jennifer Lee"
]