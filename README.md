# Library Management System

A simple Library Management System built as a student backend project using Python, Flask, SQLite, HTML, CSS, and JavaScript.

The project provides REST APIs for managing books, library members, borrowing and returning books, and borrowing history. It also includes a simple web interface to interact with the system through a web browser.

## Project Description

The Library Management System is designed to manage basic library operations.

The backend provides APIs to:

- Add and view books
- Add and view library members
- Update member details
- Borrow books
- Return books
- Check book availability
- Prevent unavailable books from being borrowed
- Store borrowing and return history

A simple frontend is included to interact with the library system.

## Features

### Backend Features

- Add new books
- View all books
- Add new library members
- View all members
- Update member details
- Borrow books
- Return books
- Track book availability
- Prevent borrowing of unavailable books
- Store borrowing and return history
- SQLite database for storing project data

### Frontend Features

- Display all books
- Display book availability
- Display all library members
- Borrow a book using Book ID and Member ID
- Return a book using Book ID and Member ID
- Display borrowing history
- Show success and error messages

## Technologies Used

- Python
- Flask
- SQLite
- HTML
- CSS
- JavaScript
- REST API
- JSON

## Project Structure

library management system/
│
├── app.py
├── database.py
├── library.db
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css

## Backend API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Opens the frontend web interface |
| GET | `/books` | View all books |
| POST | `/books` | Add a new book |
| GET | `/members` | View all library members |
| POST | `/members` | Add a new member |
| PUT | `/members/<member_id>` | Update member details |
| POST | `/borrow` | Borrow a book |
| POST | `/return` | Return a book |
| GET | `/history` | View borrowing history |

## How the Backend Works

1. A book can be added through the `/books` POST endpoint.
2. The book is stored in the SQLite database.
3. When a member borrows a book, the `/borrow` endpoint checks whether the book is available.
4. If the book is available, a borrowing record is created and the book is marked as unavailable.
5. When the book is returned, the `/return` endpoint updates the return date and marks the book as available again.
6. The `/history` endpoint displays borrowing and return records.

## Database

The project uses SQLite as its database.

The database contains three main tables:

### Books

Stores:

- Book ID
- Book title
- Author
- Availability status

### Members

Stores:

- Member ID
- Member name
- Member email

### Borrowings

Stores:

- Borrowing ID
- Book ID
- Member ID
- Borrow date
- Return date

## Frontend

The frontend is created using HTML, CSS, and JavaScript.

The main frontend page is:

templates/index.html

The styling is stored in:

static/style.css

JavaScript uses the `fetch()` function to communicate with the Flask backend.

The frontend allows users to:

- View books
- View members
- Borrow books
- Return books
- View borrowing history

## How to Run the Application

### 1. Install Dependencies

Open a terminal in the project folder and run:

```bash
pip install -r requirements.txt

You can also install Flask directly:

pip install flask
2. Create the Database

Run:

python database.py

You should see:

All tables created successfully!

3. Start the Flask Application

Run:

python app.py

The application will run at:

http://127.0.0.1:5000/

4. Open the Web Interface

Open the following address in your browser:

http://127.0.0.1:5000/

Example API Requests
Add a Book

POST /books

{
    "title": "Harry Potter",
    "author": "J.K. Rowling"
}
Add a Member

POST /members

{
    "name": "Amit",
    "email": "example@email.com"
}
Borrow a Book

POST /borrow

{
    "book_id": 1,
    "member_id": 1
}
Return a Book

POST /return

{
    "book_id": 1,
    "member_id": 1
}
Update a Member

PUT /members/1

{
    "name": "Amit",
    "email": "newemail@example.com"
}
Error Handling

The backend checks important conditions before performing operations.

For example:

If a book does not exist, the system returns a book-not-found message.
If a book is already borrowed, the system prevents another member from borrowing it.
If there is no active borrowing record during return, the system returns an appropriate error message.
If a member does not exist while updating, the system returns a member-not-found message.
API Testing

The backend APIs were tested to verify:

Adding books
Viewing books
Adding members
Viewing members
Updating member details
Borrowing books
Returning books
Viewing borrowing history
Preventing an unavailable book from being borrowed
Learning Outcomes

Through this project, I practiced:

Python programming
Flask application development
REST API development
GET, POST, and PUT HTTP methods
JSON request and response handling
SQLite database operations
Connecting frontend with backend
JavaScript fetch() requests
GitHub project management
Future Improvements

Possible future improvements include:

User authentication
Admin panel
Book search
Due dates and overdue tracking
Reservation or waitlist system
Better frontend design
Book deletion and editing
Dashboard and statistics
Note

This project was developed as a student backend project with AI-assisted learning and guidance.



