class book:
    def __init__(self, title, author):
        self.title = title
        self.book = title
        self.name = title
        self.author = author

class title(book):
    def __init__(self, title, author, genre, id = 0):
        super().__init__(title, author)
        self.genre = genre
        self.id = id

class issue(book):
    def __init__(self, title, author, id, date):
        super().__init__(title, author)
        self.id = id
        self.date = date