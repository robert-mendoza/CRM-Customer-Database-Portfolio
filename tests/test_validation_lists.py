"""Controlled values used by the CRM workbook.

This module contains the standard values used by Excel data-validation
drop-down lists in the customer database.

Project:
    CRM Customer Database Builder

Author:
    Robert Mendoza
"""

from __future__ import annotations


CUSTOMER_STATUSES: tuple[str, ...] = (
    "Active",
    "Inactive",
    "Prospect",
)

CUSTOMER_TYPES: tuple[str, ...] = (
    "Individual",
    "Small Business",
    "Medium Business",
    "Enterprise",
)

LEAD_SOURCES: tuple[str, ...] = (
    "Website",
    "Email",
    "Phone",
    "Referral",
    "Social Media",
    "Other",
)

PRIORITIES: tuple[str, ...] = (
    "Low",
    "Medium",
    "High",
    "Urgent",
)

INDUSTRIES: tuple[str, ...] = (
    "Education",
    "Finance",
    "Healthcare",
    "Information Technology",
    "Manufacturing",
    "Professional Services",
    "Retail",
    "Telecommunications",
    "Other",
)


__all__ = [
    "CUSTOMER_STATUSES",
    "CUSTOMER_TYPES",
    "INDUSTRIES",
    "LEAD_SOURCES",
    "PRIORITIES",
]