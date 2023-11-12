class Employee:
    def __init__(self):
        self.pan = ""
        self.name = ""
        self.tax = 0
        self.incometax = 0

    def input(self):
        self.pan = input("Enter PAN Number: ")
        self.name = input("Enter Name: ")
        self.tax = float(input("Enter Annual Taxable Income: "))

    def calc(self):
        if self.tax <= 100000:
            self.incometax = 0
        elif 100001 <= self.tax <= 150000:
            self.incometax = (self.tax - 100000) * 0.10
        elif 150001 <= self.tax <= 250000:
            self.incometax = 5000 + (self.tax - 150000) * 0.20
        else:
            self.incometax = 25000 + (self.tax - 250000) * 0.30

    def display(self):
        print("\nEmployee Details:")
        print("PAN Number:", self.pan)
        print("Name:", self.name)
        print("Taxable Income:", self.tax)
        print("Income Tax:", self.incometax)


if __name__ == "__main":
    emp = Employee()
    emp.input()
    emp.calc()
    emp.display()
