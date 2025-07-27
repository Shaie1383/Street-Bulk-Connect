from datetime import datetime, timedelta

USERS = {
    "vendor1": {"role": "vendor", "name": "Ravi Chaat"},
    "vendor2": {"role": "vendor", "name": "Shaista Snacks"},
    "vendor3": {"role": "vendor", "name": "Tikki Tandoor"},
    "supplier1": {"role": "supplier", "name": "FreshVeg Distributors"},
    "supplier2": {"role": "supplier", "name": "Masala Mart"},
}

GROUP_ORDERS = [
    {
        "id": 1,
        "product": "Onions",
        "min_qty": 100,
        "price_per_unit": 10,
        "expiry": datetime.now() + timedelta(minutes=30),
        "committed": 60,
        "supplier": "supplier1",
        "participants": {"vendor1": 20, "vendor2": 40},
    },
    {
        "id": 2,
        "product": "Tomatoes",
        "min_qty": 80,
        "price_per_unit": 12,
        "expiry": datetime.now() + timedelta(minutes=15),
        "committed": 50,
        "supplier": "supplier1",
        "participants": {"vendor3": 50},
    },
    {
        "id": 3,
        "product": "Chaat Masala (1kg packs)",
        "min_qty": 20,
        "price_per_unit": 150,
        "expiry": datetime.now() + timedelta(minutes=60),
        "committed": 5,
        "supplier": "supplier2",
        "participants": {"vendor2": 10},
    },
]
