# Library Management System

A simple backend API for managing books, library members, and book borrowing and returning.

## Project Description

The Library Management System provides backend APIs to manage books and library members. It allows members to borrow and return books while keeping track of book availability and borrowing history.

## Features

- Add new books
- View all books
- Add new library members
- View all members
- Update member details
- Borrow books
- Return books
- Check book availability
- Prevent borrowing of unavailable books
- Store borrowing and return history
- SQLite database for storing data

## Technologies Used

- Python
- Flask
- SQLite
- REST API
- JSON

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/books` | View all books |
| POST | `/books` | Add a new book |
| GET | `/members` | View all members |
| POST | `/members` | Add a new member |
| PUT | `/members/<member_id>` | Update member details |
| POST | `/borrow` | Borrow a book |
| POST | `/return` | Return a book |
| GET | `/history` | View borrowing history |

## Database

The project uses SQLite as the database.

It contains three main tables:

### Books
Stores:
- Book ID
- Title
- Author
- Availability

### Members
Stores:
- Member ID
- Name
- Email

### Borrowings
Stores:
- Borrowing ID
- Book ID
- Member ID
- Borrow date
- Return date

## How to Run the Application

### 1. Install Flask

Open the terminal in the project folder and run:

```bash
pip install flask