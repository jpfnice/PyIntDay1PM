class Point:
    counter=0 # class attribute
    
    def __init__(self, vx, vy):
        
        Point.counter += 1
        self.__x=vx   # attribute x is defined here
        self.__y=vy   # attribute y is defined here
    
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

    def setX(self, val):
        if isinstance(val, (int, float)):
            self.__x=val
        else:
            raise Exception("Invalid value")
    def getX(self):
        return self.__x

    x=property(getX, setX)
    
    def setY(self, val):
        if isinstance(val, int):
            self.__y=val
        else:
            raise Exception("Invalid value")
    def getY(self): # instance method
        return self.__y

    y=property(getY, setY)
    
    def parsePoint(text): # class method
        import re
        mo=re.match(r"<(\d+),(\d+)>", text)
        if mo:
            vx=int(mo[1])
            vy=int(mo[2])
            return Point(vx, vy)
        else:
            raise Exception(f"Wrong string format {text}")
    
    parsePoint=staticmethod(parsePoint)
    
    # def parsePoint(cls, text): # class method
    #     import re
    #     mo=re.match(r"<(\d+),(\d+)>", text)
    #     if mo:
    #         vx=int(mo[1])
    #         vy=int(mo[2])
    #         return Point(vx, vy)
    #     else:
    #         raise Exception(f"Wrong string format {text}")
    
    # parsePoint=classmethod(parsePoint)
    


p3=Point.parsePoint("<23,56>")
print(p3, type(p3))





