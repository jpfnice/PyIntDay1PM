class Point:
    counter=0 # A class variable or class attribute
    
    def __init__(self, vx, vy):
        self.__x=vx   # attribute x is defined here
        self.__y=vy   # attribute y is defined here
        Point.counter += 1
    
    def __del__(self):
        Point.counter -= 1
        
    def __str__(self):
        return f"<{self.__x},{self.__y}>"
    
    def __add__(self, other):
        return Point(self.__x+other.__x, self.__y+other.__y)
    
    def distance(self, other):
        import math
        return math.sqrt((other.__x-self.__x)**2 + (other.__y-self.__y)**2)
    
    def clear(self):
        self.__x=self.__y=0

    @property  # x=property(x)
    def x(self):
        return self.__x
    
    @x.setter # x=x.setter(x)
    def x(self, val):
        if isinstance(val, (int, float)):
            self.__x=val
        else:
            raise Exception("Invalid value")
    
    @property  # y=property(y)
    def y(self): # instance method
        return self.__y
    
    @y.setter  #y.setter(y)
    def y(self, val):
        if isinstance(val, int):
            self.__y=val
        else:
            raise Exception("Invalid value")
    
    @classmethod  # a decorator
    def parsePoint(cls, text): # class method
        import re
        mo=re.match(r"<(\d+),(\d+)>", text)
        if mo:
            vx=int(mo[1])
            vy=int(mo[2])
            return Point(vx, vy)
        else:
            raise Exception(f"Wrong string format {text}")
    
   
print("Counter: ", Point.counter)    
p1=Point(0,0)

p1.x=35

p1.y=67

print(p1)

p3=Point.parsePoint("<34,56>")

print(p3.x, "--", p3.y)
print("Counter: ", Point.counter)  

del p1
print("Counter: ", Point.counter) 






