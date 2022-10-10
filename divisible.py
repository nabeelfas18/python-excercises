
def divisible():
    l=[43,65,52,50,70,85,25]
    l2=[]
    for i in l:
        if(i%5==0):
         l2.append(i)
    print(sorted(l2))
divisible()