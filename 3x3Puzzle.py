import turtle as t
import time

t1 = t.Turtle()
t2 = t.Turtle()
t3 = t.Turtle()
t4 = t.Turtle()
t5 = t.Turtle()
t6 = t.Turtle()
t7 = t.Turtle()
t8 = t.Turtle()
t9 = t.Turtle()
start = t.Turtle()
quit = t.Turtle()
title = t.Turtle()
gameover = t.Turtle()
gameover.hideturtle()

t.bgpic("img/bg.gif")
t.setup(567, 564)
t.title("3x3 Puzzle Game")

location1 = -100, 120
location2 = 0, 120
location3 = 100, 120
location4 = -100, 20
location5 = 0, 20
location6 = 100, 20
location7 = -100, -80
location8 = 0, -80
location9 = 100, -80

t_list = [t1, t2, t3, t4, t5, t6, t7, t8, t9, start, title]
l_list = [location1, location2, location3, location4, location5,
          location6, location7, location8, location9]

locations = {location1:t1, location2:t2, location3:t3, location4:t4,
             location5:t5, location6:t6, location7:t7, location8:t8,
             location9:None}


def move_block(x, y):
    print(locations)
    print(x, y)
    if -50 >= x >= -150 and 70 <= y <= 170:
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
    elif 50 >= x >= -50 and 70 <= y <= 170:
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
    elif 50 <= x <= 150 and 70 <= y <= 170:
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
    elif -50 >= x >= -150 and 70 >= y >= -30:
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
    elif 50 >= x >= -50 and 70 >= y >= -30:
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
    elif 50 <= x <= 150 and 70 >= y >= -30:
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
            t_list[8].hideturtle()
        else:
            pass
    elif -50 >= x >= -150 and -30 >= y >= -130:
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
    elif 50 >= x >= -50 and -30 >= y >= -130:
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
            t_list[8].hideturtle()
        else:
            pass       
    elif 50 <= x <= 150 and -30 >= y >= -130:
        print("9번 위치")
        if locations[location6] == None:
            locations[location9].setposition(location6)
            locations[location6] = locations[location9]
            locations[location9] = None
            t_list[8].showturtle()
        elif locations[location8] == None:
            locations[location9].setposition(location8)
            locations[location8] = locations[location9]
            locations[location9] = None
            t_list[8].showturtle()
        else:
             pass

    print(locations[location1] == t1)
    print(locations[location2] == t2)
    print(locations[location3] == t3)
    print(locations[location4] == t4)
    print(locations[location5] == t5)
    print(locations[location6] == t6)
    print(locations[location7] == t7)
    print(locations[location8] == t8)
    print(locations[location9] == None)

def game_over(x, y):
    print("")

def start_game(x, y):
    print("") #1~8랜덤으로 섞어야함
    t_list[3].goto(location5)
    t_list[4].goto(location4)
    locations[location5] = t_list[3]
    locations[location4] = t_list[4]

    t_list[1].goto(location3)
    t_list[2].goto(location2)
    locations[location3] = t_list[1]
    locations[location2] = t_list[2]


def set_blocks():
    for i in range(1, 10):
        path = "img/" + str(i) + ".gif"
        t.register_shape(path)
        t_list[i - 1].penup()
        t_list[i-1].shape(path)
        t_list[i-1].shapesize(5, 5, 0)
        t_list[i-1].goto(l_list[i-1])
        t_list[i-1].onclick(move_block)
    t.register_shape("img/start.gif")
    t.register_shape("img/quit.gif")
    t.register_shape("img/title.gif")
    t.register_shape("img/gameover.gif")

    title.penup()
    title.shape("img/title.gif")
    title.setposition(130, 260)

    start.shape("img/start.gif")
    start.penup()
    start.setposition(-80, -200)
    start.onclick(start_game)

    quit.shape("img/quit.gif")
    quit.penup()
    quit.goto(80, -200)
    gameover.shape("img/gameover.gif")
    gameover.penup()
    gameover.goto(0, 100)


set_blocks()

t.mainloop()
