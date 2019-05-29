import turtle
import random

name = input("Which turtle artist would you like to comission:\n"\
             "Giorgio, Francesco, Antonio or Salvador? - ")

window = turtle.Screen()
artist = turtle.Turtle()
artist.shape("turtle")

#Functions

def giorgio(): #Rectangles
    for i in range(101):
        artist.forward(random.randint(1,100))
        artist.right(90)
    
def francesco(): #Triangles
    for i in range(101):
        artist.forward(random.randint(10,100))
        artist.right(135)

def antonio(): #Circles
    for i in range(301):
        artist.forward(random.randint(5,30))
        artist.right(random.randint(5,10))

def salvador(): #Random??
    for i in range(200):
        artist.forward(random.randint(5,50))
        if random.getrandbits(1) == 1:
            artist.right(random.randint(10,180))
        else:
            artist.left(random.randint(10,180))
            
#If statements

if name == ("Giorgio" or "giorgio" or "G" or "g"):
    giorgio()
    
elif name == ("Francesco" or "francesco" or "F" or "f"):
    francesco()
    
elif name == ("Antonio" or "antonio" or "A" or "a"):
    antonio()
    
elif name == ("Salvador" or "salvador" or "S" or "s"):
    salvador()
    
else:
    print("I do not recognise that artist")     

    
                       
    
    
        



