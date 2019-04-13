from turtle import*
n=4
l=5
forward(80)
left(90)

for i in range(n):
    for i in range(n):
        forward(10);left(90);forward(10);left(90);forward(10)
        right(90);forward(10);
        for j in range(l):
           right(90);forward(1);right(90);forward(10)
           left(90);forward(1);left(90);forward(10)
        left(90);forward(10);right(180)
    penup();forward(10);pendown()

    for i in range(n):
        forward(10);left(-90);forward(10);left(-90);forward(10)
        right(-90);forward(10);
        for j in range(l):
           right(-90);forward(1);right(-90);forward(10)
           left(-90);forward(1);left(-90);forward(10)
        left(-90);forward(10);right(-180)
    penup();forward(10);pendown()
"""right(180);penup();forward(80);pendown()
right(90);for"""
