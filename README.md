---

# Restaurant Live Table Order & Billing System

## Overview

This project is a **Restaurant Dine-In Order & Billing System** built using **Django**.
It provides **real-time visibility of table status**, **order lifecycle management**, **billing workflow**, and **role-based access control** for restaurant staff.

The system enforces **correct business workflows** (orders → served → billing → payment → table reset) and prevents invalid operations.

---

## Tech Stack

* **Backend**: Django, Django REST Framework
* **Frontend**: Django Templates (HTML)
* **Auth & RBAC**: Django Auth + Groups
* **Database**: SQLite (default, easily replaceable)
* **Notifications**: Django Signals
* **Architecture**: Service-layer driven (business logic isolated)

---

## Roles & Permissions

| Role    | Permissions                               |
| ------- | ----------------------------------------- |
| Waiter  | Place orders, mark orders as served       |
| Cashier | Generate bills, mark bills as paid        |
| Manager | View live dashboard, manage tables & menu |
| System  | Enforces state transitions automatically  |

RBAC is enforced at **both API and UI level**.

---

## Core Features

### 1. Table Management

* Tables have capacity and status
* Status lifecycle:

```
AVAILABLE → OCCUPIED → BILL_REQUESTED → AVAILABLE
```

### 2. Menu & Orders

* Menu categories: Starter, Main, Drinks, Dessert
* Orders can contain multiple items with quantities
* Order lifecycle:

```
PLACED → IN_KITCHEN → SERVED
```

* Table automatically becomes **Occupied** on first order

### 3. Billing

* Bills generated only after orders are **Served**
* Tax calculation applied
* Bill lifecycle:

```
PENDING_PAYMENT → PAID
```

* Table resets to **Available** after payment
## Test Login Credentials

These credentials are provided for evaluation and testing purposes only.

Waiter
Username: waiter1 
Password: kesavan2002 

Cashier
Username: cashier1 
Password: kesavan2002 

Manager
Username: manager1 
Password: kesavan2002 

Admin (Django Admin)
Username: kesav 
Password: kesavan2002 

### 4. Dashboard

* Live table status
* Active orders per table
* Bill status & totals
* Read-only aggregation layer

### 5. Notifications

* Kitchen notification triggered using **Django Signals** when a new order is placed

---

## Project Structure

```
restaurant/
├── accounts/        # Roles & permissions
├── tables/          # Table management
├── menu/            # Menu items
├── orders/          # Orders & order items
├── billing/         # Billing & payments
├── notifications/   # Signals
├── dashboard/       # Aggregated APIs
├── frontend/        # HTML views
├── templates/       # Shared templates
├── manage.py
```

Business logic is isolated in **service layers**, not views.

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/kesavan46/Restaurant-Live-Table-Order-Billing-System.git
cd restaurant
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install django djangorestframework
```

### 4. Migrate Database

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser

```bash
python manage.py createsuperuser
```

### 6. Run Server

```bash
python manage.py runserver
```

---

## Initial Data Setup (IMPORTANT)

### Create Groups

Admin → Groups:

* Waiter
* Cashier
* Manager

### Create Users

Assign users to correct groups.

### Create Tables & Menu

Use Django Admin to add:

* Tables (capacity, number)
* Menu items (category, price)

---

## Application URLs

| URL           | Description          |
| ------------- | -------------------- |
| `/login/`     | Login                |
| `/dashboard/` | Manager dashboard    |
| `/order/`     | Place order (Waiter) |
| `/billing/`   | Billing (Cashier)    |
| `/logout/`    | Logout               |
| `/admin/`     | Admin panel          |

---

## End-to-End Workflow (Demo Script)

1. **Manager**

   * Logs in
   * Views live table dashboard

2. **Waiter**

   * Places order → table becomes OCCUPIED
   * Marks order as SERVED

3. **Cashier**

   * Generates bill
   * Marks bill as PAID

4. **System**

   * Table resets to AVAILABLE

---

## Validation & Error Handling

* Cannot bill without served orders
* Cannot pay bill twice
* Role-restricted pages (403 Forbidden)
* State transitions strictly enforced

---

## Assumptions

* Single restaurant
* Single active bill per table session
* Payments simulated (no gateway)
* UI kept minimal for clarity

---

## Bonus Considerations

* APIs already structured for future React frontend
* Signals easily replaceable with Celery / WebSockets
* Docker & PDF export can be added without refactor

---

## Submission Checklist (DO THIS BEFORE SUBMITTING)

✅ All migrations committed
✅ README included
✅ Demo users documented
✅ No hardcoded credentials
✅ Server runs without errors
✅ Admin panel usable
✅ Full workflow tested

---

## Final Note

This project prioritizes **workflow correctness, clean architecture, and clarity** over unnecessary complexity—matching real-world backend engineering expectations.
