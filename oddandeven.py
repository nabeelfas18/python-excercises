def oddeven():
    oddsum=0
    evensum=0
    for i in range(15,36):
        if(i%2==0):
            evensum+=i
        else:
            oddsum+=i
    print("OddSum",oddsum)
    print("EvenSum",evensum)        
oddeven()  