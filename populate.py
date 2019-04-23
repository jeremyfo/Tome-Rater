from TomeRater import *

def print_menu(menu):
    print("---------------------------------------------------")
    print("\t\t{}".format(menu))
    print("---------------------------------------------------")
    
def main():
    Tome_Rater = TomeRater()

    book1 = Tome_Rater.create_book("Society of Mind 1", 12345678, 9.99)
    book2 = Tome_Rater.create_book("Society of Mind 2", 82345678, 8.00)
    book3 = Tome_Rater.create_book("Society of Mind 3", 72345678, 7.00)
    book4 = Tome_Rater.create_book("Society of Mind 4", 52345678, 12.00)
    book5 = Tome_Rater.create_book("Society of Mind 5", 92345678, 13.00) 

    novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345, 22.00)
    novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010, 21.00)
    novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000, 18.00)
    novel4 = Tome_Rater.create_novel("Life of Pi", "Yan Martel", 70005001, 12.99)
    novel5 = Tome_Rater.create_novel("Life of Pi 1", "Yan Martel", 70005002, 12.99)
    novel6 = Tome_Rater.create_novel("Life of Pi 2", "Yan Martel", 70005003, 12.99)
    novel7 = Tome_Rater.create_novel("Life of Pi 3", "Yan Martel", 70005004, 12.99)
    novel8 = Tome_Rater.create_novel("Life of Pi 4", "Yan Martel", 70005005, 12.99)
    novel9 = Tome_Rater.create_novel("Life of Pi 5", "Yan Martel", 70005006, 12.99)
    novel10 = Tome_Rater.create_novel("Life of Pi 6", "Yan Martel", 70005007, 12.99)
    novel11 = Tome_Rater.create_novel("Life of Pi 7", "Yan Martel", 70005008, 12.99)
    novel12 = Tome_Rater.create_novel("Life of Pi 8", "Yan Martel", 70005009, 12.99)
    novel13 = Tome_Rater.create_novel("Life of Pi 9", "Yan Martel", 70005010, 12.99)
    novel14 = Tome_Rater.create_novel("Life of Pi 10", "Yan Martel", 70005020, 12.99)
    novel15 = Tome_Rater.create_novel("Life of Pi 11", "Yan Martel", 70005030, 12.99)

    nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452, 9.99)
    nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938, 14.55)
    nonfiction3 = Tome_Rater.create_non_fiction("A Programmers Guide to Mathmatics", "Programming", "advanced", 911561938, 25.99)
    nonfiction4 = Tome_Rater.create_non_fiction("Advanced Algorithms", "Programming", "advanced", 611411938, 33.99)

    novel1.set_isbn(9781536831139)

    #Create users:
    Tome_Rater.add_user("Alan Turing", "alan@turing.com")
    Tome_Rater.add_user("David Marr", "david@computation.org")
    Tome_Rater.add_user("Bob Smith", "bsmith@gmail.com")
    Tome_Rater.add_user("Dewey Brown", "dbrown@aol.com")
    Tome_Rater.add_user("Marie Moore", "mmoore@gmail.com")
    Tome_Rater.add_user("Matt Moore", "mmoore@gmail.com") # Should throw an error - duplicate email
    Tome_Rater.add_user("Brandy Adams", "badams@gmail.com")
    Tome_Rater.add_user("Jason Jones", "jjones@gmail.com")
    Tome_Rater.add_user("Nick Branch", "nbranch@gmail.com")
    Tome_Rater.add_user("Lucian Hooper","ipsum.dolor.sit@convallis.edu")
    Tome_Rater.add_user("Duncan Solomon","Integer.id.magna@gravidanuncsed.org")
    Tome_Rater.add_user("Blaine Watson","urna@mauris.edu")
    Tome_Rater.add_user("Teegan Moran","et.euismod@Nuncsed.org")
    Tome_Rater.add_user("Cally Parks","montes.nascetur@elit.org")
    Tome_Rater.add_user("Maia Lara","Ut.semper@neque.net")
    Tome_Rater.add_user("Inga Hurst","ac.mattis.semper@pretiumneque.edu")
    Tome_Rater.add_user("Marah Sears","sem.mollis@necanteMaecenas.edu")
    Tome_Rater.add_user("Quintessa Gutierrez","sed.libero@loremtristiquealiquet.com", user_books=[book1, book2, book3, book4, book5])
    Tome_Rater.add_user("Kenneth Hampton","lacus@inceptoshymenaeosMauris.com", user_books=[nonfiction1, nonfiction2, nonfiction3, nonfiction4])
    Tome_Rater.add_user("Yasir Wilson","vel.lectus@InfaucibusMorbi.org", user_books=[novel13, novel14, novel15])
    Tome_Rater.add_user("Cullen Wade","tincidunt.aliquam.arcu@lorem.org", user_books=[novel10, novel11, novel12, novel13])

    #Add a user with three books already read:
    Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])

    #Add books to a user one by one, with ratings:
    Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
    Tome_Rater.add_book_to_user(book2, "alan@turing.com", 1)
    Tome_Rater.add_book_to_user(book3, "alan@turing.com", 1)
    Tome_Rater.add_book_to_user(book4, "alan@turing.com", 1)
    Tome_Rater.add_book_to_user(book5, "alan@turing.com", 3) 

    Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
    Tome_Rater.add_book_to_user(novel2, "alan@turing.com", 3)
    Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 3)
    Tome_Rater.add_book_to_user(novel4, "alan@turing.com", 3)

    Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 4)
    Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
    Tome_Rater.add_book_to_user(nonfiction3, "alan@turing.com", 4)
    Tome_Rater.add_book_to_user(nonfiction4, "alan@turing.com", 4)

    Tome_Rater.add_book_to_user(book1, "bsmith@gmail.com", 1)
    Tome_Rater.add_book_to_user(book2, "bsmith@gmail.com", 2)
    Tome_Rater.add_book_to_user(book3, "bsmith@gmail.com", 3)
    Tome_Rater.add_book_to_user(book4, "bsmith@gmail.com", 4)

    Tome_Rater.add_book_to_user(novel1, "dbrown@aol.com", 1)
    Tome_Rater.add_book_to_user(novel2, "dbrown@aol.com", 2)
    Tome_Rater.add_book_to_user(novel3, "dbrown@aol.com", 3)
    Tome_Rater.add_book_to_user(novel4, "dbrown@aol.com", 4)

    Tome_Rater.add_book_to_user(nonfiction1, "mmoore@gmail.com", 1)
    Tome_Rater.add_book_to_user(nonfiction2, "mmoore@gmail.com", 2)
    Tome_Rater.add_book_to_user(nonfiction3, "mmoore@gmail.com", 3)
    Tome_Rater.add_book_to_user(nonfiction4, "mmoore@gmail.com", 4)
    Tome_Rater.add_book_to_user(novel5, "mmoore@gmail.com", 4)
    Tome_Rater.add_book_to_user(novel6, "mmoore@gmail.com", 3)
    Tome_Rater.add_book_to_user(novel7, "mmoore@gmail.com", 2)
    Tome_Rater.add_book_to_user(novel8, "mmoore@gmail.com", 3)
    Tome_Rater.add_book_to_user(novel9, "mmoore@gmail.com", 1)
    Tome_Rater.add_book_to_user(novel10, "mmoore@gmail.com", 4)

    Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
    Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
    Tome_Rater.add_book_to_user(novel11, "marvin@mit.edu", 2)
    Tome_Rater.add_book_to_user(novel12, "marvin@mit.edu", 2)
    Tome_Rater.add_book_to_user(novel13, "marvin@mit.edu", 2)
    Tome_Rater.add_book_to_user(novel14, "marvin@mit.edu", 2)
    Tome_Rater.add_book_to_user(novel15, "marvin@mit.edu", 2)

    Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)

    print_menu("Catalog")
    Tome_Rater.print_catalog()

    print_menu("Users")
    Tome_Rater.print_users()

    print("---------------------------------------------------")
    print("Most positive user: ")
    print(Tome_Rater.most_positive_user())

    print("---------------------------------------------------")
    print("Highest rated book: ")
    print(Tome_Rater.highest_rated_book())

    print("---------------------------------------------------")
    print("Most read book: ")
    print(Tome_Rater.most_read_book())

    print("---------------------------------------------------")
    print(Tome_Rater)

    print_menu("Get Most Expensive Books")
    Tome_Rater.get_n_most_expensive_books(7)

    print_menu("Get User Worth")
    Tome_Rater.get_worth_of_user("mmoore@gmail.com")
    Tome_Rater.get_worth_of_user("alan@turing.com")
    Tome_Rater.get_worth_of_user("bsmith@gmail.com")

    print_menu("Get Most Read Book")
    Tome_Rater.get_n_most_read_books(5)

    print_menu("Get Most Prolific Reader")
    Tome_Rater.get_n_most_prolific_readers(5)

if __name__ == '__main__':
    main()