
class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
#self.books maps a Book object to the user's rating of the book
        self.books = {}

    def get_email(self):
        return self.email  #should this be email or self.email?

    def change_email(self, address):
        self.email = address
        print('{}\'s email has been updated'.format(self.name))

    def __repr__(self):
        print('User {name}, email: {email}, books read: {books}'.format(name = self.name, email = self.email, books = len(self.books)))

#compares users to see if they are the same
    def __eq__(self, other_user):
        if (self.email == other_user.email) & (self.name == other_user.name)== True:
            return True
        else:
            return False

    def read_book(self, book, rating = None):
        self.books[book] = rating

    def get_average_rating(self):
        total_ratings = 0
        number_of_ratings = 0
        for book in self.books:
            if self.books[book] is not None:
                total_ratings+= self.books[book]
                number_of_ratings+=1
            average_rating = total_ratings/number_of_ratings
        return average_rating
            

class Book(object):
    def __init__(self,title,isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def __hash__(self):
        return hash((self.title, self.isbn))

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print('This book\'s ISBN has been updated')

    def add_rating(self, rating):
        if rating is not None:
            if (rating>=0)&(rating<=4):
                self.ratings.append(rating)
            else:
                print('Invalid Rating')       
            
    def __eq__(self, other_book):
        if (self.title == other_book.title) & (self.isbn == other_book.isbn):
            return True
        else:
            return False

    def get_average_rating(self):
        total_ratings = 0
        number_of_ratings = 0
        for rating in self.ratings:
            if rating is not None:
                total_ratings+=rating
                number_of_ratings+=1
            average_rating = total_ratings/number_of_ratings
        return average_rating

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return '{title} by {author}'.format(title = self.title, author = self.author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return '{title}, a {level} manual on {subject}'.format(title = self.title, level = self.level, subject = self.subject)
    
    
class TomeRater():
    def __init__(self):
        self.users = {}  # user's email : correponding user object
        self.books = {}  # Book object :  number of users that have read it
        
    def create_book(self, title, isbn):
        new_book = Book(title, isbn)
        return new_book

    def create_novel(self,title,author,isbn):
        new_fiction = Fiction(title,author,isbn)
        return new_fiction

    def create_non_fiction(self, title,subject,level,isbn):
        new_non_fiction = Non_Fiction(title,subject,level,isbn)
        return new_non_fiction



    def add_book_to_user(self, book, email, rating = None):
        
        try:
            self.users[email].read_book(book,rating)
            book.add_rating(rating)
            if book in self.books.items():
                self.books[book] +=1
            else:
                self.books[book] = 1
        except:
            print("No user with email {}!".format(email))


    def add_user(self, name, email, user_books = None):
        self.users[email] = User(name, email)
        if user_books is not None:
            for book in user_books:
                self.add_book_to_user(book, email)
        else:
            user_books = []

    def print_catalog(self):
        for book in self.books:
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user.name)
            print('User {name}, email: {email}'.format(name = user.name, email = user.email))


    def most_read_book(self):
        max_number_of_reads = 0
        for book in self.books.keys():
            times_read = self.books[book]
            if times_read > max_number_of_reads:
                max_number_of_reads= times_read
                most_read_book = book
            return most_read_book.get_title()

    def highest_rated_book(self):
        highest_rating = 0
        highest_rated_book = []
        for book in self.books.keys():
            average_rating = book.get_average_rating()
            if average_rating> highest_rating:
                highest_rating = average_rating
                highest_rated_book = book
        return highest_rated_book

    def most_positive_user(self):
        most_positive_rating = 0
        highest_rated_book = []
        for user in self.users.values():
            average_rating = user.get_average_rating()
            if average_rating>most_positive_rating:
                most_positive_rating = average_rating
                most_positive_user = user
            return most_positive_user




            
            
    
            
    
            
            
        
        

