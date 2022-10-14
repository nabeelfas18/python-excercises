class Employee:
    def __init__(self):
        self.employee_id=""
        self.name=""
        self.designation=""
        self.address=""
        self.phonenumber=""
    def get_data(self):
       print("Enter The EmployeeId")
       self.employee_id=input()
       print("Enter The Name")
       self.name=input()
       print("Enter The Designation")
       self.designation=input()
       print("Enter The Address")
       self.address=input()
       print("Enter The phonenumber")
       self.phonenumber=input()
    def put_data(self):
       print("EmployeeId:",self.employee_id,"Name:",self.name,"Designation:",self.designation,"Address:",self.address,"Phonenumber:",self.phonenumber)
class Salary(Employee):
    def __init__(self):
        self.basicpay=0.0
        self.Ta=0.0
        self.hra=0.0
        self.pf=0.0
        self.netpay=0.0
    def get_basicpay(self):
        super().get_data()
        print("Enter The Basic Pay")
        self.basicpay=input()
    def calculate(self):
        self.Ta=float(self.basicpay)*0.15
        self.hra=float(self.basicpay)*0.20
        self.pf=float(self.basicpay)*0.12
        self.netpay=float(self.basicpay)+float(self.Ta)+float(self.hra)+float(self.pf)
    def display(self):
        super().put_data()
        print("Basic Pay",self.basicpay)
        print("TA",self.Ta)
        print("PF",self.pf)
        print("HRA",self.hra)
        print("Net Pay",self.netpay)

S=Salary()
S.get_basicpay()
S.calculate()
S.display()

