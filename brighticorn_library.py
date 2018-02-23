## MAKE BRIGHTICORN'S LIBRARY GOOOOOOOO

# VARIABLES GO HERE
books = []

# MAIN MENU GOES HERE
def call_menu():
    """Continuously calls library menu until user exits"""
    while True:
        print """\nBrighticorn's Library: 
        \nType the command to select an action
        - ADD a Book
        - VIEW Books
        - CHECK for a Book
        - EXIT\n\n"""

        command = raw_input("> ").upper()

        if command == "ADD":
            you_chose(command)
            add_books()
        elif command == "VIEW":
            you_chose(command)
            view_books()
            pass
        elif command == "CHECK":
            you_chose(command)
            check_books()
        elif command == "EXIT":
            break
        else:
            print "You did it wrong, Dave. Try again."

def you_chose(command):
    """ Prints user choice"""
    print "You chose to {}".format(command)

def add_books(book_title=''):
    """ Add the book title that the user wants to the bookshelf """
    
    if len(book_title) == 0:
        book_title = raw_input("What is the title of the book? ").title()

    if book_title in books:
        print "\nThat book is already in the library! Type 'VIEW' to view all library contents"
        return

    books.append(book_title)
    print "\nYou added the book!!"


def view_books():
    """ View the current contents of Brighticorn's Library!!!! YAY """
    for book in books:
        print "- ", book

def check_books():
    """Checks if the the book is in the library :) """

    book_title = raw_input("What is the title of the book? ").title()
    if book_title in books:
        print "\nThat book is already in the library!"
    else:
        print "\nThat book is not in the library!"
        print "\nWould you like to add it? Y/N"
        if raw_input(">").upper() == "Y":
            add_books(book_title)
        else:
            print "\nOk, you can always add it later."

call_menu()