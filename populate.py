from TomeRater import *

import sys
Tome_Rater = TomeRater()

#Create some books:
print("POP: Create books, novels and non_fictions")
book1 = Tome_Rater.create_book("Society of Mind", 12345678)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)

#os.exit(0)

#Create users:
print("POP: Create some users")
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")

#Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])

#Add books to a user one by one, with ratings:
print("POP: Add books to users")
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)


#Uncomment these to test your functions:
print("POP: print catalogs")
Tome_Rater.print_catalog()
#
print("POP: print users")
Tome_Rater.print_users()
#
print("POP: Most read book:")
print(Tome_Rater.get_most_read_book())

#
print("POP: Highest rated book:")
print(Tome_Rater.highest_rated_book())

print("POP: Most positive user:")
print(Tome_Rater.most_positive_user())


# Test __eq__ in User

print("POP: Test EQ User method, should be different")
marvin = Tome_Rater.users['marvin@mit.edu']
david  = Tome_Rater.users['david@computation.org']
if marvin == david:
    print('\tmarvin and david are the same user')
else:
    print('\tmarvin and david are not the same user')

# change david's email and name to match Marvins
print("POP: Test EQ User method, should be the same after changing email and user")
david.change_email('marvin@mit.edu')
david.change_name('Marvin Minsky')
if marvin == david:
    print('\tmarvin and david are the same user')
else:
    print('\tmarvin and david are not the same user')
    
