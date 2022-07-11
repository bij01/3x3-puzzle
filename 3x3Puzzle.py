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


t.bgpic("")
t_list = [t1, t2, t3, t4, t5, t6, t7, t8, t9]


def make_shape():
    for i in range(1, 10):
        t_list[i - 1] = t.Turtle()
        path = "img/" + str(i) + ".gif"
        t.register_shape(path)
        t_list[i-1].shape(path)
        t_list[i - 1].shapesize(5, 5, 0)
        t_list[i - 1].penup()


make_shape()

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

locations = {location1:t1, location2:t2, location3:t3, location4:t4,
             location5:t5, location6:t6, location7:t7, location8:t8,
             location9:t9}


def move_block(x, y):
    print(x, y)
    print(locations[location1] == t1)
    print(locations[location2] == t2)
    print(locations[location3] == t3)
    print(locations[location4] == t4)
    print(locations[location5] == t5)
    print(locations[location6] == t6)
    print(locations[location7] == t7)
    print(locations[location8] == t8)
    print(locations[location9] == t9)

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
            locations[location2].setposition(location5)
            locations[location5] = locations[location2]
            locations[location2] = None
        else:
            pass
    elif -50 >= x >= -150 and 50 >= y >= -50:
        print("4번 위치")
    elif 50 >= x >= -50 and 50 >= y >= -50:
        print("5번 위치")
    elif 50 <= x <= 150 and 50 >= y >= -50:
        print("6번 위치")
    elif -50 >= x >= -150 and -50 >= y >= -150:
        print("7번 위치")
    elif 50 >= x >= -50 and -50 >= y >= -150:
        print("8번 위치")
    elif 50 <= x <= 150 and -50 >= y >= -150:
        print("9번 위치")

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
