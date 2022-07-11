import turtle as t

t1 = t.Turtle()
t2 = t.Turtle()
t3 = t.Turtle()
t4 = t.Turtle()
t5 = t.Turtle()
t6 = t.Turtle()
t7 = t.Turtle()
t8 = t.Turtle()
t9 = t.Turtle()

t1.penup()
t2.penup()
t3.penup()
t4.penup()
t5.penup()
t6.penup()
t7.penup()
t8.penup()
t9.penup()

t1.shape("square")
t2.shape("square")
t3.shape("square")
t4.shape("square")
t5.shape("square")
t6.shape("square")
t7.shape("square")
t8.shape("square")
t9.shape("square")

t1.shapesize(5, 5, 0)
t2.shapesize(5, 5, 0)
t3.shapesize(5, 5, 0)
t4.shapesize(5, 5, 0)
t5.shapesize(5, 5, 0)
t6.shapesize(5, 5, 0)
t7.shapesize(5, 5, 0)
t8.shapesize(5, 5, 0)
t9.shapesize(5, 5, 0)

t1.color("blue")
t2.color("gray")
t3.color("yellow")
t4.color("gray")
t5.color("green")
t6.color("gray")
t7.color("blue")
t8.color("gray")
t9.color("red")

t1.goto(-100, 100)
t2.goto(0, 100)
t3.goto(100, 100)

t4.goto(-100, 0)
t5.goto(0, 0)
t6.goto(100, 0)

t7.goto(-100, -100)
t8.goto(0, -100)
t9.goto(100, -100)


def move_block(x, y):
    print(x, y)
    print(t1.position())
    print(t2.position())
    print(t3.position())


t1.onclick(move_block)



t.mainloop()
