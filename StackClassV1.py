# -*- coding: utf-8 -*-
"""
Exercise 10:
    
attributes:
    
    int (maxi): the maximum number of elements accepted in the stack
    list (content): to store the items pushed in the stack
    
methods:
    __init__
    push
    __str__
    __len__
    pop
    peek
    __eq__ (optional)
    
"""
class StackSizeError(Exception):
    pass
class StackFullError(Exception):
    pass
class StackEmptyError(Exception):
    pass

class Stack:
    def __init__(self, maxSz=10): # initialize the 2 attributes (maxi and content)
                               # Does not return anything
        if isinstance(maxSz, int) and maxSz > 0:
            self.maxi=maxSz
        else:
            raise StackSizeError("Wrong size given !!")
            
        self.content=[]
        
    def push(self, item):   # add an item at the end of the inner list
                            # "content" if the stack is not full
                            # Does not return anything
        if len(self.content)<self.maxi:
            self.content.append(item)
        else:
           raise StackFullError("Stack is full!")
            
    def __str__(self):      # Construct and return a string representing the
                            # stack
        return f"({len(self.content)}/{self.maxi}) {self.content}"
    
    def __len__(self):      # Return the current size of the inner list "content"
        return len(self.content)
    
    def pop(self):          # Remove and return the last element of the inner
                            # list "content" if content is not empty
        if len(self.content)>0:
            return self.content.pop()
        else:
            raise StackEmptyError("Stack is empty!")
        
    def peek(self):         # Return the last element of the inner
                            # list "content" if content is not empty
        if len(self.content)>0:
            return self.content[-1]
        else:
            raise StackEmptyError("Stack is empty!")
            
        
    def __eq__(self, other):# Return a bool: True if the self == other False if not
        return self.maxi == other.maxi and self.content == other.content


if __name__ == "__main__":
    s2=Stack(3)
    s2.pop()
    s2.push(200)
    s2.push(300)
    print(s2) # (2/4) [200,300]
    s2.push(56)
    s2.push(99)
    
    
    try:
        s1=Stack(3)

        s1.push(200)
        s1.push(300)
        print(s1) # (2/4) [200,300]
        s1.push(56)
        s1.push(99)
        # s1.push(56) # Error should be reported: the stack is full
        print(s1) # (4/4) [200,300,56,99]
        
        print(f"Size of s1 {len(s1)}") # s1.__len__()
        
        top=s1.pop()
        print(top) # 99
        print(s1) # (3/4) [200,300,56]
        top=s1.pop()
        print(top) # 56
        print(s1) # (2/4) [200,300]
        top=s1.peek()
        print(top) # 300
        print(s1) # (2/4) [200,300]
        top=s1.peek()
        print(top) # 300
        print(s1) # (2/4) [200,300]

        s2=Stack(4)
        s2.push(200)
        s2.push(300)
        
        print(s1==s2)
    except StackSizeError as ex:
        print(f"Exception received: {ex} !!")
    except StackFullError as ex:
        print(f"Exception received: {ex} !!")
    except StackEmptyError as ex:
        print(f"Exception received: {ex} !!")








