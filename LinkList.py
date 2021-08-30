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
    
    def append(self,node=None):
        
        if self.head is None:
            self.head=node
            return
        
        temp=self.head
        while temp.next:
            temp=temp.next 
        
        temp.next=node
        return 
        
    
    
    def prepend(self,node=None):
        
        if self.head is None:
            self.head=node
            return
        else:
            node.next=self.head
            self.head=node
            return 
    
            
    def insert_after_node(self, prev_node, node):
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
         
        temp_node=self.head
         
        while temp_node is not None:
            print(temp_node.data)
            temp_node=temp_node.next
            
             
         
        
a=LinkedList()  
a.append(node=Node("Mon"))
a.append(node=Node("Tue"))
a.append(node=Node("Wed"))
a.append(node=Node("Thu"))

a.prepend(node=Node("Sun"))

a.insert_after_node(prev_node=a.head.next.next,node=Node("Foo"))

#a.printList()

a.delete_node(val="Foo")
