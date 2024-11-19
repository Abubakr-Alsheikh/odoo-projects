# Odoo Exercises - Ebtech Odoo Developer Free Training

This repository contains solutions to exercises from the Ebtech "Odoo Developer Free Training" program.

## Exercise 1: Course Management Module

This module implements a course management system with courses and sessions.

### Features:

* **Course Model:**
    * Fields: From Date, To Date, State (computed), Sessions (one-to-many).
    * Validations: Ensures To Date is not before From Date.
    * Computed Field: Calculates the course state (Draft, In Process, Done) based on session completion.
* **Session Model:**
    * Fields: From Date, To Date, Is Done, Is Expired (computed).
    * Validations: Ensures To Date is not before From Date and that session dates are within the course date range.
    * Computed Field: Determines if a session is expired based on the To Date.
* **User Interface:**
    * Form, tree, and search views for both models.
    * Buttons on the course form to manage state transitions.

## Exercise 2: Sale Coupon Wizard and Coupon Model

This module implements a wizard to generate sale coupons based on customer and sale order criteria.

### Features:

* **Coupon Model:**
    * Fields: Product, Customer, Percentage.
* **Wizard:**
    * Fields: Customer, From Date, To Date, Sale Orders (many-to-many), Default Product.
    * Functionality:
        * Fetches sale orders based on the selected customer and date range.
        * Creates a coupon with a default product, the selected customer, and a 50% percentage if more than 5 sale orders are found.
* **User Interface:**
    * Form view for the coupon model.
    * Form view for the wizard with buttons to fetch sale orders and generate coupons.
    * Menu items for easy access.



## Setup

1. **Dockerized Setup (Recommended):**  This project uses Docker and Docker Compose for easy setup. Refer to the `docker-compose.yml` file for details. Use `docker-compose up --build` to build and start the containers.

2. **Manual Setup:** If you're not using Docker, you'll need to:
    *   Install Odoo (version 17 or later recommended).
    *   Create a new database.
    *   Place the `course_management` and `sale_coupon_wizard` modules in your Odoo addons directory.
    *   Install the modules through the Odoo Apps menu.



## Usage

*   Course Management: Access the "Courses" and "Sessions" menu items under the "Courses" top-level menu.
*   Sale Coupon: Access the "Generate Coupon" wizard from the "Sales" menu.

## Acknowledgements

*   Ebtech "Odoo Developer Free Training" program.