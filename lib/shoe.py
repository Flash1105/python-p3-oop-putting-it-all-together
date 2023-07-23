class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = size
        self.condition = "New"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, shoe_size):
        if isinstance(shoe_size, int):
            self._size = shoe_size
        else:
            raise ValueError("size must be an integer")

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"



if __name__ == "__main__":
    stan_smith = Shoe("Adidas", 9)
    print(stan_smith.size)  
    stan_smith.size = "not an integer"  
    stan_smith.size = 10
    print(stan_smith.size)  
    stan_smith.cobble()  
    print(stan_smith.condition) 
