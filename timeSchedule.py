import os
from turtle import *

a=input("for adding data type ---> 'add' for seeing the result type ---> 'plot' \n")
if(a=="add"):
    exists = os.path.isfile('/home/mohi/Desktop/data.txt')
    if exists:
        pass
    else:
        f= open("data.txt","w+")
        f.close()

    f = open("data.txt")
    lines = f.readlines()
    f.close()
    if(len(lines)>=31):
        print("you have completed you period ! ****congrats****")
        print("if you want to start a new period enter ---> yes ")
        print("****attention**** ")
        print("if enter 'yes' all the previous results will be deleted ")
        print("if you want to see your result again enter ---> plot")
        new = input()
        if(new == "yes"):
            os.remove("data.txt")
            print("start the programm again.")
        elif(new == "plot"):
            print("restart the program")
            exit()
        else:
            print("you entered wrong charectars .restart the Program.")

    else:

        print("enter you data in shape of zeros and ones : ")
        data = ""
        for i in range(0,48):
            print("your %s data is :"%str(i+1))
            a = input()
            data += a

        print(data)
        f = open("data.txt", "a+")
        f.write(data)
        f.write("\n")

elif(a=="plot"):
    f = open("data.txt")
    lines = f.readlines()
    f.close()

    t = Turtle()
    wn = Screen()
    wn.setup(1200,1200)
    t.speed('fastest')
    t.hideturtle()
    t.pencolor("white")
    t.penup()
    t.goto(-500,250)
    t.pendown()
    box_size = 20
    for row in range(len(lines)):
        for col in range(len(lines[row])-1):
            t.goto(-500+box_size*(col+1),250-box_size*(row))
            if(int(lines[row][col])==0):
                t.fillcolor("black")
                t.begin_fill()
                for i in range(0,4):
                    t.forward(box_size)
                    t.left(90)

                t.end_fill()
                t.penup()
                t.pendown()
            else:
                t.fillcolor("white")
                t.begin_fill()

                for i in range(0,4):
                    t.forward(box_size)
                    t.left(90)
                t.end_fill()
                t.penup()
                t.pendown()
    t.hideturtle()

    ts = t.getscreen()
    ts.getcanvas().postscript(file="result.jpg.eps")
    t.hideturtle()
    wn.exitonclick()
else:
    print("you entered wrong charectars .restar the Program.")
