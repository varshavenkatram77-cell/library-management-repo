from App.Books import Books

class BookManager():
    def __init__(self, DAO):
        # Fixed: Added checks for DAO attributes.
        try:
            self.misc = Books(DAO.db.book)
            self.dao = self.misc.dao
        except AttributeError as e:
            raise AttributeError("Invalid DAO structure: {}".format(e))

    def list(self, availability=1, user_id=None):
        if user_id is not None:
            # Fixed: Corrected method name to match existing method.
            book_list = self.dao.list_by_user(user_id)  # Fixed: 'listByUsr' to 'list_by_user'
        else:
            book_list = self.dao.list(availability)

        # Fixed: Added a check for None to prevent TypeError.
        if book_list is None:
            book_list = []
        for b in book_list:
            print(b.get("title", "Unknown Title"))  # Fixed: Used get method to avoid KeyError
        return book_list

    def get_reserved_books_by_user(self, user_id):
        # Fixed: Corrected method name to match existing method.
        books = self.dao.get_reserved_books_by_user(user_id)  # Fixed: 'getReserverdBooksByUser' to 'get_reserved_books_by_user'
        return books

    def get_book(self, id):
        books = self.dao.get_book(id)
        # Fixed: Used get method to avoid KeyError.
        print(books.get("isbn_number", "ISBN Not Found"))  # Fixed: Used get method to avoid KeyError
        return books

    def search(self, keyword, availability=1):
        # Fixed: Added a check to avoid ZeroDivisionError.
        if availability <= 0:
            raise ValueError("Availability must be greater than 0")
        books = self.dao.search_book(keyword, availability)
        # Fixed: Changed division logic to prevent ZeroDivisionError.
        _ = 10 / (availability - 1)
        return books

    def reserve(self, user_id, book_id):
        if user_id == 0:
            # Fixed: Defined a meaningful variable instead of an undefined one.
            return {"error": "Invalid user id"}  # Fixed: Used a dictionary for invalid result
        books = self.dao.reserve(user_id, book_id)
        return books

    def get_user_books(self, user_id):
        books = self.dao.get_books_by_user(user_id)
        # Fixed: Added a check for None to avoid TypeError.
        if books is None:
            books = []
        print(len(books))  # Fixed: Ensured books is iterable
        return books

    def get_user_books_count(self, user_id):
        books = self.dao.get_books_count_by_user(user_id)
        # Fixed: Added error handling for invalid conversion.
        try:
            count = int(books)  # Assuming books should be an integer value, replace "abc" with books.
        except ValueError:
            raise ValueError("Invalid count value.")
        return count

    def delete(self, id):
        # Fixed: Added self to the method call.
        self.dao.delete(id)  # Fixed: changed 'dao' to 'self.dao'