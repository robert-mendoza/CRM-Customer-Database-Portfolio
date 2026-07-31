"""
Location Reference Data

CRM Customer Database Portfolio

Version: 1.2

Contains country, dialing code, currency, timezone,
and major cities used by the customer generator.
"""

LOCATIONS = {

    "United States": {
        "code": "+1",
        "currency": "USD",
        "timezone": "America/New_York",
        "cities": [
            "New York",
            "Los Angeles",
            "Chicago",
            "Houston",
            "Phoenix",
            "Seattle",
            "San Francisco",
            "Boston",
            "Dallas",
            "Austin"
        ]
    },

    "Canada": {
        "code": "+1",
        "currency": "CAD",
        "timezone": "America/Toronto",
        "cities": [
            "Toronto",
            "Vancouver",
            "Montreal",
            "Ottawa",
            "Calgary",
            "Edmonton",
            "Winnipeg"
        ]
    },

    "United Kingdom": {
        "code": "+44",
        "currency": "GBP",
        "timezone": "Europe/London",
        "cities": [
            "London",
            "Manchester",
            "Liverpool",
            "Birmingham",
            "Leeds",
            "Glasgow",
            "Edinburgh"
        ]
    },

    "Australia": {
        "code": "+61",
        "currency": "AUD",
        "timezone": "Australia/Sydney",
        "cities": [
            "Sydney",
            "Melbourne",
            "Brisbane",
            "Perth",
            "Adelaide",
            "Canberra"
        ]
    },

    "Singapore": {
        "code": "+65",
        "currency": "SGD",
        "timezone": "Asia/Singapore",
        "cities": [
            "Singapore"
        ]
    },

    "Philippines": {
        "code": "+63",
        "currency": "PHP",
        "timezone": "Asia/Manila",
        "cities": [
            "Makati",
            "Taguig",
            "Pasig",
            "Quezon City",
            "Mandaluyong",
            "Cebu City",
            "Davao City",
            "Baguio",
            "Iloilo City",
            "Bacolod"
        ]
    },

    "Germany": {
        "code": "+49",
        "currency": "EUR",
        "timezone": "Europe/Berlin",
        "cities": [
            "Berlin",
            "Munich",
            "Hamburg",
            "Frankfurt",
            "Cologne",
            "Stuttgart",
            "Düsseldorf"
        ]
    },

    "Japan": {
        "code": "+81",
        "currency": "JPY",
        "timezone": "Asia/Tokyo",
        "cities": [
            "Tokyo",
            "Osaka",
            "Nagoya",
            "Yokohama",
            "Kyoto",
            "Sapporo",
            "Fukuoka"
        ]
    },

    "Netherlands": {
        "code": "+31",
        "currency": "EUR",
        "timezone": "Europe/Amsterdam",
        "cities": [
            "Amsterdam",
            "Rotterdam",
            "The Hague",
            "Utrecht",
            "Eindhoven"
        ]
    },

    "New Zealand": {
        "code": "+64",
        "currency": "NZD",
        "timezone": "Pacific/Auckland",
        "cities": [
            "Auckland",
            "Wellington",
            "Christchurch",
            "Hamilton",
            "Tauranga"
        ]
    }

}