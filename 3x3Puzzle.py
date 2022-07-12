import turtle as t
import pygame

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

t.bgpic("img/bg.gif")
t.setup(567, 564)

location1 = -100, 100
location2 = 0, 100
location3 = 100, 100
location4 = -100, 0
location5 = 0, 0
location6 = 100, 0
location7 = -100, -100
location8 = 0, -100
location9 = 100, -100

t_list = [t1, t2, t3, t4, t5, t6, t7, t8, t9]
l_list = [location1, location2, location3, location4, location5,
          location6, location7, location8, location9]

locations = {location1:t1, location2:t2, location3:t3, location4:t4,
             location5:t5, location6:t6, location7:t7, location8:t8,
             location9:None}


def move_block(x, y):
    print(locations)
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
            t_list[8].hideturtle()
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
            t_list[8].hideturtle()
        else:
            pass       
    elif 50 <= x <= 150 and -50 >= y >= -150:
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
    
    if (locations[location1] == t1) and (locations[location2] == t2) and (locations[location3] == t3) and (locations[location4] == t4) and (locations[location5] == t5) and (locations[location6] == t6) and (locations[location7] == t7) and (locations[location8] == t8) and (locations[location9] == None): 
        print("the game's over")
        pygame.quit()
    '''        
    li = [t1, t2, t3, t4, t5, t6, t7, t8, t9]  
    for i in li:
        if locations.get() == i:
            print("Game's over") 
            pygame.quit()
    '''           
     
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

def make_shape():
    for i in range(1, 10):
        path = "img/" + str(i) + ".gif"
        t.register_shape(path)
        t_list[i - 1].penup()
        t_list[i-1].shape(path)
        t_list[i-1].shapesize(5, 5, 0)
        t_list[i-1].goto(l_list[i-1])
        t_list[i-1].onclick(move_block)
t.register_shape("img/start.gif")
start.shape("img/start.gif")
start.penup()
start.setposition(0, -200)

make_shape()
t.mainloop()









'''     
msg = game_font.render(game_result, True, (255, 255, 0))            
msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
screen.blit(msg, msg_rect)
pygame.display.update()
pygame.time.delay(2000)
sys.exit("인자값") ----import sys
'''