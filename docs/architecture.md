# 🏗️ System Architecture

This document outlines the high-level architecture of the **Video Store Management System**, including its components, flow of control, and integration between the server, client, and database layers.

---

## 📦 Project Structure

video_store/
│
├── server.py # Starts the TCP server and handles incoming client requests
├── main.py # Entry point for running the client application
├── start_menu.py # Handles user menu interface
│
├── customer_register.py # UI logic for registering customers
├── video_register.py # UI logic for registering videos
├── hire_out_video.py # UI logic for hiring out videos
├── return_video.py # UI logic for returning videos
│
├── customer_manager.py # Business logic for customer management
├── video_manager.py # Business logic for video management
├── hire_manager.py # Business logic for hiring videos
├── return_manager.py # Business logic for returning videos
│
├── database.py # Handles direct database connections
├── create_db.py # Functions to create the database and tables
├── clear_screen.py # Utility to clear the terminal screen

---

## 🔄 Program Flow

### Step 1: Server Initialization

- `server.py` is launched first in a dedicated terminal window.
- It listens for incoming client connections on a defined port using TCP.

### Step 2: Client Start

- `main.py` is run in a second terminal window.
- Prompts user to:
  - Create or reuse the database (`create_db.py`)
  - Proceed to the main menu (`start_menu.py`)

---

## 🧱 Application Layers

### 1. **Presentation Layer (UI)**
Responsible for interaction with the user via terminal prompts and inputs.
- Files: `start_menu.py`, `customer_register.py`, `video_register.py`, `hire_out_video.py`, `return_video.py`

### 2. **Logic Layer (Business Logic)**
Implements business rules and validations before database operations.
- Files: `customer_manager.py`, `video_manager.py`, `hire_manager.py`, `return_manager.py`

### 3. **Data Layer (Database Access)**
Handles all connections and operations related to the MySQL database.
- Files: `database.py`, `create_db.py`
- Communication is done both:
  - **Directly using MySQL Connector**
  - **Via TCP** to `server.py` for certain functions like fetching system time

---

## 📡 Communication

### TCP Socket Communication
- The `server.py` handles:
  - Time-based operations (e.g., logging current time)
  - Secure client requests
- The `video_manager.py` and `customer_register.py` communicate with the server through sockets.

### MySQL Database Connection
- Credentials are set in `database.py`
- All SQL interactions (inserts, queries, updates) use the MySQL Connector

---

## 🧠 Responsibilities by File

| File                | Responsibility                                 |
|---------------------|------------------------------------------------|
| `server.py`         | Listens on a socket, processes time requests   |
| `main.py`           | Orchestrates database setup and start menu     |
| `start_menu.py`     | CLI-based user interface                       |
| `customer_register.py` | Connects UI to customer logic               |
| `video_register.py` | Connects UI to video logic                     |
| `hire_out_video.py` | Handles hiring UI and logic                    |
| `return_video.py`   | Handles returns UI and logic                   |
| `customer_manager.py` | Performs CRUD on customers                   |
| `video_manager.py`  | Manages video creation and versioning          |
| `hire_manager.py`   | Manages hiring logic and validation            |
| `return_manager.py` | Manages return logic                           |
| `create_db.py`      | Builds the initial database                    |
| `database.py`       | Manages database connections                   |
| `clear_screen.py`   | Clears the terminal display                    |

---

## 🌐 Database Overview

The MySQL database `video_store` includes the following tables:

- `customers`
- `videos`
- `hires`

---

## 🔐 Security Considerations

- Currently basic terminal input; **future improvements** could include:
  - Encrypted connections between client and server
  - Authentication and user roles
  - Input validation/sanitization

---

## 📈 Scalability Notes

This modular design allows for:

- Adding a GUI front-end
- Scaling server into a multi-threaded or RESTful API service
- Replacing MySQL with another DB engine via abstraction

---

## 📌 Conclusion

This architecture provides a clear separation of concerns and allows for future maintainability, testing, and scalability.
