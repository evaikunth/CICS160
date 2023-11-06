from Node import Node


class LinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None 
        self.size = 0

    def add(self, item:object):
        newNode = Node(item)
        if(self.size == 0):
            self.head = newNode
            self.tail = newNode
        else:
            curr = self.tail
            self.tail = newNode
            curr.setNext(newNode)
            newNode.setPrevious(curr)
        self.size+=1

    def insert(self,index,item):
        newNode = Node(item)
        curr = self.head
        if(self.size > 0 and index <= self.size):
            if(index == 0):
                self.head = newNode
                curr.setPrevious(newNode)
                newNode.setNext(curr)
            elif(index == self.size):
                curr = self.tail
                self.tail = newNode
                curr.setNext(newNode)
                newNode.setPrevious(curr)
                
            else:
                i = 0
                while(i < index):
                    curr = curr.getNext()
                    i+=1
                curr.getPrevious().setNext(newNode)
                newNode.setPrevious(curr.getPrevious())
                curr.setPrevious(newNode)
                newNode.setNext(curr)
            self.size+=1
    
    def delete(self,index):
        if(self.size > 0 and index < self.size):
            x = 0
            current = self.head
            if(index == 0):
                self.size = self.size - 1
                if(self.size != 0):
                    current.getNext().setPrevious(None)
                    self.head = current.getNext()
                    current.setNext(None)
                else:
                    self.head = None
                    self.tail = None
                    
                    
                
            elif (index == self.size - 1):
                current = self.tail
                current.getPrevious().setNext(None)
                self.tail = current.getPrevious()
                current.setPrevious(None)
                self.size -=1


            else:  
                while (x<index):
                    current = current.getNext()
                    x+=1
                    
                
                current.getPrevious().setNext(current.getNext())
                current.getNext().setPrevious(current.getPrevious())
                self.size = self.size - 1

    def length(self):
        return(self.size)
                    
    
    def __getitem__(self,index):
        x = 0
        curr = self.head
        while (x < index):
            curr = curr.getNext()
            x+=1
        return(curr.getData())





    def __str__(self):
        stringToReturn = "List size: " + str(self.size)
        current = self.head
        while (current is not None):  
            stringToReturn = stringToReturn + "\n\n" + str(current)
            current = current.getNext()
        return(stringToReturn)
    
if __name__ == "__main__":
    l = LinkedList()
    l.add(11)
    l.add(17)
    l.add(12)
    print(l)
    l.insert(3,15)
    print(l)
