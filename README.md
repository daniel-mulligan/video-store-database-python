# video-store-database-python

# 🎬 Video Store Management System (Python + MySQL)

This project simulates a video rental system using Python and a MySQL database. The system supports both TCP client-server interaction and direct MySQL connector-based database access. It handles customer registration, movie registration, rentals, returns, and manages the backend data efficiently with modular Python classes.

---

## 📂 Project Overview

- **Backend**: Python 3.x
- **Database**: MySQL (v9.1.0) with MySQL Workbench (v8.0.41)
- **Server**: TCP-based connection with MySQL DB
- **Editor**: Visual Studio Code
- **OS Tested On**: Windows 11

---

## 🧠 Features

- Customer registration with phone verification
- Video registration with automated ID/versioning
- Movie hiring and returning functionality
- Modular code structure with clear separation of concerns
- TCP server for centralized DB interaction
- Robust error handling for server-client issues

---

## 🛠️ Setup Instructions

See [`docs/setup-instructions.md`](docs/setup-instructions.md)

---

## ▶️ How to Use

1. Run `server.py` in one terminal
2. In another terminal, run `main.py`
3. Follow the prompts to:
   - Create or reuse a database
   - Register customers and videos
   - Hire or return movies

Detailed step-by-step guide here: [`docs/usage-guide.md`](docs/usage-guide.md)

---

## ⚙️ Architecture

All components are separated into classes/modules for clarity:

- **Customer Management**
- **Video Inventory**
- **Hiring and Returns**
- **Database Connection**
- **Clear UI in Terminal**

For full flow explanation: [`docs/architecture.md`](docs/architecture.md)

---

## 🧯 Troubleshooting

### Server Error:
Should you encounter the following error:
Error connecting to server: [WinError 10061] No connection could be made
because the target machine actively refused it
It is because the server.py file was not running before the main.py file was executed or it
was not run on a separate terminal.
Alternatively you may have entered an invalid port number in the setup of your server.py
file.

#### To fix this:
Please ensure you are running server.py on a separate terminal before running main.py and
that the port entered into the server.py file is valid.

### Database Error:
Should you encounter the following error:
“Incorrect username or password!”
When running your server after setup, this indicates that incorrect login details were added
to the database.py file during setup.

#### To fix this:
Please ensure you have entered the correct login information for the MySQL connection
you are intending to create the database on.
