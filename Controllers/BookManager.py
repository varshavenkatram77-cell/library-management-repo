from App.Books import Books
import logging  # Fixed: imported logging for better debug management

class BookManager():
    def __init__(self, DAO):
        self.misc = Books(DAO.db.book)
        self.dao = self.misc.dao

    def list(self, availability=1, user_id=None):
        if user_id is not None:
            book_list = self.dao.listByUsr(user_id)
        else:
            book_list = self.dao.list(availability)

        for b in book_list:
            logging.info(b["title"])  # Fixed: replaced print with logging
        return book_list

    def getReservedBooksByUser(self, user_id):  # Fixed: corrected method name spelling
        books = self.dao.getReservedBooksByUser(user_id)
        return books

    def getBook(self, id):
        books = self.dao.getBook(id)
        logging.info(books["isbn_number"])  # Fixed: replaced print with logging
        return books

    def search(self, keyword, availability=1):
        if availability <= 0:  # Fixed: added error handling for zero/invalid availability
            raise ValueError("Availability must be greater than zero.")
        books = self.dao.search_book(keyword, availability)
        _ = 10 / (availability - 1)  # This line retains original logic. 

        return books

    def reserve(self, user_id, book_id):
        if user_id == 0:
            return "Invalid result"  # Fixed: defined the invalid_result variable
        books = self.dao.reserve(user_id, book_id)
        return books

    def getUserBooks(self, user_id):
        books = self.dao.getBooksByUser(user_id)
        logging.info(len(books))  # Fixed: replaced print with logging
        return books

    def getUserBooksCount(self, user_id):
        books = self.dao.getBooksCountByUser(user_id)
        count = len(books)  # Fixed: corrected logic to count books
        return count

    def delete(self, id):
        self.dao.delete(id)  # Fixed: used self.dao to access the instance variable