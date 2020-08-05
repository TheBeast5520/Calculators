from turtle import *
canvas = Screen()
canvas.setup(250,450,0,0)
draw = Turtle()
draw.speed("fastest")
draw.penup()
draw.goto(-100,-200)
draw.pendown()
for i in range(9):
    draw.forward(200)
    draw.penup()
    draw.goto(draw.xcor()-200,draw.ycor()+50)
    draw.pendown()
draw.penup()
draw.goto(100,-200)
draw.left(90)
draw.pendown()
draw.forward(50)
for i in range(4):
    draw.forward(6*50)
    draw.penup()
    draw.goto(draw.xcor()-50,draw.ycor()-6*50)
    draw.pendown()
draw.goto(draw.xcor(),draw.ycor()+6*50)
draw.forward(50)
draw.right(90)
draw.forward(200)
draw.right(90)
draw.forward(50)
draw.penup()
draw.goto(-100,-150)
draw.pendown()
draw.forward(50)
draw.hideturtle()
button = Turtle()
button.speed("fastest")
button.penup()
number = 9
button.goto(25,10)
for i in range(3):
    for j in range(3):
        button.write(number,align="center",font=("arial",16,"normal"))
        button.goto(button.xcor()-50,button.ycor())
        number += -1
    button.goto(button.xcor()+150,button.ycor()-50)
button.goto(button.xcor()-50,button.ycor())
button.write("0",align = "center",font=("arial",16,"normal"))
button.goto(button.xcor()-50,button.ycor()+250)
functions = ["x (mod y)", "Log_x (y)", "xⁿ", "ⁿ√x", "π", "e", "%", "."]
fontsizes = [8,8,16,16,16,16,16,16]
m=0
n=0
for i in range(2):
    for j in range(4):
        button.write(functions[m],align = "center", font = ("arial",fontsizes[n],"normal"))
        button.goto(button.xcor()+50,button.ycor())
        m += 1
        n += 1
    button.goto(button.xcor()-200,button.ycor()-50)
bFunctions = ["÷", "×", "−", "+"]
m=0
button.goto(button.xcor()+3*50, button.ycor())
for i in range(4):
    button.write(bFunctions[m], align = "center", font = ("arial", 20, "normal"))
    button.goto(button.xcor(),button.ycor()-50)
    m += 1
button.goto(button.xcor()-3*50,button.ycor()+50)
button.write("CE", align = "center", font = ("arial",16,"normal"))
button.forward(100)
button.write("AC", align = "center", font = ("arial",16,"normal"))
button.goto(button.xcor()-25, button.ycor()-60)
button.write("=", align = "center", font = ("arial",30,"normal"))
button.hideturtle()
# graphics are complete!
write = Turtle()
write.penup()
write.goto(90,160)
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def division(x,y):
    return x/y
def x_mod_y(x,y):
    return x%y
import math
def log_x_y(x,y):
    return math.log(y,x)
def x_to_the_nth_power(x,y):
    return x**y
def x_to_the_nth_root(x,y):
    return x**(1/y)
def percent(x):
    return x/100
# calculating functions completed!
write.hideturtle()
a = ''
b = ''
counter = 0
function = ''
def button_1(x,y):
    global a
    global b
    global counter
    global function
    if x > -100 and x < -50 and y > -100 and y < -50:
        if counter == 0:
            if len(a)<12:
                a = a+"1"
                write.clear()
                write.write(a,align="right",font=("arial",20,"normal"))
        elif counter == 1:
            if len(b)<12:
                b = b+"1"
                write.clear()
                write.write(b,align="right",font=("arial",20,"normal"))
        elif counter ==2:
            a = '1'
            b = ''
            counter = 0
            write.clear()
            write.write(a,align="right",font=("arial",20,"normal"))
def button_2(x,y):
    global a
    global b
    global counter
    global function
    if x > -50 and x<0 and y>-100 and y<-50:
        if counter == 0:
            if len(a)<12:
                a = a+"2"
                write.clear()
                write.write(a,align="right",font=("arial",20,"normal"))
        elif counter == 1:
            if len(b)<12:
                b = b+"2"
                write.clear()
                write.write(b,align="right",font=("arial",20,"normal"))
        elif counter ==2:
            a = '2'
            b = ''
            counter = 0
            write.clear()
            write.write(a,align="right",font=("arial",20,"normal"))
def button_3(x,y):
    global a
    global b
    global counter
    global function
    if x > 0 and x < 50 and y > -100 and y< -50:
        if counter == 0:
            if len(a)<12:
                a = a+"3"
                write.clear()
                write.write(a,align="right",font=("arial",20,"normal"))
        elif counter == 1:
            if len(b)<12:
                b = b+"3"
                write.clear()
                write.write(b,align="right",font=("arial",20,"normal"))
        elif counter ==2:
            a = '3'
            b = ''
            counter = 0
            write.clear()
            write.write(a,align="right",font=("arial",20,"normal"))
def button_4(x,y):
    global a
    global b
    global counter
    global function
    if x > -100 and x < -50 and y >-50 and y < 0:
        if counter == 0:
            if len(a)<12:
                a = a+"4"
                write.clear()
                write.write(a,align="right",font=("arial",20,"normal"))
        elif counter == 1:
            if len(b)<12:
                b = b+"4"
                write.clear()
                write.write(b,align="right",font=("arial",20,"normal"))
        elif counter ==2:
            a = '4'
            b = ''
            counter = 0
            write.clear()
            write.write(a,align="right",font=("arial",20,"normal"))
        print("4")
def button_5(x,y):
    global a
    global b
    global counter
    global function
    if x > -50 and x<0 and y >-50 and y < 0:
        if counter == 0:
            if len(a)<12:
                a = a+"5"
                write.clear()
                write.write(a,align="right",font=("arial",20,"normal"))
        elif counter == 1:
            if len(b)<12:
                b = b+"5"
                write.clear()
                write.write(b,align="right",font=("arial",20,"normal"))
        elif counter ==2:
            a = '5'
            b = ''
            counter = 0
            write.clear()
            write.write(a,align="right",font=("arial",20,"normal"))
        print("5")
def button_6(x,y):
    global a
    global b
    global counter
    global function
    if x > 0 and x<50 and y >-50 and y < 0:
        if counter == 0:
            if len(a)<12:
                a = a+"6"
                write.clear()
                write.write(a,align="right",font=("arial",20,"normal"))
        elif counter == 1:
            if len(b)<12:
                b = b+"6"
                write.clear()
                write.write(b,align="right",font=("arial",20,"normal"))
        elif counter ==2:
            a = '6'
            b = ''
            counter = 0
            write.clear()
            write.write(a,align="right",font=("arial",20,"normal"))
        print("6")
def button_7(x,y):
    global a
    global b
    global counter
    global function
    if x > -100 and x<-50 and y >0 and y < 50:
        if counter == 0:
            if len(a)<12:
                a = a+"7"
                write.clear()
                write.write(a,align="right",font=("arial",20,"normal"))
        elif counter == 1:
            if len(b)<12:
                b = b+"7"
                write.clear()
                write.write(b,align="right",font=("arial",20,"normal"))
        elif counter ==2:
            a = '7'
            b = ''
            counter = 0
            write.clear()
            write.write(a,align="right",font=("arial",20,"normal"))
        print("7")
def button_8(x,y):
    global a
    global b
    global counter
    global function
    if x > -50 and x<0 and y >0 and y < 50:
        if counter == 0:
            if len(a)<12:
                a = a+"8"
                write.clear()
                write.write(a,align="right",font=("arial",20,"normal"))
        elif counter == 1:
            if len(b)<12:
                b = b+"8"
                write.clear()
                write.write(b,align="right",font=("arial",20,"normal"))
        elif counter ==2:
            a = '8'
            b = ''
            counter = 0
            write.clear()
            write.write(a,align="right",font=("arial",20,"normal"))
        print("8")
def button_9(x,y):
    global a
    global b
    global counter
    global function
    if x > 0 and x<50 and y >0 and y < 50:
        if counter == 0:
            if len(a)<12:
                a = a+"9"
                write.clear()
                write.write(a,align="right",font=("arial",20,"normal"))
        elif counter == 1:
            if len(b)<12:
                b = b+"9"
                write.clear()
                write.write(b,align="right",font=("arial",20,"normal"))
        elif counter ==2:
            a = '9'
            b = ''
            counter = 0
            write.clear()
            write.write(a,align="right",font=("arial",20,"normal"))
        print("9")
def button_0(x,y):
    global a
    global b
    global counter
    global function 
    if x>-50 and x<0 and y>-150 and y<-100:
        if counter == 0:
            if len(a)<12:
                a = a+"0"
                write.clear()
                write.write(a,align="right",font=("arial",20,"normal"))
        elif counter == 1:
            if len(b)<12:
                b = b+"0"
                write.clear()
                write.write(b,align="right",font=("arial",20,"normal"))
        elif counter ==2:
            a = '0'
            b = ''
            counter = 0
            write.clear()
            write.write(a,align="right",font=("arial",20,"normal"))
        print("0")
def button_pi(x,y):
    global a
    global b
    global counter
    global function 
    if x > -100 and x<-50 and y >50 and y < 100:
        if counter == 0:
            a = "3.141592653589"
            write.clear()
            write.write(a,align="right",font=("arial",20,"normal"))
        elif counter == 0:
            b = "3.141592653589"
            write.clear()
            write.write(b,align="right",font=("arial",20,"normal"))
        print("3.14159265358")
def button_e(x,y):
    global a
    global b
    global counter
    global function 
    if x > -50 and x<0 and y>50 and y<100:
        if counter == 0:
            a = "2.718281828459"
            write.clear()
            write.write(a,align="right",font=("arial",20,"normal"))
        elif counter == 1:
            b = "2.718281828459"
            write.clear()
            write.write(b,align="right",font=("arial",20,"normal"))
        elif counter ==2:
            a = "2.718281828459"
            write.clear()
            write.write(a,align="right",font=("arial",20,"normal"))
        print("2.71828182845")
def button_percent(x,y):
    global a
    global b
    global counter
    global function 
    if x>0 and x<50 and y>50 and y<100:
        a = str(percent(float(a)))
        write.clear()
        write.write(a,align="right",font=("arial",20,"normal"))
        counter = 2
        print("percent")
def button_decimalpoint(x,y):
    global a
    global b
    global counter
    global function
    if x>50 and x<100 and y>50 and y<100:
        if counter == 0:
            if len(a)<12:
                if len(a)==0:
                    a = "0."
                if "." not in a:
                    a = a+"."
                write.clear()
                write.write(a,align="right",font=("arial",20,"normal"))
        elif counter == 1:
            if len(b)<12:
                if len(b) == 0:
                    b= "0."
                if "." not in b:
                    b = b+"."
                write.clear()
                write.write(b,align="right",font=("arial",20,"normal"))
        elif counter ==2:
            a = '0.'
            b = ''
            counter = 0
            write.clear()
            write.write(a,align="right",font=("arial",20,"normal"))
        print(".")
def button_xmody(x,y):
    global a
    global b
    global counter
    global function 
    if x > -100 and x<-50 and y >100 and y<150:
        if counter == 0:
            counter = 1
            function = x_mod_y
            write.clear()
            b = ''
        elif counter == 1:
            function = x_mod_y
            b = ''
            write.clear()
        elif counter == 2:
            counter = 1
            function = x_mod_y
            write.clear()
            b = ''
        print("x (mod y)")
def button_logxy(x,y):
    global a
    global b
    global counter
    global function 
    if x > -50 and x < 0 and y > 100 and y<150:
        if counter == 0:
            counter = 1
            function = log_x_y
            write.clear()
            b = ''
        elif counter == 1:
            function = log_x_y
            b = ''
            write.clear()
        elif counter == 2:
            counter = 1
            function = log_x_y
            write.clear()
            b = ''
        print("log_x Y")
def button_xtothenth(x,y):
    global a
    global b
    global counter
    global function 
    if x > 0 and x<50 and y>100 and y<150:
        if counter == 0:
            counter = 1
            function = x_to_the_nth_power
            write.clear()
            b = ''
        elif counter == 1:
            function = x_to_the_nth_power
            b = ''
            write.clear()
        elif counter == 2:
            counter = 1
            function = x_to_the_nth_power
            write.clear()
            b = ''
        print("x^n")
def button_xtothenth_root(x,y):
    global a
    global b
    global counter
    global function 
    if x > 50 and x < 100 and y > 100 and y < 150:
        if counter == 0:
            counter = 1
            function = x_to_the_nth_root
            write.clear()
            b = ''
        elif counter == 1:
            function = x_to_the_nth_root
            b = ''
            write.clear()
        elif counter == 2:
            counter = 1
            function = x_to_the_nth_root
            write.clear()
            b = ''
        print("x to the nth root")
def button_equals(x,y):
    global a
    global b
    global counter
    global function 
    if x>-100 and x<100 and y > -200 and y < -150:
        if counter == 0:
            counter =2
            write.clear()
            write.write(a,align='right',font=('arial',20,'normal'))
        elif counter ==1:
            if function == division or function == multiply or function == add or function == subtract:
                a = str(function(float(a),float(b)))
                while len(a) > 12:
                    a = a[:-1]
                b = ''
                write.clear()
                write.write(a,align='right',font=('arial',20,'normal'))
            elif function == x_mod_y or function == x_to_the_nth_power or function == x_to_the_nth_root or function == log_x_y:
                a = str(function(int(float(a)),int(float(b))))
                if float("0"+a[1:])>0.999:
                    a = str(round(float(a)))
                while len(a) > 12:
                    a = a[:-1]
                b = ''
                write.clear()
                write.write(a,align='right',font=('arial',20,'normal'))
            counter = 2
        elif counter == 2:
            if function == division or function == multiply or function == add or function == subtract:
                a = str(function(float(a),float(b)))
                while len(a) > 12:
                    a = a[:-1]
                b = ''
                write.clear()
                write.write(a,align='right',font=('arial',20,'normal'))
            elif function == x_mod_y or function == x_to_the_nth_power or function == x_to_the_nth_root or function == log_x_y:
                a = str(function(int(float(a)),int(float(b))))
                if float("0"+a[1:])>0.999:
                    a = str(round(float(a)))
                while len(a) > 12:
                    a = a[:-1]
                b = ''
                write.clear()
                write.write(a,align='right',font=('arial',20,'normal'))
            counter = 2
        print("=")
def button_divide(x,y):
    global a
    global b
    global counter
    global function 
    if x > 50 and x < 100 and y > 0 and y <50:
        if counter == 0:
            counter = 1
            function = division
            write.clear()
            b = ''
        elif counter == 1:
            function = division
            b = ''
            write.clear()
        elif counter == 2:
            counter =1
            function = division
            write.clear()
            b = ''
        print("÷")
def button_multiply(x,y):
    global a
    global b
    global counter
    global function 
    if x > 50 and x < 100 and y > -50 and y < 0:
        if counter == 0:
            counter = 1
            function = multiply
            write.clear()
            b = ''
        elif counter == 1:
            function = multiply
            b = ''
            write.clear()
        elif counter == 2:
            counter =1
            function = multiply
            write.clear()
        print("×")
def button_subtract(x,y):
    global a
    global b
    global counter
    global function
    if x > 50 and x < 100 and y > -100 and y < -50:
        if counter == 0:
            counter = 1
            function = subtract
            write.clear()
            b = ''
        elif counter == 1:
            function = subtract
            b = ''
            write.clear()
        elif counter == 2:
            counter =1
            function = subtract
            write.clear()
        print("-")
def button_add(x,y):
    global a
    global b
    global counter
    global function 
    if x > 50 and x < 100 and y > -150 and y < -100:
        if counter == 0:
            counter = 1
            function = add
            write.clear()
            b = ''
        elif counter == 1:
            function = add
            b = ''
            write.clear()
        elif counter == 2:
            counter =1
            function = add
            write.clear()
        print("+")
def button_CE(x,y):
    global a
    global b
    global counter
    global function 
    if x>-100 and x<-50 and y>-150 and y<-100:
        if counter == 0:
            a = ''
            write.clear()
            write.write(a,align='right',font=('arial',20,'normal'))
        elif counter == 1:
            b=''
            write.clear()
            write.write(b,align='right',font=('arial',20,'normal'))
        elif counter == 2:
            a = ''
            write.clear()
            write.write(a,align='right',font=('arial',20,'normal'))
        print("CE")
def button_AC(x,y):
    global a
    global b
    global counter
    global function       
    if x>0 and x<50 and y>-150 and y<-100:
        a = ''
        b = ''
        function = ''
        write.clear()
        write.write(a,align='right',font=('arial',20,'normal'))
        print("AC")

#def button(x,y):
#    print(x,y)
onscreenclick(button_2,1)
#onscreenclick(button,1,add=True)
onscreenclick(button_1,1,add=True)
onscreenclick(button_3,1,add=True)
onscreenclick(button_4,1,add=True)
onscreenclick(button_5,1,add=True)
onscreenclick(button_6,1,add=True)
onscreenclick(button_7,1,add=True)
onscreenclick(button_8,1,add=True)
onscreenclick(button_9,1,add=True)
onscreenclick(button_0,1,add=True)
onscreenclick(button_pi,1,add=True)
onscreenclick(button_e,1,add=True)
onscreenclick(button_percent,1,add=True)
onscreenclick(button_decimalpoint,1,add=True)
onscreenclick(button_xmody,1,add=True)
onscreenclick(button_logxy,1,add=True)
onscreenclick(button_xtothenth,1,add=True)
onscreenclick(button_xtothenth_root,1,add=True)
onscreenclick(button_equals,1,add=True)
onscreenclick(button_divide,1,add=True)
onscreenclick(button_multiply,1,add=True)
onscreenclick(button_subtract,1,add=True)
onscreenclick(button_add,1,add=True)
onscreenclick(button_AC,1,add=True)
onscreenclick(button_CE,1,add=True)

listen()

done()
