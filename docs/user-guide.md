# 🎮 User Guide

Welcome to the **Video Store Management System**. This guide will help you interact with the program once it's been properly installed and configured.

---

## 🚀 Launching the Application

Before you begin:

1. Ensure that `server.py` is running in one terminal.
2. Open a second terminal and run:

```bash
python main.py
```

You will now be guided through a series of menus and options.

## 🧭 Menu Navigation
Once main.py is running, you’ll be presented with a Start Menu offering several options.

### 🔹 Option 1: Register a Customer
From the menu, type 1 and press Enter.

You’ll be asked to enter a phone number.

If the phone number already exists, the system will notify you.

If it's new, you’ll be prompted to enter:

* First Name

* Last Name

* Address

After successful registration, type M to return to the main menu.

### 🔹 Option 2: Register a Movie
From the menu, type 2 and press Enter.

You’ll be prompted to enter:

* Video Name

* Video Type (e.g., Action, Comedy)

Once completed, type M to return to the main menu.

### 🔹 Option 3: Hire Out a Movie
From the menu, type 3 and press Enter.

You will need to input:

* Video ID – must already exist

* Video Version – such as a specific release or format

* Customer ID – must be a registered customer

If incorrect details are entered, you will be prompted again.

Type M to return to the main menu.

### 🔹 Option 4: Return a Movie
From the menu, type 4 and press Enter.

You’ll be asked for:

* Video ID

* Video Version

After logging the return, type M to go back to the main menu.

### ❌ Option X: Exit the Application
Type x or X to exit the program safely.

Both the server and client programs will terminate.

## 🔄 General Tips
* Use the MySQL Workbench in the background to verify live data changes in the database.

* Refer to table names such as customers, videos, hires, and returns to find valid IDs and verify data integrity.

* The application will clear the screen between actions for a cleaner user experience.

* You can always return to the main menu by typing M when prompted.

## 💬 Still Stuck?
If you run into unexpected behavior, refer to the [Setup Instructions](docs/setup-instructions.md). for help.
