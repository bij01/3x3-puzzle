import turtle as t
import time
import random

t.title("3x3 Puzzle Game")
t.bgpic("C://Users//Kwon//Desktop//git//3x3_puzzle//img//bg.gif")
t.setup(567, 564)

btnB = False
gameB = True

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
pen = t.Turtle()
pen.hideturtle()

location1 = -100, 120
location2 = 0, 120
location3 = 100, 120
location4 = -100, 20
location5 = 0, 20
location6 = 100, 20
location7 = -100, -80
location8 = 0, -80
location9 = 100, -80

t_list = [t1, t2, t3, t4, t5, t6, t7, t8, t9]
t_list2 = [1, 2, 3, 4, 5, 6, 7, 8]


l_list = [location1, location2, location3, location4, location5,
          location6, location7, location8, location9]

locations = {location1:t1, location2:t2, location3:t3, location4:t4,
             location5:t5, location6:t6, location7:t7, location8:t8,
             location9:None}

def move_block(x, y):
    if btnB == False:
        pass
    else:
        #print(x, y)
        if -50 >= x >= -150 and 70 <= y <= 170:
            #print("1번 위치")
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
            #print("2번 위치")
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
            #print("3번 위치")
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
            #print("4번 위치")
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
            #print("5번 위치")
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
            #print("6번 위치")
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
            #print("7번 위치")
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
            #print("8번 위치")
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
            #print("9번 위치")
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

        if (locations[location1] == t1) and (locations[location2] == t2) and (locations[location3] == t3) and (locations[location4] == t4) and (locations[location5] == t5) and (locations[location6] == t6) and (locations[location7] == t7) and (locations[location8] == t8) and (locations[location9] == None):
            game_over()


def quit_game(x, y):
    t.bye()


def game_over():
    t.register_shape("C://Users//Kwon//Desktop//git//3x3_puzzle//img//start.gif")
    endTime = time.time()
    playTime = time.localtime(endTime-startTime)
    for x in t_list:
        x.hideturtle()
    gameover.showturtle()
    pen.showturtle()
    pen.penup()
    pen.goto(0, 0)
    pen.write("걸린시간: {}분 {}초".format(playTime.tm_min, playTime.tm_sec)
              , move=True, align='center', font=('배달의민족 주아', 20, 'normal'))
    pen.goto(120, 20)
    start.shape("C://Users//Kwon//Desktop//git//3x3_puzzle//img//start.gif")


def start_game(x, y):
    t.register_shape("C://Users//Kwon//Desktop//git//3x3_puzzle//img//down.gif")
    
    global btnB, gameB
    btnB = False
    if gameB == False:
        pass
    else:
        gameB = False
        for i in range(0, 8):
            t_list[i].goto(l_list[i])
            locations[l_list[i]] = t_list[i]

        locations[l_list[8]] = None
        global startTime
        startTime = time.time()
        pen.clear()
        for x in t_list:
            x.showturtle()
        gameover.hideturtle()
        pen.hideturtle()
        start.shape("C://Users//Kwon//Desktop//git//3x3_puzzle//img//down.gif")
        random.shuffle(t_list2)

        fCount = 0
        # [무질서 카운트]
        # 리스트의 앞순서에 있는 숫자를 뒷순서에 있는 숫자들과 하나씩 비교했을때
        # 뒷순서에 있는 숫자가 앞순서에 있는 숫자보다 작을 경우 무질서 카운트를 증가시킴
        for x in range(0, len(t_list2)):
            for y in range(x, len(t_list2)):
                if t_list2[x] <= t_list2[y]:
                    pass
                else:
                    fCount += 1
        # 무질서 카운트를 2로 나눈 나머지 값이 1일 경우 짝수, 0일 경우 홀수
        # 나머지 값이 홀수일 경우 정상적인 게임 진행이 불가능하므로 랜덤값을 다시 돌림
        if fCount % 2 != 0:
            gameB = True
            start_game(0, 0)
        else:
            t_list3 = [] #블록 순서를 위한 배열
            for x in range(0, len(t_list2)):
                t_list3.append(t_list[t_list2[x] - 1])
            for i in range(0, len(t_list3)):
                t_list3[i].goto(l_list[i])
                locations[l_list[i]] = t_list3[i]
            btnB = True
            gameB = True
            


def set_blocks():
    for i in range(1, 10):
        path = "C://Users//Kwon//Desktop//git//3x3_puzzle//img//" + str(i) + ".gif"
        t.register_shape(path)
        t_list[i - 1].penup()
        t_list[i-1].shape(path)
        t_list[i-1].shapesize(5, 5, 0)
        t_list[i-1].goto(l_list[i-1])
        t_list[i-1].onclick(move_block)

    t.register_shape("C://Users//Kwon//Desktop//git//3x3_puzzle//img//start.gif")
    t.register_shape("C://Users//Kwon//Desktop//git//3x3_puzzle//img//quit.gif")
    t.register_shape("C://Users//Kwon//Desktop//git//3x3_puzzle//img//title.gif")
    t.register_shape("C://Users//Kwon//Desktop//git//3x3_puzzle//img//gameover.gif")
    t.register_shape("C://Users//Kwon//Desktop//git//3x3_puzzle//img//pen.gif")
    
    title.penup()
    title.shape("C://Users//Kwon//Desktop//git//3x3_puzzle//img//title.gif")
    title.setposition(130, 260)

    start.shape("C://Users//Kwon//Desktop//git//3x3_puzzle//img//start.gif")
    start.penup()
    start.setposition(-80, -200)
    start.onclick(start_game)

    quit.shape("C://Users//Kwon//Desktop//git//3x3_puzzle//img//quit.gif")
    quit.penup()
    quit.goto(80, -200)
    quit.onclick(quit_game)

    gameover.shape("C://Users//Kwon//Desktop//git//3x3_puzzle//img//gameover.gif")
    gameover.penup()
    gameover.goto(0, 100)

    pen.shape("C://Users//Kwon//Desktop//git//3x3_puzzle//img//pen.gif")


set_blocks()
t.mainloop()
