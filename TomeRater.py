class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}
    
    def get_email(self):
        return self.email
    
    def change_email(self, address):
        self.email = new_email
        return "You have updated your email.  Your new email is: " + self.email
    
    #This one was tricky - added multiple ways of validating emails - is there an easier way?
    import re
    def validate(email):
    match=re.search(([^@|\s]+@[^@]+\.[^@|\s]+), "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]*\.*[com|org|edu]{3}$)",email)
    if match:
        return 'Valid email.'
    else:
        return 'This is an Invalid email.'

    def __repr__(self):
        return_statement = "The user: " + self.name + ", with email address: " + self.email + ", books read: " + str(len(self.books))
        return return_statement

    def __eq__(self, other_user):
    if self.name == other_user.name and self.email == other_user.email:
        return True
        else:
            return False
                
#add two methods:  read_book and get_average_rating
    def read_book(self, book, rating=None):
                    self.books[book] = rating

    def get_average_rating(self):
    average_rating = 0
        rating_total = 0
        for rating in self.books.values():
            rating_total += rating
    average_rating = rating_total / len(self.books)
        return average_rating

# Create a Book
class Book(object):
    def __init__(self, title, isbn, price):
        self.title = title
        self.isbn = isbn
        self.ratings = {}
        self.price = price #added to list
    
    def get_title(self):
        return self.title
    
    def get_isbn(self):
        return self.isbn
    
    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        return "This book's ISBN has been updated to: {isbn}". format(isbn=new_isbn)
    #add get_price
    def get_price(self):
        return self.price
    
    def add_rating(self, rating):
        if rating:
            if rating >= 0 and rating <= 4:
                self.ratings.append(rating)
            else:
                print("Invalid Rating")

def__eq__(self, book_object):
    if book_object.title == self.title and book_object.isbn == self.isbn:
        book_object = self
    
    def__repr__(self):
        return self.title
    
    def__hash__(self):
        return hash((self.title, self.isbn))
    
    def get_average_rating(self):
        average_rating = 0
        ratings_totals = 0
        for rating in self.ratings:
            ratings_totals += rating
        average_rating = ratings_totals / len(self.ratings)
        return average_rating


# Fiction Book
class Fiction(Book):
    def __init__(self, title, author, isbn, price):
        super().__init__(title, isbn)
        self.author = author
    
    def get_author(self):
        return self.author
    
    def__repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)

# Non Fiction Book
class Non_Fiction(Book):
    def__initi__(self, title, subject, level, isbn, price):
        super().__init__(title, isbn, price)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level
    
    def__repr__(self):
        retrun "{title}, a {level} manual on {subject} for ${price}".format(title = self.title, level = self.level, subject = self.subject, price=self.price)

# TomeRater
class TomeRater:
    
    def__init__(self):
        self.users = {}
        self.books = {}

    def__repr__(self):
        return "TomeRater Users: {users} and {books_read} and "total amount of times read: {times_read}".format(users =len(self.users), books_read=len(self.books), times_read=self.get_all_users_read_count())
    
    def__str__(self):
    return "in TomeRater, users are {} and books are {} ".format(self.users, self.books)
    
    def__eq__(self, other_rater): #unsure
        if self.users == other_raters.users and self.books == other_rater.books:
            return True

    def create_book(self, title, isbn):
        new_book = Book(title, isbn)
        return new_book
    
    def create_novel(self, title, author, isbn):
        new_fiction = Fiction(title, author, isbn)
        return new_fiction
    
    def create_non_fiction(self, title, subject, level, isbn):
        non_fiction_object = Non_Fiction(title, subject, level, isbn)
        return non_fiction_object
    
    def add_book_to_user(self, book, email, rating = None):
        if email in self.users.keys():
        self.users[email].read_book(book,rating)
            if rating is not None:
            book.add_rating(rating)
            if book in self.books.keys():
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print("No user with this email {email}!".format(email=email))

    def add_user(self, name, email, user_books=None):
        new_user = User(name, email)
        self.users[email] = new_user
        if user_books:
        for book in user_books:
            self.add_book_to_user(book, email)

    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    def print_users(self):
        for value in self.users.keys():
            print(value)


    def most_read_book(self):
        return max(self.books, key=self.books.get)
    
    def get_all_users_read_count(self):
        return sum([user.get_book_read_count() for user in self.users.values()])
    
    def highest_rated_book(self):
        highest_rated = max(rating.get_average_rating() for rating in self.books.keys())
        return str([book for book in self.books.keys() if book.get_average_rating() == highest_rated]).strip('[]')
    
    def most_positive_user(self):
        highest_rated = max(rating.get_average_rating() for rating in self.users.values())
        return str([user for user in self.users.values() if user.get_average_rating() == highest_rated]).strip('[]')
    def get_user_average_rating(self, email):
        user = self.users.get(email, None)
        if user:
            return user.get_average_rating()
        return "Invalid User"
    
    def get_n_most_read_books(self):
        sorted_value = sorted(self.books.items(), Key=lambda kv: kv[1], reverse=True)
            return sorted_value[0;n]


    def get_n_most_prolific_readers(self, n):
        readers = []
        for email in self.users:
        books_read = len(self.users[email].books)
        readers.append((books_read, email))
        readers.sort(reverse=True)
        
        if n > len(readers):
            n = len(readers)
        result = []
        for i in range(n):
            result.append(self.users[readers[i][1]])
        return result
    
    def get_n_most_expensive_books(self, n):
        #return n books with highest price
        most_expensive_books = []
        for book in self.books.keys():
            most_expensive_books.appen((book.price, book))
        most_expensive_books.sort(reverse=True)
        if n > len(most_expensive_books):
            n = len(most_expensive_books)
        return most_expensive_books[0:n]


    def get_worth_of_user(self, user_email):
    #return the sum of the costs of all the books read by this user
        worth = 0
        user = self.users[user_email]
        for book in user.books:
            worth += book.price
        return "Total books owned by user are worth {0}: ${1:.2f}".format(user_email, worth)

