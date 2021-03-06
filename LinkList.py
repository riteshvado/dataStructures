class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
        
class LinkedList:
    def __init__(self):
        self.head=None
    
    def printList(self):
        temp=self.head
        while temp.next:
            print(temp.data)
            temp=temp.next
        
        #Last node
        if temp.next is None:
            print(temp.data)
            
    def printListRecurse(self,node=None):
        if node is not None:
            print(node.data)
            self.printListRecurse(node=node.next)
            
    
    def countItemstRecurse(self,node=None,first=1):
        if first == 1:
            node=self.head
            
        if node is not None:
            print (node.next,1)
            return 1 + self.countItemstRecurse(node=node.next,first=0)
        else:
            return 0
    
    def append(self,node=None):
        """
        Adding node at the end
        """
        
        if self.head is None:
            self.head=node
            return
        
        temp=self.head
        while temp.next:
            temp=temp.next 
        
        temp.next=node
        return 
        
    
    
    def prepend(self,node=None):
        """
        Adding node at the beginning 
        """
        if self.head is None:
            self.head=node
            return
        else:
            node.next=self.head
            self.head=node
            return 
    
            
    def insert_after_node(self, prev_node, node):
        """
        Inserting after particular node.
        prev_node is existing node  you want to locate and insert a new node after it.
        node : New node we want to insert
        """
        if prev_node is None: 
            print("Error : Prev node is None")
            return 
        
        #save prev_node.next 
        #insert node is D.
        #B is the prev node 
        #A-->B-->C
        
        ##Saving B-->next 
        prev_next=prev_node.next
        
        ##Replace prev_node next to a new node we are inserting. 
        #making B->next == D
        prev_node.next=node
        
        #Setting prev_next to inserted node. 
        #making D->next to C (which earlier was in B->next)
        node.next=prev_next

    def delete_node(self, val=None):
        """
        Delete a node.
        """
        temp_node=self.head
        prev=None 
        while temp_node is not None:
            #print(temp_node.data)
           
            if temp_node.data == val:
                print("--Found prev and current node",prev,temp_node,prev.data)
                prev.next=temp_node.next
                return 
            else:
                prev=temp_node
                temp_node=temp_node.next
            
    
    def swap_nodes(self,val1=None,val2=None):
        """
        Swapping 2 nodes based on values
        """
        
        if val1== val2:
            return 
        
        prev1=None
        curr1=self.head
        
        ##Identifying prev and current node for val1 
        while curr1 and curr1.data != val1:
            print("|"* 10)
            print(curr1.data)
            prev1=curr1
            curr1=curr1.next 
        
        
        
                
            
        ##Identifying prev and current node for val2 
        prev2=None
        curr2=self.head
        
        while curr2 and curr2.data != val2:
            print("*"*10)
           # print(curr2.data)
            prev2=curr2
            curr2=curr2.next     
        
        
        
        
        if prev1:
            print(prev1.data,curr1.data)
            prev1.next=curr2.next
        else:
            print(prev1,curr1.data)
            self.head=curr2
            
            
        if prev2:
            print(prev2.data,curr2.data)
            prev2.next=curr1
        else:
            print(prev2,curr2.data)
            self.head=curr1
        
        
        
        curr1.next,curr2.next=curr2.next,curr1.next 
        
    def get_nth_from_last(self, n):
       """
       This is for finding nth node from tail.
       
       """
       len_total=self.countItemstRecurse()
       remain=len_total-n+1
       curr=self.head 
       count=0
       print(remain)
       while curr:
           count=count+1
           if count == remain:
               return curr
           else:
               curr=curr.next 
               
    
    def count_values(self,val,first=1,node=None):
        """
        Recurive way of verifying how many matching data values are there in linked list. 
        """
        if first == 1:
            node=self.head
        
        if node:
            if node.data == val:
                return 1 + self.count_values(val=val,first=0,node=node.next)
            
            else:
                return 0+self.count_values(val=val,first=0,node=node.next)
        else:
            return 0
            
    def rotate(self,val=None):
        """
        The node we find becomes tail. THe next one becomes head and rest portion gets added to original head.
        If you are rotating last node there is nothing to rotate.
        If you have multiple value match it will rotate on last found.
        """
        curr=self.head
        prev=None
        newTail=None
        newHead=None
        match=False
        while curr:
            if curr.data == val and curr.next is not None:
                match=True
                newTail=curr
                newHead=curr.next
                
            prev=curr
            curr=curr.next
        
        if match:
            print(prev.data,newTail.data,newHead.data,"FFFFFFFFFF")   
            prev.next=self.head
            newTail.next=None
            self.head=newHead
            
            
            
        
   

a=LinkedList()  
a.append(node=Node("Mon"))
a.append(node=Node("Tue"))
a.append(node=Node("Wed"))
a.append(node=Node("Thu"))

a.prepend(node=Node("Sun"))


a.insert_after_node(prev_node=a.head.next.next,node=Node("Foo"))

#a.printList()
a.printList()

a.delete_node(val="Foo")

a.printList()

print("Printing using recursive call ")
a.printListRecurse(node=a.head)
#print(a.countItemstRecurse())
#a.swap_nodes(val1="Sun",val2="Thu")
#print("After Swappppppp")
#a.printListRecurse(node=a.head)

#a.get_nth_from_last(n=3)
#print(a.get_nth_from_last(n=6))

#print(a.count_values(val='Sun'))
print(a.rotate(val='Thu'))
print("*"*20)

a.printListRecurse(node=a.head)
