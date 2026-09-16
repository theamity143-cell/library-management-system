from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    connection = sqlite3.connect("library.db")
    connection.row_factory = sqlite3.Row
    return connection


@app.route("/")
def home():
    return "Library Management System is running!"


@app.route("/books", methods=["GET"])
def get_books():
    connection = get_db_connection()
    books = connection.execute("SELECT * FROM books").fetchall()
    connection.close()

    return jsonify([dict(book) for book in books])
@app.route("/books", methods=["POST"])
def add_book():
    data = request.json

    title = data["title"]
    author = data["author"]

    connection = get_db_connection()

    connection.execute(
        "INSERT INTO books (title, author) VALUES (?, ?)",
        (title, author)
    )

    connection.commit()
    connection.close()

    return jsonify({"message": "Book added successfully!"})
@app.route("/members", methods=["POST"])
def add_member():
    data = request.json

    name = data["name"]
    email = data["email"]

    connection = get_db_connection()

    connection.execute(
        "INSERT INTO members (name, email) VALUES (?, ?)",
        (name, email)
    )

    connection.commit()
    connection.close()

    return jsonify({"message": "Member added successfully!"})
@app.route("/borrow", methods=["POST"])
def borrow_book():
    data = request.json

    book_id = data["book_id"]
    member_id = data["member_id"]

    connection = get_db_connection()

    # Check if book exists and is available
    book = connection.execute(
        "SELECT * FROM books WHERE id = ?",
        (book_id,)
    ).fetchone()

    if book is None:
        connection.close()
        return jsonify({"message": "Book not found!"}), 404

    if book["available"] == 0:
        connection.close()
        return jsonify({"message": "Book is not available!"}), 400

    # Add borrowing record
    connection.execute(
        "INSERT INTO borrowings (book_id, member_id, borrow_date) VALUES (?, ?, DATE('now'))",
        (book_id, member_id)
    )

    # Mark book as unavailable
    connection.execute(
        "UPDATE books SET available = 0 WHERE id = ?",
        (book_id,)
    )

    connection.commit()
    connection.close()

    return jsonify({"message": "Book borrowed successfully!"})
@app.route("/return", methods=["POST"])
def return_book():
    data = request.json

    book_id = data["book_id"]
    member_id = data["member_id"]

    connection = get_db_connection()

    # Find the active borrowing record
    borrowing = connection.execute(
        """SELECT * FROM borrowings
           WHERE book_id = ? AND member_id = ? AND return_date IS NULL""",
        (book_id, member_id)
    ).fetchone()

    if borrowing is None:
        connection.close()
        return jsonify({"message": "No active borrowing found!"}), 404

    # Set return date
    connection.execute(
        "UPDATE borrowings SET return_date = DATE('now') WHERE id = ?",
        (borrowing["id"],)
    )

    # Make book available again
    connection.execute(
        "UPDATE books SET available = 1 WHERE id = ?",
        (book_id,)
    )

    connection.commit()
    connection.close()

    return jsonify({"message": "Book returned successfully!"})
@app.route("/history", methods=["GET"])
def get_history():
    connection = get_db_connection()

    history = connection.execute("""
        SELECT
            borrowings.id,
            books.title AS book,
            members.name AS member,
            borrowings.borrow_date,
            borrowings.return_date
        FROM borrowings
        JOIN books ON borrowings.book_id = books.id
        JOIN members ON borrowings.member_id = members.id
    """).fetchall()

    connection.close()

    return jsonify([dict(record) for record in history])
@app.route("/members", methods=["GET"])
def get_members():
    connection = get_db_connection()

    members = connection.execute("SELECT * FROM members").fetchall()

    connection.close()

    return jsonify([dict(member) for member in members])

    
# NEW update member route
@app.route("/members/<int:member_id>", methods=["PUT"])
def update_member(member_id):
    data = request.json

    name = data["name"]
    email = data["email"]

    connection = get_db_connection()

    member = connection.execute(
        "SELECT * FROM members WHERE id = ?",
        (member_id,)
    ).fetchone()

    if member is None:
        connection.close()
        return jsonify({"message": "Member not found!"}), 404

    connection.execute(
        "UPDATE members SET name = ?, email = ? WHERE id = ?",
        (name, email, member_id)
    )

    connection.commit()
    connection.close()

    return jsonify({"message": "Member updated successfully!"})




if __name__ == "__main__":
    app.run(debug=True)





   