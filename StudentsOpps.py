class student:
    def __init__(self):
        self.rollno=""
        self.student_name=""
    def get_data(self):
       print("Enter The Rollnumber")
       self.rollno=input()
       print("Enter The Name")
       self.student_name=input()

    def print_data(self):
        print(self.rollno,self.student_name)

class marks(student):
    def __init__(self):
        
        self.maths=""
        self.python=""
        self.java=""
        self.c=""
        self.cpp=""
        self.php=""
    def get_data(self):
          super().get_data()
          print("Enter The Maths Mark")
          self.maths=input()
          print("Enter The Python Mark")
          self.python=input()
          print("Enter The Java Mark")
          self.java=input()
          print("Enter The C Mark")
          self.c=input()
          print("Enter The CPP Mark")
          self.cpp=input()
          print("Enter The PHP Mark")
          self.php=input()
    def print_data(self):
        super().print_data()
        dict1={"Maths":self.python,"Python":self.python,"Java":self.python,"C":self.c,"CPP":self.cpp,"PHP":self.php}
        print(dict1)
        

s2=marks()
s2.get_data()
s2.print_data()
