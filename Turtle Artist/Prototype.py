import random
import turtle

turtle.stamp()

moveAmount = int(input("Enter the amount of moves \
you would like your Turtle Artist to make: "))



for i in range(moveAmount):
    turtle.right(random.randint(1,51)) #<-- For circles.
    turtle.forward(random.randint(1,101))
    turtle.stamp() #Do you collect stamps?

input("Press any button to exit.")

#Turtle bounce off the edge mechanic.
#Input preference, square, circle, etc.
#Print/Save image.

