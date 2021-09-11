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
        
            


  def prepend():
    pass
  
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
    
if __name__=="__main__":
    print ("__main__"*10)
    cir=CircularLinkList()
    cir.append(1)
    cir.append(2)
    cir.append(3)
    cir.print_list()
