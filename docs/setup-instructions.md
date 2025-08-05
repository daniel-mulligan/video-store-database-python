# 🛠️ Setup Instructions

This guide explains how to install and configure the Video Store Management System on your local machine.

---

## 📦 Prerequisites

Before installing the application, ensure you have the following installed:

- **Python 3.x**
- **MySQL Server** (recommended version: 9.1.0)
- **MySQL Workbench** (recommended version: 8.0.41)
- **MySQL Connector for Python** (recommended version: 8.0.33)
- **Code Editor or IDE** (e.g., Visual Studio Code)

---

## 📁 Folder Structure

All Python files must be kept inside the `video_store/` directory.  
The server and client programs work together, so file placement and consistency is crucial.

---

## ⚙️ Configuration Steps

### 1. Configure `server.py`

Open `server.py` and:

- On **line 85**, enter a valid **port number** (e.g., `65432`) for your server to listen on.

### 2. Configure `database.py`

Open `database.py` and:

- On **lines 17–19** and **35–37**, insert your **MySQL login credentials**:
  - `host`
  - `user`
  - `password`
  - `database`

> ⚠️ Make sure the database name matches the one your script will create (`video_store`).

### 3. Configure `video_manager.py`

Open `video_manager.py` and:

- On **line 62**, enter the **same port number** used in `server.py` to ensure consistent TCP communication.

---

## 🔄 Installing MySQL and SSMS (If Not Installed)

You can install SQL Server and SQL Server Management Studio by following this link:

[SQL Server Developer Edition Installer](https://go.microsoft.com/fwlink/p/?linkid=2215158&clcid=0x409&culture=en-us&country=us)

Follow these steps:

1. Download and run `SQL2022-SSEI-Dev.exe`.
2. Select the **Basic** installation type.
3. Accept the License Agreement.
4. Choose an install location and proceed.
5. After installation, install **SSMS** via the provided prompt.
6. Run `SSMS-Setup-ENU.exe` and follow the instructions.

---

## ✅ Running the Program

### 1. Start the Server

Open a terminal and run:

```bash
python server.py
2. Run the Client
In a separate terminal, run:

bash
Copy
Edit
python main.py
3. Follow Terminal Prompts
Create the database: type Y

Proceed to main menu: type M

Select from the available options (register customer, register movie, hire/return movie, exit)
