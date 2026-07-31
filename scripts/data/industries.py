"""
Industry Reference Data

CRM Customer Database Portfolio

Version: 1.2
"""

INDUSTRIES = {

    "Software": {

        "contract_min": 20000,
        "contract_max": 250000,

        "sales_cycle_days": 45,

        "renewal_months": 12,

        "customer_type": "B2B",

        "job_titles": [
            "Software Engineer",
            "Senior Software Engineer",
            "Technical Lead",
            "DevOps Engineer",
            "Cloud Engineer",
            "Solutions Architect",
            "IT Manager",
            "Product Manager",
            "Engineering Manager",
            "Chief Technology Officer"
        ]
    },

    "Finance": {

        "contract_min": 30000,
        "contract_max": 500000,

        "sales_cycle_days": 90,

        "renewal_months": 24,

        "customer_type": "Enterprise",

        "job_titles": [
            "Financial Analyst",
            "Finance Manager",
            "Investment Manager",
            "Risk Analyst",
            "Compliance Officer",
            "Chief Financial Officer",
            "Treasury Manager",
            "Accounting Manager"
        ]
    },

    "Healthcare": {

        "contract_min": 15000,
        "contract_max": 200000,

        "sales_cycle_days": 75,

        "renewal_months": 12,

        "customer_type": "Healthcare",

        "job_titles": [
            "Hospital Administrator",
            "Clinical Manager",
            "Medical Director",
            "Healthcare Consultant",
            "Operations Manager",
            "IT Manager",
            "Procurement Officer"
        ]
    },

    "Manufacturing": {

        "contract_min": 50000,
        "contract_max": 750000,

        "sales_cycle_days": 120,

        "renewal_months": 36,

        "customer_type": "Industrial",

        "job_titles": [
            "Plant Manager",
            "Production Manager",
            "Operations Director",
            "Manufacturing Engineer",
            "Supply Chain Manager",
            "Quality Manager",
            "Procurement Manager"
        ]
    },

    "Retail": {

        "contract_min": 10000,
        "contract_max": 150000,

        "sales_cycle_days": 30,

        "renewal_months": 12,

        "customer_type": "Retail",

        "job_titles": [
            "Store Manager",
            "Retail Director",
            "Merchandising Manager",
            "Sales Manager",
            "Operations Manager",
            "Branch Manager"
        ]
    },

    "Logistics": {

        "contract_min": 20000,
        "contract_max": 350000,

        "sales_cycle_days": 60,

        "renewal_months": 24,

        "customer_type": "Logistics",

        "job_titles": [
            "Logistics Manager",
            "Warehouse Manager",
            "Distribution Manager",
            "Fleet Manager",
            "Operations Supervisor",
            "Supply Chain Director"
        ]
    },

    "Telecommunications": {

        "contract_min": 25000,
        "contract_max": 400000,

        "sales_cycle_days": 90,

        "renewal_months": 24,

        "customer_type": "Enterprise",

        "job_titles": [
            "Network Engineer",
            "Telecommunications Manager",
            "Infrastructure Manager",
            "Solutions Consultant",
            "Regional Manager"
        ]
    },

    "Education": {

        "contract_min": 5000,
        "contract_max": 80000,

        "sales_cycle_days": 60,

        "renewal_months": 12,

        "customer_type": "Education",

        "job_titles": [
            "School Director",
            "Registrar",
            "Academic Coordinator",
            "IT Administrator",
            "Dean",
            "Principal"
        ]
    },

    "Consulting": {

        "contract_min": 15000,
        "contract_max": 300000,

        "sales_cycle_days": 45,

        "renewal_months": 12,

        "customer_type": "Professional Services",

        "job_titles": [
            "Business Consultant",
            "Senior Consultant",
            "Managing Consultant",
            "Engagement Manager",
            "Project Manager",
            "Director"
        ]
    }

}