"""
Customer Data Generator
CRM Customer Database Portfolio

Version: 1.2
"""

from __future__ import annotations

import random
from datetime import timedelta

from faker import Faker

from data.reference_data import (
    ACCOUNT_MANAGERS,
    CUSTOMER_STATUS,
    LEAD_SOURCES,
    PAYMENT_STATUS,
    PREFERRED_CONTACT,
    PRIORITY,
)
    PREFERRED_CONTACT,
    ACCOUNT_MANAGERS,
)

from data.companies import COMPANIES
from data.locations import LOCATIONS

fake = Faker("en_US")


# ==========================================================
# Helper Functions
# ==========================================================

def build_email(first_name: str, last_name: str, domain: str) -> str:
    """
    Generate a professional business email.
    Example:
        john.smith@northwindtech.com
    """
    first = first_name.lower().replace(" ", "")
    last = last_name.lower().replace(" ", "")

    return f"{first}.{last}@{domain}"


def generate_phone(country: str) -> str:
    """
    Generate a phone number using the country's dialing code.
    """

    country_info = LOCATIONS[country]
    code = country_info["code"]

    return (
        f"{code} "
        f"{random.randint(200,999)}-"
        f"{random.randint(100,999)}-"
        f"{random.randint(1000,9999)}"
    )


def generate_contract_value(industry: str) -> int:
    """
    Generate realistic contract values
    based on industry.
    """

    ranges = {

        "Software": (20000, 250000),

        "Finance": (30000, 500000),

        "Healthcare": (15000, 200000),

        "Manufacturing": (50000, 750000),

        "Retail": (10000, 150000),

        "Telecommunications": (25000, 400000),

        "Education": (5000, 80000),

        "Logistics": (20000, 350000),

        "Consulting": (15000, 300000),

    }

    minimum, maximum = ranges.get(
        industry,
        (10000, 100000),
    )

    return random.randint(minimum, maximum)


def generate_customer_status() -> str:
    """
    Weighted customer status.
    """

    return random.choices(
        CUSTOMER_STATUS,
        weights=[65, 20, 15],
        k=1,
    )[0]


def generate_payment_status(customer_status: str) -> str:
    """
    Generate payment status based on customer status.
    """

    if customer_status == "Active":

        return random.choices(
            ["Paid", "Pending", "Overdue"],
            weights=[75, 20, 5],
            k=1,
        )[0]

    if customer_status == "Prospect":

        return random.choices(
            ["Pending", "Paid"],
            weights=[90, 10],
            k=1,
        )[0]

    return random.choices(
        PAYMENT_STATUS,
        weights=[20, 20, 60],
        k=1,
    )[0]


def generate_dates(customer_status: str):

    if customer_status == "Active":

        created = fake.date_between(
            start_date="-3y",
            end_date="-6m",
        )

        last_contact = fake.date_between(
            start_date="-30d",
            end_date="today",
        )

    elif customer_status == "Prospect":

        created = fake.date_between(
            start_date="-12m",
            end_date="-30d",
        )

        last_contact = fake.date_between(
            start_date="-90d",
            end_date="today",
        )

    else:

        created = fake.date_between(
            start_date="-5y",
            end_date="-2y",
        )

        last_contact = fake.date_between(
            start_date="-365d",
            end_date="-180d",
        )

    next_follow_up = last_contact + timedelta(
        days=random.randint(7, 45)
    )

    return created, last_contact, next_follow_up


# ==========================================================
# Customer Generator
# ==========================================================

def generate_customer(customer_number: int) -> dict:

    company = random.choice(COMPANIES)

    country = random.choice(list(LOCATIONS.keys()))

    city = random.choice(
        LOCATIONS[country]["cities"]
    )

    first_name = fake.first_name()

    last_name = fake.last_name()

    email = build_email(
        first_name,
        last_name,
        company["domain"],
    )

    phone = generate_phone(country)

    customer_status = generate_customer_status()

    payment_status = generate_payment_status(
        customer_status
    )

    created_date, last_contact, next_follow_up = generate_dates(
        customer_status
    )

    contract_value = generate_contract_value(
        company["industry"]
    )

    return {

        "Customer ID":
            f"CUST-{customer_number:04d}",

        "First Name":
            first_name,

        "Last Name":
            last_name,

        "Company":
            company["name"],

        "Job Title":
            fake.job(),

        "Industry":
            company["industry"],

        "Email":
            email,

        "Phone":
            phone,

        "Country":
            country,

        "City":
            city,

        "Customer Status":
            customer_status,

        "Lead Source":
            random.choice(LEAD_SOURCE),

        "Account Manager":
            random.choice(ACCOUNT_MANAGERS),

        "Date Created":
            created_date,

        "Last Contact":
            last_contact,

        "Next Follow-up":
            next_follow_up,

        "Contract Value":
            contract_value,

        "Payment Status":
            payment_status,

        "Priority":
            random.choice(PRIORITY),

        "Preferred Contact":
            random.choice(PREFERRED_CONTACT),

        "Notes":
            fake.sentence(nb_words=10),

    }


# ==========================================================
# Dataset Generator
# ==========================================================

def generate_customers() -> list[dict]:
    """
    Generate all customer records.
    """

    return [
        generate_customer(customer_number)
        for customer_number in range(
            1,
            TOTAL_RECORDS + 1,
        )
    ]


# ==========================================================
# Test
# ==========================================================

if __name__ == "__main__":

    customers = generate_customers()

    print(
        f"\nGenerated {len(customers)} customer records.\n"
    )

    print(customers[0])