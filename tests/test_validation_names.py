"""Functional tests for workbook validation defined names."""

from openpyxl import Workbook

from builder.validation_lists_sheet import build_validation_lists
from builder.validation_names import (
    VALIDATION_DEFINED_NAMES,
    build_validation_defined_names,
)


def main() -> None:
    """Validate workbook defined names."""
    workbook = Workbook()
    workbook.remove(workbook.active)

    build_validation_lists(workbook)
    build_validation_defined_names(workbook)

    for name, expected_reference in VALIDATION_DEFINED_NAMES:
        defined_name = workbook.defined_names[name]

        if defined_name.attr_text != expected_reference:
            raise AssertionError(
                f"{name}: unexpected reference "
                f"{defined_name.attr_text!r}"
            )

        print(
            f"{name}: {defined_name.attr_text}"
        )

    print("Defined names:", len(VALIDATION_DEFINED_NAMES))
    print("Part 4C functional test passed")


if __name__ == "__main__":
    main()