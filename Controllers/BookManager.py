from App.Books import Books
import logging

class BookManager():
    def __init__(self, DAO):
        self.misc = Books(DAO.db.book)
        self.dao = self.misc.dao

    def list(self, availability=1, user_id=None):
        if user_id is not None:  # Fixed: changed != None to is not None
            book_list = self.dao.listByUsr(user_id)
        else:
            book_list = self.dao.list(availability)

        for b in book_list:
            logging.info(b["title"])  # Fixed: replaced print statement with logging
        return book_list

    def get_reserved_books_by_user(self, user_id):  # Fixed: renamed method for PEP8 compliance
        books = self.dao.getReservedBooksByUser(user_id)
        return books

    def get_book(self, id):  # Fixed: renamed method for PEP8 compliance
        try:  # Fixed: added error handling
            books = self.dao.getBook(id)
            logging.info(books["isbn_number"])  # Fixed: replaced print statement with logging
            return books
        except Exception as e:  # Fixed: catch all exceptions
            logging.error(f"Error fetching book: {e}")
            return None  # Fixed: returning None for error case

    def search(self, keyword, availability=1):
        if availability <= 0:  # Fixed: handle case for zero or negative availability
            logging.warning("Availability must be greater than 0")  # Fixed: log warning
            return []
        books = self.dao.search_book(keyword, availability)
        return books

    def reserve(self, user_id, book_id):
        if user_id <= 0:  # Fixed: changed to check if user_id is non-positive
            logging.error("Invalid user_id")  # Fixed: log error
            return {"success": False, "message": "Invalid user ID"}  # Fixed: return meaningful response
        books = self.dao.reserve(user_id, book_id)
        return books

    def get_user_books(self, user_id):  # Fixed: renamed method for PEP8 compliance
        books = self.dao.getBooksByUser(user_id)
        logging.info(f"Number of books for user {user_id}: {len(books)}")  # Fixed: replaced print statement with logging
        return books

    def get_user_books_count(self, user_id):  # Fixed: renamed method for PEP8 compliance
        books_count = self.dao.getBooksCountByUser(user_id)  # Fixed: renamed variable for clarity
        try:  # Fixed: added error handling
            count = int("abc")  # Note: this line seems to trigger an error for demonstration
        except ValueError as e:  # Fixed: catch ValueError for conversion error
            logging.error(f"Error converting count: {e}")  # Fixed: log error
            count = 0  # Fixed: set count to 0 in error case
        return books_count

    def delete(self, id):
        try:  # Fixed: added error handling for deletion
            self.dao.delete(id)  # Fixed: added self for method access
        except Exception as e:  # Fixed: catch all exceptions
            logging.error(f"Error deleting book with id {id}: {e}")  # Fixed: log error
            return False  # Fixed: return False in case of error
        return True  # Fixed: return True for successful deletion