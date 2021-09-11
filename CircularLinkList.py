class Node:
  def __init__(self,data):
    self.data=data
    self.next=None


class CircularLinkList:
  """
    
    Circular Link list is a single link list where tail instead of pointing to None points to HEAD
    1--> 2 --> 3--> 4 --> 5 -->|
    ^                          |
    ^--------------------------|
    
  """
  def __init__(self):
    self.head=None
  
  def append(self,data):
    if self.head is None:
        self.head=Node(data)
        self.head.next=self.head
    
    else:
        curr=self.head
        new_node=Node(data)
        ##If current next match head we are at tail. Remember that it is circular list.
        while curr.next != self.head:
            curr=curr.next
        
        ##curr is now at tail. Adding new node to tail 
        curr.next=new_node
        ##making new node as the new tail 
        new_node.next=self.head
        
            


  def prepend(self,data):
      """
      
      """
      if self.head is None:
          self.append(data)
      else:
          
          curr=self.head
          new_node=Node(data)
          #adding head to new node next 
          new_node.next=self.head
          ##Iterating till tail 
          while curr.next != self.head:
              curr=curr.next
          
          #Making new node as head.
          self.head=new_node
          #assign next of tail to new head.
          curr.next=new_node
          
          
            
    
  
  def print_list(self):
      
      if self.head is None:
          return 
      else:
          curr=self.head
          #Print head data first
          print(curr.data) 
          while curr.next != self.head:
              curr=curr.next
              print(curr.data)
  
  def print_list_recursive(self,node=None):
      """
      printing list in recursion
      """
      if self.head is None:
          return
      
      if node is None:
          node=self.head 
          
      if node.next == self.head:
          print (node.data)
          return 
      else:
          print(node.data)
          self.print_list_recursive(node=node.next)
          
          
if __name__=="__main__":
    print ("__main__"*10)
    cir=CircularLinkList()
    cir.append(1)
    cir.append(2)
    cir.append(3)
    cir.print_list()
    print("prepending now")
    cir.prepend(0)
    cir.prepend(-1)
    cir.print_list_recursive()
