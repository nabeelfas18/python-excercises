def student_grade():
 print("enter c,c++,java,python,c#,.Net")
 marks=input()
 total=[int (i) for i in marks.split()]
 average=sum(total)/len(total)
  
 if(average>90 and average>80):
  print("Your Grade Is A")
 elif(average>80 and average>70):
    print("Your Grade Is B")
 elif(average>70 and average>60):
    print("Your Grade is C")
 elif(average>60 and average>50):
    print("your Grade is D")
 else:
    print("fail")
student_grade()
