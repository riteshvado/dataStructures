##Using 2 array pointers
def mergeSortedList(a=[] , b=[]):
    i=0
    j=0 
    k=0
    c=[]
    print(k,i,j)   
    while i < len(a) and j < len(b):
        if a[i]<=b[j]:
            c.append(a[i])
            i=i+1
        elif b[j] < a[i]:
            c.append(b[j])
            j=j+1
        
    print(c,i,j)
    if i < len(a):
        print("we append ")
    elif j < len(b):
        while j < len(b):
            c.append(b[j])
            j=j+1
    
    print(c,i,j)
