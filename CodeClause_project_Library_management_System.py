class Library:

    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks

    def displayAvailableBooks(self):
        print()
        print("Available Books:")
        for book in self.availableBooks:
            print(book)

    def lendBook(self, requestedBook):
        if requestedBook in self.availableBooks:
            self.availableBooks.remove(requestedBook)
            print("you have now borrowed a book called ", requestedBook)
        else:
            print("Sorry, The book is not Available in our list.")

    def addbook(self, returnedBook):
        self.availableBooks.append(returnedBook)
        print("you have returned the book, Thank you!")


class Customer:

    def requestBook(self):
        self.book = input("Enter a name of a book you would like to borrow:")
        return self.book

    def returnBook(self):
        self.book = input("Enter a name of a book you would like to return:")
        return self.book


# Class Initialization
library = Library(['The Endgame', 'India’s vaccine Growth story', 'As Good As My Word','Snakes in the Ganga', 'Miracle at Happy Bazar' , 'How the Onion Got Its Layers' , 'The Third Pillar'
                   , 'My Life, My Mission', 'Courts of India', 'The New Delhi Conspiracy', 'Game Changer', 'My Journey', 'The India Way Strategies for an Uncertain World' ,'Lessons Life Taught Me Unknowingly'
                   , 'Midnight in Chernobyl', 'Ayodhya: City of Faith, City of Discord', 'Indian Fiscal Federalism', 'Vivekadeepini' , 'Braille Edition of ‘Exam Warriors','Quality, Accreditation, and Ranking – A Silent Revolution in the Offing in Indian Higher Education'])
customer = Customer()
while 1:
    print("Enter 1 to display the Available Books.")
    print("Enter 2 to request for a book.")
    print("Enter 3 to return a book.")
    print("Enter 4 to exit.")

    userChoice = int(input())
    if userChoice == 1:
        library.displayAvailableBooks()
    elif userChoice == 2:
        requestedBook = customer.requestBook()
        library.lendBook(requestedBook)
    elif userChoice == 3:
        returnedBook = customer.returnBook()
        library.addbook(returnedBook)
    elif userChoice == 4:
        print("Thank you!")
        quit()
