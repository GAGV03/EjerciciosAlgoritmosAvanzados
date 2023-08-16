from math import sqrt
from turtle import done, fd, rt, pensize, fillcolor,pencolor,circle, lt, speed

PHI = 2 / (sqrt(5) - 1)

def square(size):
    for _ in range(4):
        fd(size)
        lt(90)

def golden_spiral(n):
    size = 5
    for _ in range(n):
        pencolor("blue")
        square(size)
        pencolor("yellow")
        circle(size, 90)
        size *= PHI 
        
def print_fibonacci(n):
    a = 2
    b = 7
    
    for _ in range(n):
        r = b / a
        print(f'{a:15}{b:15}{r:20.16}')
        a, b = b, a + b
        
print_fibonacci(40)        
pensize(3) 
speed('fastest')       
golden_spiral(9)
done()

