def employee_details():
 print("Enter the emplyee Id")
 id=int(input())
 print("Enter the employee name")
 name=input()
 print("Enter the basic pay")
 pay=int(input())

 hra=0
 ta=0
 netpay=0
 if(pay>10000):
  hra=float((pay/15))
  ta=float((pay/8))
 elif(pay>5000 and pay<10000):
  hra=float((pay/100))
  ta=float((pay/100))
 elif(pay<5000):
  hra=float((pay/5))
  ta=float((pay/3))
 netpay=hra+ta+pay 
 print("HRA=",hra)
 print("TA=",ta)
 print("NatPay=",netpay)
employee_details()
