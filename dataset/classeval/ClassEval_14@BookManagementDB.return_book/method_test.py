def test(self):
        self.db_name = "test.db"
        self.db = BookManagementDB(self.db_name)
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        # Add a book for testing returning
        self.db.add_book("Book to Return", "James Smith")
        self.db.borrow_book(1)
        self.db.return_book(1)

        # Check if the book was marked as available again
        self.cursor.execute("SELECT available FROM books WHERE id=1")
        result = self.cursor.fetchone()
        return result[0]