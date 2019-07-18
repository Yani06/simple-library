
from Book import Book
class Library:
  """ Library class """

  def __init__(self, books: [Book]):
    """
    parmeters:
    -----------
    books: [Book]
      list of book
    """
    self.books = books


  def __str__(self):
     return "There is  %s " %(len(self.books))+ " books.\n" 
   
  def addBook(self, book: Book):
    """
      Add a new book to the library
      return self list
    """
    return self.books.append(book)

  def getBookList(self):
    """
      Get all books of the library
    """
    i=1
    for book in self.books:
      print("******** Livre N° %s ************\nISBN: %s, \nTitle: %s \nSummary: %s \nAuthor: %s" %(i, book.isbn, book.title, book.summary, book.author),"\n**********************************\n")
      i += 1


