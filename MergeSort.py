##Not DONE COMPLETELY
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
    
 
#mergeSortedList(a=[2,5,10],b=[3,6,9,13,14,45])    



def mergeSort(array=[],left=None,right=None):
    n=len(array)
    
    if n < 2 :
        return 
    
    #Get mid point 
    mid=int(n/2)
    print(n,mid)
    leftArray=array[:mid]
    rightArray=array[mid:]
    print("===============")
   
    print("left ::"+ str(leftArray))
    
    print("right ::"+ str(rightArray))
    print("===============")
    mergeSort(leftArray,left=True)
    mergeSort(rightArray,right=True)


mergeSort(array=[2,5,10,3,6,9,13,14,45])    
    
