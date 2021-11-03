
import atexit

@atexit.register
def f1():
    print("F1 is invoked")

@atexit.register
def f2():
    print("F2 is invoked")

# atexit.register(f1)
# atexit.register(f2)
    
l1=[2,3,4]
l1.append(23)
print(l1)