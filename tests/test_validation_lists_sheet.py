"""Functional tests for the validation lists worksheet."""

from openpyxl import Workbook

from builder.validation_lists import (
    CUSTOMER_STATUSES,
    CUSTOMER_TYPES,
    INDUSTRIES,
    LEAD_SOURCES,
    PRIORITIES,
)
from builder.validation_lists_sheet import build_validation_lists


def main() -> None:
    """Validate the generated validation lists worksheet."""
    workbook = Workbook()
    worksheet = build_validation_lists(workbook)

    expected = {
        "A": ("Customer Statuses", *CUSTOMER_STATUSES),
        "B": ("Customer Types", *CUSTOMER_TYPES),
        "C": ("Industries", *INDUSTRIES),
        "D": ("Lead Sources", *LEAD_SOURCES),
        "E": ("Priorities", *PRIORITIES),
    }

    for column, values in expected.items():
        actual = tuple(
            worksheet[f"{column}{row}"].value
            for row in range(1, len(values) + 1)
        )

        if actual != values:
            raise AssertionError(
                f"{column} validation list does not match."
            )

    print("Worksheet:", worksheet.title)
    print("Columns validated:", len(expected))
    print("Validation list values verified")
    print("Part 4A functional test passed")


if __name__ == "__main__":
    main()