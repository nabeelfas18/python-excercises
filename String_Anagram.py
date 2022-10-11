def anagram():
    print("Enter The String")
    str=input()
    l1=list(str)
    l2=[]
    l3=[]
    for i in l1:
        for j in l1:
            if(i==j):
                continue
            l2.append(i)
            l2.append(j)
            for k in l1:
                if(i==k):
                 continue
                elif(j==k):
                  continue
                else:
                  l2.append(k)
    n=len(str)
    for i in range(0, len(l2), n):
     l3.append(''.join(l2[i:i+n]))
    
    print(l3)
               
anagram()
            
