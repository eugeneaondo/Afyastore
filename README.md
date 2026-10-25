# Afyastore

A Django back-office application for running a small store: managing customers, products, orders and payments from one place.

![Python](https://img.shields.io/badge/Python-0d1117?style=flat-square&logo=python&logoColor=3776AB)
![Django](https://img.shields.io/badge/Django-4.2-0d1117?style=flat-square&logo=django&logoColor=44B78B)
![SQLite](https://img.shields.io/badge/SQLite-0d1117?style=flat-square&logo=sqlite&logoColor=8B949E)

---

## Modules

The project is split into three Django apps, each owning one part of the business:

| App | Responsibility |
|---|---|
| `customers` | Customer records with unique email and contact details |
| `ordermanagement` | Product catalogue, orders, and order line items |
| `payments` | Payments with transaction references, amounts and configurable payment modes |

## Data model

```mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ ORDER_ITEM : contains
    PRODUCT ||--o{ ORDER_ITEM : "appears in"
    PAYMENT_MODE ||--o{ PAYMENT : "used by"

    CUSTOMER { string first_name string last_name string email string phone_number }
    PRODUCT { string name text description decimal price }
    ORDER { date order_date decimal total_amount }
    ORDER_ITEM { int quantity }
    PAYMENT_MODE { string mode string description }
    PAYMENT { string transaction_ref decimal amount string paid_by datetime trans_date }
```

Orders and products are linked through an explicit `OrderItem` model, so each line item carries its own quantity.

## Routes

| Path | Description |
|---|---|
| `/admin/` | Django admin for all models |
| `/customers/` | Customer list |
| `/ordermgmt/products/` | Product catalogue and product detail pages |
| `/ordermgmt/orders/` | Orders and order detail pages |
| `/payments/add_payment/` | Record a payment |
| `/payments/all/` | All payments |
| `/payments/<id>/` | Payment detail |

## Getting started

```bash
git clone https://github.com/eugeneaondo/Afyastore.git
cd Afyastore

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install "django>=4.2,<5"

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/admin/` and sign in with the superuser you created.

## Roadmap

- [ ] Link payments directly to orders
- [ ] Order totals calculated from line items
- [ ] Stock tracking on products
- [ ] Mobile money payment integration
- [ ] Move configuration and secrets to environment variables
