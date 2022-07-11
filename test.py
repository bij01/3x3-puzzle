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

location1 = -100, 100
location2 = 0, 100
location3 = 100, 100
location4 = -100, 0
location5 = 0, 0
location6 = 100, 0
location7 = -100, -100
location8 = 0, -100
location9 = 100, -100

locations = {location1:t1, location2:None, location3:t3, location4:t4,
             location5:t5, location6:t6, location7:t7, location8:t8,
             location9:t9}


print(locations[location1])
