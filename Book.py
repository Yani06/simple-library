
class Book:
  """ Book class """

  def __init__(self, isbn, title, summary, author ):
    """
    parmeters:
    -----------
    isbn: str
      book isbn
    title: str
      book title
    summary
      book description
    author
      book author's  
    """
    self.isbn = isbn 
    self.title = title
    self.summary =summary
    self.author = author

  def __str__(self):
     return "ISBN: %s \nBook title: %s \nBook summaury %s \nAuthor: %s"  %(self.isbn, self.title, self.summary, self.author)