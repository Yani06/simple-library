import json
import time
from Library import Library
from Book import Book
DATA_PATH = './data/books.json'

def main ():

  # Start timer execution
  start = time.time()

  # Read static data from json file (10 books)
  with open(DATA_PATH) as json_file:
    jsonBookList = json.load(json_file)
    # Create book objects 
    library = Library([])
    for book in jsonBookList:
      b =Book(book['isbn'], book['title'], book['summary'], book['author'])
      library.addBook(b)

  # create new Library with books
  book = Book(isbn= "319069696-F", title = "New title",  summary=" it's about the New Title", author= "author")
  
  print('\n****************** Welcome to our Library :) *****************\n')
  print("\n******************************************************************\n")

  # Add a new book to the library
  library.addBook(book)

  # Count of book in the library
  print(library.__str__())
  
  # Get all books from library
  library.getBookList()

  # Start timer execution
  end = time.time()
  print("Executed in %ss  ...%s" %(round(end-start, 2),"Bye !"))


# Run all
main()


