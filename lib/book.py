class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, count):
        if isinstance(count, int):
            self._page_count = count
        else:
            raise ValueError("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")


if __name__ == "__main__":
    book = Book("And Then There Were None", 272)
    print(book.page_count)  
    book.page_count = "not an integer" 
    book.page_count = 300
    print(book.page_count)  
    book.turn_page() 
