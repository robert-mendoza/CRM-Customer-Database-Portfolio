# CRM Customer Database Portfolio

A production-quality Python/OpenPyXL project that builds a structured customer data management workbook for CRM workflows.

## Current production scope

The validated workbook builder is frozen at Part 4L and produces:

1. `01_Cover`
2. `04_Validation_Lists`
3. `03_Customer_Database`
4. `02_Dashboard`
5. `05_Data_Quality_Report`
6. `06_Activity_Log`
7. `07_Instructions`

Part 4M is intentionally not implemented because no authoritative requirement exists for it.

## Project structure

```text
CRM-Customer-Database-Portfolio/
├── builder/
├── output/
├── tests/
├── requirements.txt
├── .gitignore
└── README.md
```

## Requirements

- Python 3.12 recommended
- `openpyxl`
- `pytest`

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

## Build the workbook

From the repository root:

```powershell
python -c "from pathlib import Path; from builder.workbook_builder import build_workbook; print(build_workbook(Path('output/Customer_Data_Management_Workbook.xlsx')))"
```

## Run tests

```powershell
python -m pytest -q
```

## Validation baseline

The production validation covers workbook generation, worksheet integration, tables, data validations, defined names, dashboard formulas, data quality formulas, Activity Log structure, and the Instructions worksheet.

## Project boundary

The legacy CRM Dataset Build / Merge Engine is a separate project and is not part of this workbook-builder release. Legacy `loader.py`, `merge_engine`, and abandoned Part 4M artifacts must not be copied into this repository.

## Release status

Current workbook-builder scope: **4L frozen**

Part 4M: **not implemented**

Define a new requirement before starting any future module.
