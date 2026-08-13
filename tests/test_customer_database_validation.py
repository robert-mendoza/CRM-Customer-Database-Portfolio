"""Functional tests for customer database data validation."""

from openpyxl import Workbook

from builder.customer_database import build_customer_database


EXPECTED_RANGES = {
    "F5:F1004",
    "G5:G1004",
    "H5:H1004",
    "I5:I1004",
    "J5:J1004",
}


def main() -> None:
    """Validate customer database drop-down configuration."""
    workbook = Workbook()
    worksheet = build_customer_database(workbook)

    validations = list(worksheet.data_validations.dataValidation)

    print("Data validation count:", len(validations))

    if len(validations) != 5:
        raise AssertionError(
            f"Expected 5 validations, found {len(validations)}."
        )

    actual_ranges = {
        str(validation.sqref)
        for validation in validations
    }

    print("Validation ranges:", sorted(actual_ranges))

    if actual_ranges != EXPECTED_RANGES:
        raise AssertionError(
            "Validation ranges do not match the expected customer "
            "database columns."
        )

    for validation in validations:
        if validation.type != "list":
            raise AssertionError(
                f"Expected list validation, found {validation.type!r}."
            )

    print("Validation type: list")
    print("Part 3 functional test passed")


if __name__ == "__main__":
    main()