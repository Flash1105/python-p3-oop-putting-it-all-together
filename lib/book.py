#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
        
    def set_page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self.page_counter = value