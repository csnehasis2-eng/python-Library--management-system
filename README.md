# 📚 Library Management System

A console-based **Library Management System** built with Python and Object-Oriented Programming (OOP). This project helps manage books, members, and borrowing/returning operations with persistent data storage using JSON.

The system is designed to demonstrate practical Python concepts through a simple, structured, and interactive application.

## ✨ Features

### 📖 Book Management
- Add new books to the library.
- Automatically generate unique Book IDs.
- Store book details such as title, author, and total copies.
- Display all available book records.
- Track total and available copies.

### 👤 Member Management
- Register new library members.
- Automatically generate unique Member IDs.
- Store member details such as name and email.
- Display registered members and their borrowed books.

### 🔄 Borrow & Return System
- Borrow books using Member ID and Book ID.
- Check book availability before borrowing.
- Automatically decrease available copies when a book is borrowed.
- Return previously borrowed books.
- Automatically increase available copies after returning a book.

### 💾 Data Persistence
- Store all library records in a JSON file.
- Preserve books and member information between program executions.
- Automatically save changes after operations.

## 🛠️ Technologies & Concepts Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| OOP | Class and object-based structure |
| JSON | Data storage |
| `json` | Reading and writing JSON data |
| `random` | Generating random IDs |
| `string` | Uppercase letters and digits |
| `pathlib` | File and path handling |
| `datetime` | Recording timestamps |

## 📂 Project Structure

```text
Library-Management-System/
│
├── main.py          # Main application
├── library.json     # Library database
└── README.md        # Project documentation
```

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Library-Management-System.git
```

### 2. Navigate to the Project Directory

```bash
cd Library-Management-System
```

### 3. Run the Application

```bash
python main.py
```

**Requirements:** Python 3.x

No external Python packages are required.

## 🖥️ Application Menu

```text
==================================================
          Library Management System
==================================================

1. Add Book
2. List Book
3. Add Member
4. List Member
5. Borrow Book
6. Return Book
0. Exit the Portal

--------------------------------------------------
What task you want to do?
```

## 📊 How It Works

The application follows a simple workflow:

1. **Add Books:** Register books with automatically generated IDs.
2. **Register Members:** Create member records with unique IDs.
3. **Borrow Books:** Members borrow books using their IDs.
4. **Return Books:** Returned books are added back to the available inventory.
5. **Save Data:** All modifications are stored in `library.json`.

## 🎯 Learning Objectives

This project helped me practice:

- Python Object-Oriented Programming.
- Classes, objects, and class methods.
- Lists and dictionaries.
- List comprehension.
- File handling and JSON serialization.
- Exception handling.
- Random ID generation.
- Date and time handling.
- Working with persistent data.

## 🔮 Future Improvements

Potential improvements for future versions:

- Search books by title, author, or ID.
- Delete and update book records.
- Member-wise borrowing history.
- Due dates and fine calculation.
- Input validation and duplicate prevention.
- Graphical User Interface (GUI).
- Database integration using SQLite.

## 👨‍💻 Author

**Snehasis Chakraborty**

B.Tech CSE Student | Python & Programming Enthusiast

- GitHub: [@csnehasis2-eng](https://github.com/csnehasis2-eng)

---

⭐ If you find this project interesting, feel free to explore the repository!