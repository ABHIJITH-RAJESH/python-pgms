# find the area of a circle
# find the area of cone 

import math
def areacircle():
    r=int(input("enter the radius of circle"))
    return math.pi*pow(r,2)

def areacone():
    r=int(input("enter the radius of cone"))
    h=int(input("enter the height of cone"))
    a=math.pi*pow(r,2)+math.pi*r*h
    return a