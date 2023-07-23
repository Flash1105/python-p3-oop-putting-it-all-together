#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand =brand
        self.size = size

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

    def set_size(self, value):
        if not isinstance(value, int):
            print("size must be an integar")
        else:
            self.size = value