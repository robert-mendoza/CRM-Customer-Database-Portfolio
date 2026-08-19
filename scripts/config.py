"""
CRM Customer Database Portfolio
Project Configuration

This module contains all global configuration values used throughout
the CRM Customer Database Portfolio project.
"""

from pathlib import Path

# =============================================================================
# Project Information
# =============================================================================

PROJECT_NAME = "CRM Customer Database Portfolio"

PROJECT_VERSION = "1.0.0"

PROJECT_AUTHOR = "Robert Mendoza"

PROJECT_LICENSE = "MIT"

# =============================================================================
# Project Paths
# =============================================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

OUTPUT_FOLDER = PROJECT_ROOT / "workbook"

WORKBOOK_FILENAME = (
    f"CRM_Customer_Database_Portfolio_v{PROJECT_VERSION}.xlsx"
)

OUTPUT_FILE = OUTPUT_FOLDER / WORKBOOK_FILENAME

# =============================================================================
# Workbook Settings
# =============================================================================

WORKBOOK_TITLE = PROJECT_NAME

DEFAULT_CUSTOMER_COUNT = 100

TABLE_NAME = "tblCustomers"

# =============================================================================
# Worksheet Names
# =============================================================================

CUSTOMERS_SHEET = "Customers"

DASHBOARD_SHEET = "Sales Dashboard"

VALIDATION_SHEET = "Data Validation"

PIVOT_SHEET = "Pivot Report"

# =============================================================================
# Customer Table Headers
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
    "Customer Status",
    "Lead Source",
    "Date Created",
    "Last Contact",
    "Next Follow-up",
    "Contract Value",
    "Payment Status",
    "Priority",
    "Preferred Contact",
    "Account Manager",
    "Notes",
]

# =============================================================================
# Excel Formatting
# =============================================================================

HEADER_BACKGROUND = "1F4E78"

HEADER_FONT = "FFFFFF"

TABLE_STYLE = "TableStyleMedium2"

FREEZE_PANE = "A2"

DATE_FORMAT = "yyyy-mm-dd"

CURRENCY_FORMAT = '$#,##0.00'

AUTO_FILTER = True

AUTO_FIT_COLUMNS = True

# =============================================================================
# Dashboard Settings
# =============================================================================

TOP_COUNTRIES = 10

TOP_INDUSTRIES = 10

TOP_ACCOUNT_MANAGERS = 10

# =============================================================================
# Localization
# =============================================================================

DEFAULT_LANGUAGE = "en-US"

DEFAULT_COUNTRY = "United States"

DEFAULT_CURRENCY = "USD"

# =============================================================================
# Customer Status
# =============================================================================

CUSTOMER_STATUS = [
    "Active",
    "Prospect",
    "Inactive",
]

# =============================================================================
# Priority
# =============================================================================

PRIORITY = [
    "High",
    "Medium",
    "Low",
]

# =============================================================================
# Payment Status
# =============================================================================

PAYMENT_STATUS = [
    "Paid",
    "Pending",
    "Overdue",
]

# =============================================================================
# Lead Source
# =============================================================================

LEAD_SOURCE = [
    "LinkedIn",
    "Website",
    "Referral",
    "Conference",
    "Cold Call",
    "Email Campaign",
]

# =============================================================================
# Preferred Contact
# =============================================================================

PREFERRED_CONTACT = [
    "Email",
    "Phone",
    "Microsoft Teams",
    "Zoom",
]

# =============================================================================
# Industries
# =============================================================================

INDUSTRIES = [
    "Software",
    "Finance",
    "Healthcare",
    "Retail",
    "Manufacturing",
    "Logistics",
    "Telecommunications",
    "Education",
]

# =============================================================================
# Countries
# =============================================================================

COUNTRIES = [
    "Australia",
    "Canada",
    "Germany",
    "Japan",
    "Philippines",
    "Singapore",
    "United Kingdom",
    "United States",
]

# =============================================================================
# Account Managers
# =============================================================================

ACCOUNT_MANAGERS = [
    "Robert Mendoza",
    "Anna Cruz",
    "David Lim",
    "Jennifer Lee",
    "John Reyes",
    "Maria Santos",
]

# =============================================================================
# Miscellaneous
# =============================================================================

MAX_NOTE_LENGTH = 150