
class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f'{self.title} by {self.author}'

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return f'{self.num_pages + other.num_pages} pages'

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f'Key {key} is not a valid key'


book1 = Book('My first book', 'Ooga', 100)
book2 = Book('My first book', 'Ooga', 300)
book3 = Book('My third book', 'Googa', 300)

print(book1)
print(book1 == book2)
print(book1 < book3)
print(book1 > book3)
print(book2 + book3)
print('third' in book2)
print('third' in book3)
print(book2['title'])
print(book2['author'])
print(book2['num_pages'])