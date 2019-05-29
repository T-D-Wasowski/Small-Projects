import turtle
import random

moves = 300

for i in range(moves):
    #turtle.stamp()
    turtle.right(random.randint(1,11))
    turtle.forward(random.randint(1,21))

turtle.done()
