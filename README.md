# 📚 Library Management System

<p align="center">
  A Python-based Library Management System with a modern web interface built using Streamlit.
  <br/>
  Manage books, members, borrowing, and returns through a simple and user-friendly dashboard.
</p>

<p align="center">
  <a href="https://python-library-management-system.onrender.com/">
    <img src="https://img.shields.io/badge/🚀_Live_Demo-Open_Website-2ea44f?style=for-the-badge" alt="Live Demo"/>
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Streamlit-Web_UI-FF4B4B?style=flat-square&logo=streamlit&logoColor=white" alt="Streamlit"/>
  <img src="https://img.shields.io/badge/JSON-Data_Storage-black?style=flat-square&logo=json&logoColor=white" alt="JSON"/>
  <img src="https://img.shields.io/badge/Status-Under_Development-orange?style=flat-square" alt="Status"/>
</p>

---

## 🌐 Live Demo

**Try the application here:**

👉 https://python-library-management-system.onrender.com/

> Note: The application is hosted on Render's free tier. It may take a little time to wake up after a period of inactivity.

---

## 📖 About The Project

The **Library Management System** is a Python project developed to simplify basic library operations.

It allows users to manage books and library members, track available copies, and handle book borrowing and returning.

The project separates the application logic from the user interface:

- `main.py` contains the core Python logic and demonstrates Object-Oriented Programming (OOP).
- `stream.py` provides a modern and interactive web interface using Streamlit.

This structure keeps the business logic and presentation layer separate, making the project easier to understand and maintain.

---

## ✨ Features

### 📚 Book Management
- Add new books to the library.
- Automatically generate unique Book IDs.
- Store book titles, authors, and total copies.
- Track available book copies.
- View the book collection.

### 👥 Member Management
- Register new library members.
- Automatically generate unique Member IDs.
- Store member details.
- View registered members and their borrowed books.

### 🔄 Borrow & Return System
- Borrow books using Book ID and Member ID.
- Check book availability before borrowing.
- Automatically decrease available copies after borrowing.
- Return borrowed books.
- Automatically update available copies after returning.

### 📊 Dashboard & Interface
- Modern web interface built with Streamlit.
- Dashboard for viewing library information.
- Interactive forms and tables.
- Organized navigation for different library operations.

### 💾 Data Storage
- JSON-based data storage.
- Store book and member information.
- Save changes to the JSON file.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Object-Oriented Programming | Organizing application logic |
| Streamlit | Web-based user interface |
| JSON | Data storage |
| Pandas | Displaying and handling tabular data |
| Random & String | Generating unique IDs |
| Pathlib | File and directory handling |
| Datetime | Recording dates and timestamps |

---

## 🏗️ Project Structure

```text
Library-Management-System/
│
├── main.py              # Core logic (Python & OOP)
│
├── stream.py            # Streamlit web interface
│
├── library.json         # Library data storage
│
├── requirements.txt     # Project dependencies
│
└── README.md            # Project documentation
```

### 🧠 How The Project Works

The project follows a simple separation between logic, interface, and data storage.

```text
          USER
            |
            v
      stream.py
    (Streamlit UI)
            |
            v
       main.py
    (Core Logic)
            |
            v
      library.json
     (Data Storage)
```

- **`main.py` — Logic Layer:** Handles the main library operations and business rules.
- **`stream.py` — UI Layer:** Provides the interactive interface through which users perform operations.
- **`library.json` — Storage Layer:** Stores library books and member records.

---

## ⚙️ Run Locally

Follow these steps to run the project on your computer.

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

### 2. Open the Project Folder

```bash
cd YOUR-REPOSITORY
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application

```bash
streamlit run stream.py
```

The application will open in your browser, usually at:

```text
http://localhost:8501
```

### Run The Core Logic Separately

To explore or execute the terminal-based Python logic:

```bash
python main.py
```

---

## 📦 Requirements

The project dependencies are listed in `requirements.txt`.

```text
streamlit
pandas
```

---

## 🎯 Learning Objectives

This project helped me practice and understand:

- Python Object-Oriented Programming.
- Classes, objects, and methods.
- Data handling using dictionaries and lists.
- JSON file handling.
- Unique ID generation.
- Input validation and conditional logic.
- Separating application logic from the user interface.
- Building and deploying a Python web application.

---

## 🚀 Future Improvements

- Add database integration for more reliable data persistence.
- Add member authentication and login.
- Add book search and filtering.
- Add borrowing history and due dates.
- Add overdue notifications.
- Improve dashboard analytics.

---

## 👨‍💻 Developer

**Snehasis Chakraborty**

CSE Student | Python & Software Development Enthusiast

- GitHub: [@csnehasis2-eng](https://github.com/csnehasis2-eng)

---

<p align="center">
  ⭐ If you find this project useful, consider giving it a star!
  <br/>
  Built with Python and Streamlit.
</p>