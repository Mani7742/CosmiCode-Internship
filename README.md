# CosmiCode-Internship
Inventory Management System - Documentation
1. Introduction
The Inventory Management System is a desktop application built using Python, SQLite, and Tkinter. It allows users to manage products, sales, and stock efficiently. The application is suitable for small businesses that need a simple and lightweight solution for tracking inventory.
2. Features
•	Product Management: Add, view, and delete products.
•	Sales Management: Record sales transactions and automatically reduce stock levels.
•	Stock Control: View current stock and prevent overselling.
•	Database: SQLite database is used to store product and sales data.
3. Technology Stack
The system is developed using the following technologies:
•	Python 3
•	Tkinter (for GUI)
•	SQLite (for database)
4. Database Schema
The application uses three main tables:
•	Table: products
•	id - Primary Key
•	code - Unique product code
•	name - Product name
•	category - Product category
•	cost - Purchase cost
•	price - Selling price
•	stock - Current stock quantity
•	supplier - Supplier name
•	Table: sales
•	id - Primary Key
•	invoice_no - Unique invoice number
•	sale_date - Date of sale
•	total_amount - Total sale amount
•	paid_amount - Amount paid
•	cashier - Name of cashier
•	Table: sale_items
•	id - Primary Key
•	sale_id - References sales table
•	product_id - References products table
•	quantity - Quantity sold
•	selling_price - Selling price per item
•	subtotal - Total for this item line
5. Application Workflow
1.	User opens the application.
2.	Database initializes if not already created.
3.	User can add new products with details like code, name, category, cost, price, and stock.
4.	Products are displayed in a table.
5.	User can create a sale by selecting product ID and quantity.
6.	Stock is automatically reduced when a sale is made.
7.	Sales are recorded with invoice number and details.
6. User Interface
The interface contains the following elements:
- Buttons: Add Product, Make Sale, Refresh.
- Table: Displays product details (ID, Code, Name, Price, Stock).
- Dialogs: Add Product Form, Sale Entry Dialog.
7. Code Structure
The code is written in a single file with two main sections:
1. Database Layer: Handles SQLite database operations.
2. Tkinter UI Layer: Provides the graphical user interface for interaction.
8. Future Improvements
•	Add product editing functionality.
•	Generate PDF/Excel reports for sales and stock.
•	Implement user authentication and roles.
•	Support barcode scanning for faster sales entry.
•	Cloud database support for multi-user access.
