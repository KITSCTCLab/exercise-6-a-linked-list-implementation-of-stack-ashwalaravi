class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Stack:
  def __init__(self):
    self.top = None

  def push(self, data) -> None:
    newnode = Node(data)
    newnode.data=data
    newnode.next = self.head
    self.top = newnode

  def pop(self) -> None:
    # Write your code here
    if self.top==None:
      return None
    else:
      poppednode = self.top
      self.top = self.top.next
      poppednode.next = None
      return poppednode

      
    
  def status(self):
    """
    It prints all the elements of stack.
    """
    # Write your code here 
     if self.top==None:
      print("None")
    else:
      iternode = self.top
      while(iternode != None):
        print(iternode.data, "->", end=" ")
        iternode = iternode.next
        if(itrnode==None):
          print("None")


# Do not change the following code
stack = Stack()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "push":
    stack.push(int(data[i]))
  elif operations[i] == "pop":
    stack.pop()
stack.status()
