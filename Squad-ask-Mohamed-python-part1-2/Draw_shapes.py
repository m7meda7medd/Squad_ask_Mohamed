
import turtle #import turtle library to draw circle
shapes_list=list() # list of shapes

# Draw functions 
def draw_circle(diameter) :
    radius = diameter/2
    t=turtle.Turtle()
    t.circle(radius)

def square(height) :
    for i in range (height) :
         print("* "*height)

def right_triangle(height) :
    for i in range  (1,height+1):
        print("* "*i)

        
def pyramid(height) :
    space = 2*height-1
    for x in range (0 ,height) :
            print(" "*int((space/2)) + "*"*int((2*x+1)) + " "*int((space/2)))
            space-=2


def get_shape() :
    shape= str(input("enter the shape Name from (square,pyramid,right triangle,circle): "))
    height = int(input ("enter the height of the %s : "%shape))
    Store = tuple((shape,height))
    shapes_list.append(Store)
    return Store 

def sort_list () :
    shapes_list.sort(key=lambda item:item[1])





# my algorithm
counter = int(input("enter number of shapes to draw :")) #get number of shapes
while counter >0 :
    x=get_shape() 
    if x[0]== "square" :
        square(x[1])
    elif x[0]== "pyramid" :
        pyramid( x[1])
    elif x[0]== "right triangle" :
        right_triangle(x[1])
    elif x[0]== "circle" :
        draw_circle(x[1])
    else :
        print("invalid")
    counter-=1    
sort_list() 
print(shapes_list)                    




