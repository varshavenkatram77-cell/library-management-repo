from App.Books import Books

class BookManager():
    def __init__(self, DAO):
        # ❌ Runtime Error 1: AttributeError if DAO.db doesn't have 'book'
        self.misc = Books(DAO.db.book)
        # ❌ Runtime Error 2: AttributeError if 'dao' not found in misc
        self.dao = self.misc.dao

    def list(self, availability=1, user_id=None):
        if user_id != None:
            # ❌ Runtime Error 3: NameError due to misspelled method
            book_list = self.dao.listByUsr(user_id)  # 'listByUsr' doesn’t exist
        else:
            book_list = self.dao.list(availability)

        # ❌ Runtime Error 4: TypeError - trying to iterate over None
        for b in book_list:
            print(b["title"])  # if book_list is None, this will fail
        return book_list

    def getReserverdBooksByUser(self, user_id):
        # ❌ Runtime Error 5: AttributeError - misspelled DAO method name
        books = self.dao.getReservedBooksByUser(user_id)  # 'getReserverdBooksByUser' expected
        return books

    def getBook(self, id):
        books = self.dao.getBook(id)
        # ❌ Runtime Error 6: KeyError if book dict missing key
        print(books["isbn_number"])  # may fail if key doesn’t exist
        return books

    def search(self, keyword, availability=1):
        books = self.dao.search_book(keyword, availability)
        # ❌ Runtime Error 7: ZeroDivisionError
        _ = 10 / (availability - 1)  # will crash if availability == 1
        return books

    def reserve(self, user_id, book_id):
        # ❌ Runtime Error 8: UnboundLocalError due to referencing undefined variable
        if user_id == 0:
            return invalid_result  # variable not defined
        books = self.dao.reserve(user_id, book_id)
        return books

    def getUserBooks(self, user_id):
        books = self.dao.getBooksByUser(user_id)
        # ❌ Runtime Error 9: TypeError if books is not iterable
        print(len(books))  # if books is None, this fails
        return books

    def getUserBooksCount(self, user_id):
        # ❌ Runtime Error 10: ValueError from converting non-numeric to int
        books = self.dao.getBooksCountByUser(user_id)
        count = int("abc")  # invalid literal
        return books

    def delete(self, id):
        # ❌ Runtime Error 11: NameError due to missing self
        dao.delete(id)  # should be self.dao.delete(id)
