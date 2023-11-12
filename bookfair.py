class BookFair:
 def __init__(self):
        self_Bname=""
        self.price=0.0
 def input(self):
        self.Bname=input("Enter the name of the book:")
        self.price=float(input("Enter the price of the book:-"))
 def calculate(self):
  if self.price<=1000:
    discount=0.02*self.price
  elif 1000<self.price<=3000:
     discount=0.10*self.price
  else:
    discount=0.15*self.price
  self.discounted_price=self.price-discount
 def display(self):
    print(f"Book name:{self.Bname}")
    print(f"Original price:Rs.{self.price}")
    print(f"discounted price:Rs.{self.discounted_price}")
book=BookFair()
book.input()
book.calculate()
book.display()
