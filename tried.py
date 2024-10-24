# Question 1(i)
# Write a Python program to find the distance between two coordinate points (x1, y1) and (x2, y2). distance= sqrt of 
# (x2-x1)** +(y2-y1)**
import math
def distance():
    
    num_x1=input("Enter the distance x1\t")
    num_y1=input("Enter the distance for y1")
    num_x2=input("Enter the distance for x2")
    num_y2=input("Enter the distace for y2")
    distance=math.sqrt((num_x2-num_x1) + (num_y2-num_y1))
    print(distance)
    print(f"The distance between two coordinate points {num_x1,num_y1} and {num_x2,num_y2} is{distance} ")
distance()


