class User():
    def __init__(self, name, email):
        self.books = {}
        self.name = name
        self.email = email

    def __eq__(self, other_user):
        # Are two User objects the same?
        return self.name == other_user.name and self.email == other_user.email

    def __repr__(self):
        # string representation of what the object is
        return "\t**User {}, email: {}, books read: {}**\n".format(self.name, self.email, len(self.books))

    def get_email(self):
        # Return the User's email
        return self.email

    def change_email(self, new_address):
        # Change the users email
        print("\tCurrent email address is {}".format(self.email))
        self.email = new_address
        print("\tNew email address is {}".format(self.email))

    def change_name(self, new_name):
        # Change the users name
        print("\tCurrent name is {}".format(self.name))
        self.name = new_name
        print("\tNew name is {}".format(self.name))

    def read_book(self, book, rating = None):
        # User read book and left a rating
        self.books[book] = rating

    def get_average_rating(self):
        # iterate over the books, if it has a rating compute the averge 
        num_of_keys = len(self.books)
        total_ratings = 0
        for key in self.books:
            if self.books[key] is not None:
                total_ratings = total_ratings + self.books[key]
        #print("\tNum of keys {} and total ratings {}".format(num_of_keys, total_ratings))
        return total_ratings / num_of_keys
    


class Book():
    def __init__(self, title, isbn):
        self.ratings = []
        self.title = title
        self.isbn = isbn

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __eq__(self):
        return self.title == other_book.title and self.isbn == other_book.isbn

    def get_title(self):
        # Return the Books Title
        return self.title

    def get_isbn(self):
        # REturn the Books isbn number
        return self.isbn

    def set_isbn(self, new_isbn):
        # Change the isbn from old to new
        print("\tCurrent isbn {}".format(self.isbn))
        # Set books new isbn
        self.isbn = new_isbn
        print("\tNew isbn {}".format(new_isbn))

    def add_rating(self, rating):
        # Check if the rating is not None
        # Validate ratings is between 0 and 4
        if rating is not None:
            if rating > 0 and rating < 5:
                self.ratings.append(rating)
            else:
                print("\tInvalid Rating")

    def get_average_rating(self):
        # Return the averge rating after adding up all the ratings
        len_of_ratings = len(self.ratings)
        total_ratings = 0
        for rating in self.ratings:
            total_ratings = total_ratings + rating
    
        #print("\tNum of ratings {} and total ratings {} for {}".format(len_of_ratings, total_ratings, self.title))
        return total_ratings / len_of_ratings


class Fiction(Book):
    # Extend the Book Class
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def __repr__(self):
        return "{} by {}".format(self.title, self.author)

    # Return the Fiction Books author
    def get_author(self):
        return author

class NonFiction(Book):
    # Extend the Book Class to Non Fictions
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def __repr__(self):
        return "{}, a {} manual on {}".format(self.title, self.level, self.subject)

    def get_subject(self):
        # Return the NonFiction subject
        return self.subject

    def get_level(self):
        # get the Non Fiction books reading level
        return self.level


class TomeRater():
    def __init__(self):
        self.users = {}
        self.books = {}
        self.isbns = {}
    
    def __repr__(self):
        return "\t**User {},  books {}**\n".format(self.users, self.books)

    def add_isbn(self, isbn):
        #  Help method to keep track of the isbn's to see if they are unique
        # IF it's more than 1 it's a dup
        if isbn in self.isbns:
            self.isbns[isbn] += 1
        else:
            self.isbns[isbn] = 1

    def create_book(self, title, isbn):
        # Call add_isbn so we don't dup isbn's
        # Check if it's unique
        # Create the Book object
        TomeRater.add_isbn(self, isbn)
        TomeRater.unique_isbn(self, isbn)
        B = Book(title, isbn)
        return B
 
    def create_novel(self, title, author, isbn):
        # Same for Novels
        TomeRater.add_isbn(self, isbn)
        TomeRater.unique_isbn(self, isbn)
        F = Fiction(title, author, isbn)
        return F

    def create_non_fiction(self, title, subject, level, isbn):
        # same for non-fictions
        TomeRater.add_isbn(self, isbn)
        TomeRater.unique_isbn(self, isbn)
        NF = NonFiction(title, subject, level, isbn)
        return NF

    def add_book_to_user(self, book, email, rating = None):
        # Check if the key exists for the user email
        # if so mark that the user read it
        # record the user rating of the book
        # add to books and increment if it exists
        #print("\tDEBUG:ABTU: {} {} {}".format(book, email, rating))
        if email in self.users.keys():
            # Call Read Book
            #print("\tDEBUG: Read book {}".format(book.title))
            self.users[email].read_book(book, rating)            
            # Add Rating
            book.add_rating(rating)
            # add the key book to self.books
            if book in self.books.keys():
                self.books[book] += 1
            else:
                self.books[book] = 1

            #if book in self.books.keys():
            #    self.books[book.title] += 1
            #else:
            #    self.books[book.title] = 1
        else:    
            print("\tNo user with email {}!".format(email))       

    def duplicate_email(self, input_email):
        # check for dup email and print message
        for existing_email in self.users:
            if existing_email == input_email:
                print("\tEmail already exists.")

    def unique_isbn(self, isbn):
        # check the isbns hash and see if it's more than 1
        if self.isbns[isbn] > 1:
            print("\tNON unique isbn")

    def validate_email(email):
        # check for the @ symbol for valid email
        # then check if the domains are what we accept
        if '@' not in email:
            print("@ is not in email {}".format(email))
        domain = email.split('@')
        dot = domain[1].split('.')[1]
        to_check=['com', 'edu', 'org']
        for check in to_check:
            if check in dot:
                return True
        return False

    def add_user(self, name, email, user_books = None):
        # Add user to our app
        # check for dup email
        TomeRater.duplicate_email(self, email)
        if not TomeRater.validate_email(email):
            print("\tEmail is not valid format")
        user_object = User(name, email)
        self.users[email] = user_object 
       
        # Add all the books that the user read
        if user_books is not None:
            for book in user_books:
                #print('add book to user')
                TomeRater.add_book_to_user(self, book, email)

    def print_catalog(self):
        # Print out the catalot
        for key in self.books:
            print("\t{}".format(key.title))

    def print_users(self):
        # Print out the users
        for user in self.users:
            print("\t{}".format(user))

    def get_most_read_book(self):
        # get the max value and return the key for the largest value
        most_read = max(self.books, key=self.books.get)
        return ("\t{}".format(most_read.title))

    def highest_rated_book(self):
        # Get the averate rating for each book a put it in a dictionary
        highest_rated_book = {}
        for book in self.books:
            #print('book {}'.format(book.title))
            rating = book.get_average_rating()
            highest_rated_book[book.title] = rating
            #print('Book {}, Rating {}'.format(book.title, rating))
        # get the key for the largest dictionary value
        hrb = max(highest_rated_book, key=highest_rated_book.get)
        return ('\t{}'.format(hrb))

    def most_positive_user(self):
        # Find the user with the most positive ratings
        # Put the avg value in a dictionary
        mpu = {}
        for user in self.users:
            rating = self.users[user].get_average_rating()
            mpu[user] = rating
            #print('User {}, Rating {}'.format(user, rating))
        # return the key from the largest value
        rmpu = max(mpu, key=mpu.get)
        return ('\t{}'.format(rmpu))

