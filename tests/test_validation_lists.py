"""Tests for CRM workbook validation lists."""

from builder.validation_lists import (
    CUSTOMER_STATUSES,
    CUSTOMER_TYPES,
    INDUSTRIES,
    LEAD_SOURCES,
    PRIORITIES,
)


def main() -> None:
    """Validate the configured workbook values."""
    assert CUSTOMER_STATUSES == (
        "Active",
        "Inactive",
        "Prospect",
    )

    assert CUSTOMER_TYPES == (
        "Individual",
        "Small Business",
        "Medium Business",
        "Enterprise",
    )

    assert LEAD_SOURCES == (
        "Website",
        "Email",
        "Phone",
        "Referral",
        "Social Media",
        "Other",
    )

    assert PRIORITIES == (
        "Low",
        "Medium",
        "High",
        "Urgent",
    )

    assert INDUSTRIES == (
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

    validation_groups = (
        CUSTOMER_STATUSES,
        CUSTOMER_TYPES,
        LEAD_SOURCES,
        PRIORITIES,
        INDUSTRIES,
    )

    for values in validation_groups:
        assert values
        assert all(isinstance(value, str) for value in values)
        assert len(values) == len(set(values))

    print("validation_lists.py functional test passed.")


if __name__ == "__main__":
    main()
