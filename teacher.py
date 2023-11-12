class Teacher:
    def __init__(self):
        self.name=""
        self.address=""
        self.phone=""
        self.subjectspecialization==""
        self.monthly_salary=0
        self.income_tax=0
    def accept_details(self):
        self.name=input("Enter the teacher's name:-")
        self.address=input("Enter the teacher's address:-")
        self.phone=("Enter the teacher's number:-")
        self.subject_specializaion=("Enter the teacher's subject specialization:-")
        self.monthly_salary=float(input("Enter the teacher's monthly salary:-"))
    def calculate_income_tax(self):
            annual_salary=self.monthly_salary*0.12
    if'annual_salary'>=175000:
        'self'.income_tax='annual_salary'-175000*0.05
    else:
        'self'.income_tax=0
def display_details(self):
        print("\nTeacher Details:")
        print("Name:-",self.name)
        print("address",self.address)
        print("phone",self.phone)
        print("subject specialization",self.subject_specialization)
        print("MOnthly salary",self.monthly_salary)
        print("Income tax",self.income_tax)

if __name__=="__main__":
              teacher=Teacher()
              teacher.accept_details()
              teacher.calculate_income_tax()
              teacher.display_details()
