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

Error like:

```bash
Error connecting to server: [WinError 10061] No connection could be made
