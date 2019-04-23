class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def __repr__(self):
        return "User: {} - Email: {} - Number of Books Read: {}".format(self.name, self.email, len(self.books))

    def __eq__(self, other_user):
        if (self.name == other_user.name) and (self.email == other_user.email):
            return True
        else:
            return False

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("{} email address has been updated to {}.".format(self.name, self.email))

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_books_read(self):
        return self.books

    def get_num_books_read(self):
        return len(self.books)
     
    def get_average_rating(self):
        sum = 0
        count = 0
        for book_rating in self.books.values():
            if book_rating:
                sum += book_rating
                count += 1
       
        if count != 0:
            return sum / count 
        else:
            return 0

class Book(object):
    def __init__(self, title, isbn, price):
        self.title = title
        self.isbn = isbn
        self.price = price
        self.ratings = []

    def __eq__(self, other_book):
        if (self.title == other_book.title) and (self.isbn == other_book.isbn):
            return True
        else:
            return False

    def __repr__(self):
        return "TITLE: {} ISBN: {}".format(self.title, self.isbn)

    def __hash__(self):
        return hash((self.title, self.isbn))

    def get_price(self):
        return self.price

    def get_title(self):
        return self.title
    
    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("{} isbn has been updated - {}".format(self.title, self.isbn))

    def add_rating(self, rating):
        if rating:
            if (rating > 0) and (rating <= 4):
                self.ratings.append(rating)
            else:
                print("Invalid Rating")

    def get_average_rating(self):
        sum = 0
        count = 0
        for rating in self.ratings:
            if rating:
                sum += rating
                count += 1
        if count != 0:
            return sum / count
        else:
            return 0

class Fiction(Book):
    def __init__(self, title, author, isbn, price):
        super().__init__(title, isbn, price)
        self.author = author

    def __repr__(self):
        return "TITLE: {} AUTHOR: {}".format(self.title, self.author)

    def get_author(self):
        return self.author

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn, price):
        super().__init__(title, isbn, price)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "TITLE: {} LEVEL: {} SUBJECT: {}".format(self.title, self.level, self.subject)

class TomeRater:
    def __init__(self):
        self.users = {} # key=User email, value=User object
        self.books = {} # key=Book object, value=# of users who have read it

    def __repr__(self):
        return "Current TomeRater Stats: Number of Users: {} -> Number of Books: {}".format(len(self.users), len(self.books))
        
    def create_book(self, title, isbn, price):
        return Book(title, isbn, price)

    def create_novel(self, title, author, isbn, price):
        return Fiction(title, author, isbn, price)

    def create_non_fiction(self, title, subject, level, isbn, price):
        return Non_Fiction(title, subject, level, isbn, price)

    def add_book_to_user(self, book, email, rating = None):
        if self.users[email]:
            self.users[email].read_book(book, rating)
            if rating:
                book.add_rating(rating)
            if book not in self.books: # Make sure the Title AND ISBN are unique
                self.books[book] = 1
            else:
                self.books[book] += 1
        else:
            print("No user with email {}!".format(email))
     

    def add_user(self, name, email, user_books = None):
        #Check if email is already in use
        UNIQUE_FLAG = True
        for user_email in self.users.keys():
            if email == user_email:
                UNIQUE_FLAG = False
                print("ERROR: User email {} is alread in use.".format(email))
                break
            else:
                continue

        if UNIQUE_FLAG:
            self.users[email] = User(name, email)
            if user_books:
                for book in user_books:
                    self.add_book_to_user(book, email)

    def print_catalog(self):
        for books in self.books.keys():
            print(books)

    def print_users(self):
        for users in self.users.values():
            print(users)

    def most_read_book(self):
        most_read = max(self.books.keys(), key=(lambda k: self.books[k]))
        return most_read

    def highest_rated_book(self):
        highest_rated = max(self.books.keys(), key=(lambda k: k.get_average_rating()))
        return highest_rated

    def most_positive_user(self):
        most_positive = max(self.users.values(), key=(lambda k: k.get_average_rating()))
        return most_positive

    def get_n_most_expensive_books(self, n):
        prices = {}
        for book in self.books.keys():
            prices[book.get_title()] = book.get_price()
        sorted_d = sorted(prices.items(), key=lambda x: x[1])
        if n <= len(sorted_d):
            print("The top {} most expensive books.".format(n))
            for x in range(len(sorted_d) - 1, len(sorted_d) - n - 1, -1):
                print(sorted_d[x])
        else:
            print("ERROR: We dont have that many books")

    def get_worth_of_user(self, user_email):
        worth = 0
        if self.users[user_email]:
            books_read = self.users[user_email].get_books_read()
            for book in books_read:
                worth += book.get_price()
            print("{} worth is ${}".format(user_email, round(worth,2)))
        else:
            print("ERROR: Invalid user email")

    def get_n_most_read_books(self, n):
        sorted_d = sorted(self.books.items(), key=lambda x: x[1])
        if n <= len(sorted_d):
            print("The {} most read books.".format(n))
            for x in range(len(sorted_d) - 1, len(sorted_d) - n - 1, -1):
                print(sorted_d[x])
        else:
            print("ERROR: We dont have that many books")

    def get_n_most_prolific_readers(self, n):
        books_read = {}
        for email, num_books in self.users.items():
            books_read[email] = num_books.get_num_books_read()
        sorted_d = sorted(books_read.items(), key=lambda x: x[1])
        if n <= len(sorted_d):
            print("The top {} most prolific readers.".format(n))
            for x in range(len(sorted_d) - 1, len(sorted_d) - n - 1, -1):
                print(sorted_d[x])
        else:
            print("ERROR: We dont have that many books")