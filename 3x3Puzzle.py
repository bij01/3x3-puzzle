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
t9.color("white")



location = {1:[-100, 100], 2:[0, 100], 3:[100, 100]}
block = [1, 2, 3, 4, 5, 6, 7, 8]

location1 = -100, 100
location2 = 0, 100
location3 = 100, 100
location4 = -100, 0
location5 = 0, 0
location6 = 100, 0
location7 = -100, -100
location8 = 0, -100
location9 = 100, -100

t1.goto(location1)
t2.goto(location2)
t3.goto(location3)
t4.goto(location4)
t5.goto(location5)
t6.goto(location6)
t7.goto(location7)
t8.goto(location8)
t9.goto(location9)

locations = {location1:t1, location2:t2, location3: t3, location4:t4,
             location5:t5, location6:t6, location7:t7, location8:t8,
             location9:None}

def move_block(x, y):
    print(locations)
    print(x, y)
    if -50 >= x >= -150 and 50 <= y <= 150:
        print("1번 위치")
        if locations[location2] == None:
            locations[location1].setposition(location2)
            locations[location2] = locations[location1]
            locations[location1] = None
        elif locations[location4] == None:
            locations[location1].setposition(location4)
            locations[location4] = locations[location1]
            locations[location1] = None
        else:
            pass
    elif 50 >= x >= -50 and 50 <= y <= 150:
        print("2번 위치")
        if locations[location1] == None:
            locations[location2].setposition(location1)
            locations[location1] = locations[location2]
            locations[location2] = None
        elif locations[location5] == None:
            locations[location2].setposition(location5)
            locations[location5] = locations[location2]
            locations[location2] = None
        elif locations[location3] == None:
            locations[location2].setposition(location3)
            locations[location3] = locations[location2]
            locations[location2] = None
        else:
            pass
    elif 50 <= x <= 150 and 50 <= y <= 150:
        print("3번 위치")
        if locations[location2] == None:
            locations[location3].setposition(location2)
            locations[location2] = locations[location3]
            locations[location3] = None
        elif locations[location6] == None:
            locations[location3].setposition(location6)
            locations[location6] = locations[location3]
            locations[location3] = None
        else:
            pass  
    elif -50 >= x >= -150 and 50 >= y >= -50:
        print("4번 위치")
        if locations[location1] == None:
            locations[location4].setposition(location1)
            locations[location1] = locations[location4]
            locations[location4] = None
        elif locations[location7] == None:
            locations[location4].setposition(location7)
            locations[location7] = locations[location4]
            locations[location4] = None
        elif locations[location5] == None:
            locations[location4].setposition(location5)
            locations[location5] = locations[location4]
            locations[location4] = None
        else:
            pass
    elif 50 >= x >= -50 and 50 >= y >= -50:
        print("5번 위치")
        if locations[location2] == None:
            locations[location5].setposition(location2)
            locations[location2] = locations[location5]
            locations[location5] = None
        elif locations[location4] == None:
            locations[location5].setposition(location4)
            locations[location4] = locations[location5]
            locations[location5] = None
        elif locations[location8] == None:
            locations[location5].setposition(location8)
            locations[location8] = locations[location5]
            locations[location5] = None
        elif locations[location6] == None:
            locations[location5].setposition(location6)
            locations[location6] = locations[location5]
            locations[location5] = None   
        else:
            pass  
    elif 50 <= x <= 150 and 50 >= y >= -50:
        print("6번 위치")

        if locations[location3] == None:
            locations[location6].setposition(location3)
            locations[location3] = locations[location6]
            locations[location6] = None
        elif locations [location5] == None:
            locations[location6].setposition(location5)
            locations[location5] = locations[location6]
            locations[location6] = None
        elif locations[location9] == None:
            locations[location6].setposition(location9)
            locations[location9] = locations[location6]
            locations[location6] = None
        else:
            pass
    elif -50 >= x >= -150 and -50 >= y >= -150:
        print("7번 위치")
        if locations[location4] == None:
            locations[location7].setposition(location4)
            locations[location4] = locations[location7]
            locations[location7] = None
        elif locations [location8] == None:
            locations[location7].setposition(location8)
            locations[location8] = locations[location7]
            locations[location7] = None
        else:
            pass
    elif 50 >= x >= -50 and -50 >= y >= -150:
        print("8번 위치")
        if locations[location5] == None:
            locations[location8].setposition(location5)
            locations[location5] = locations[location8]
            locations[location8] = None
        elif locations [location7] == None:
            locations[location8].setposition(location7)
            locations[location7] = locations[location8]
            locations[location8] = None
        elif locations[location9] == None:
            locations[location8].setposition(location9)
            locations[location9] = locations[location8]
            locations[location8] = None
        else:
            pass       
    elif 50 <= x <= 150 and -50 >= y >= -150:
        print("9번 위치")
        if locations[location6] == None:
            locations[location9].setposition(location6)
            locations[location6] = locations[location9]
            locations[location9] = None
        elif locations[location8] == None:
            locations[location9].setposition(location8)
            locations[location8] = locations[location9]
            locations[location9] = None
        else:
         pass 

    print("1번퍼즐 위치:", t1.position())
    print("2번퍼즐 위치:", t2.position())
    print("3번퍼즐 위치:", t3.position())
    print("4번퍼즐 위치:", t4.position())
    print("5번퍼즐 위치:", t5.position())
    print("6번퍼즐 위치:", t6.position())
    print("7번퍼즐 위치:", t7.position())
    print("8번퍼즐 위치:", t8.position())
    print("9번퍼즐 위치:", t9.position())

t1.onclick(move_block)
t2.onclick(move_block)
t3.onclick(move_block)
t4.onclick(move_block)
t5.onclick(move_block)
t6.onclick(move_block)
t7.onclick(move_block)
t8.onclick(move_block)
t9.onclick(move_block)

t.mainloop()
