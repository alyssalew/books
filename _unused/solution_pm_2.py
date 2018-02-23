#### THIS VERSION IS NOT CURRENTLY USED, BUT MIGHT HAVE SOME USEFUL
#### CODE FOR FURTHER-FURTHER-STUDY

def get_command():
    """Show menu and get command. Returns command."""

    print "You can: add / view / check / update / exit" 

    command = raw_input("action > ")
    command = command.lower()

    print "Action:", command

    return command


def add_book(books, authors):
    """Add new book. Returns new title."""

    print "Add Book"

    book = raw_input("Title > ")
    author = raw_input("Author > ")

    books.append(book)
    authors.append(author)

    return book


def view_books(books, authors):
    """View all books."""

    print "View Books"

    index = 0

    while index < len(books):
        print index, books[index], "by", authors[index]
        index = index + 1

    print "End of listing"


def check_book(books):
    """Search for a book. Returns title if so, or None if not."""

    print "Check for a Book"

    to_check = raw_input("Title > ")
    to_check = to_check.lower()

    for book in books:
        if to_check in book.lower():
            return book


def update_book(books, authors):
    """Update book in library. Returns status message."""

    print "Update Books"

    # First, list the books
    view_books(books, authors)

    book_index = int(raw_input("Book # to change > "))

    book = raw_input("Title > ")
    author = raw_input("Author > ")

    prev_title = books[book_index]

    books[book_index] = book
    authors[book_index] = author

    return prev_title


def library():
    """Main loop."""

    books = ["Dune", "Pride and Prejudice"]
    authors = ["Frank Herbert", "Jane Austen"]

    print "Brighticorn's Books"
    print "-------------------"

    while True:

        command = get_command()

        if command == "exit":
            print "Goodbye!"
            break

        elif command == "add":
            book = add_book(books, authors)
            print "Added", book 

        elif command == "view":
            view_books(books, authors)

        elif command == "check":
            found = check_book(books)
            print "Found:", found

        elif command == "update":
            prev_title = update_book(books, authors)

            print "Replaced", prev_title

        else:
            print "Sorry, that's not an option"


library()

