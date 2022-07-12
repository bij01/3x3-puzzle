import random
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
t_list = [t1, t2, t3, t4, t5, t6, t7, t8]
t_list2 = [1, 2, 3, 4, 5, 6, 7, 8]

random.shuffle(t_list2)


fCount = 0
print(t_list)
for x in range(0, len(t_list2)):
    for y in range(x, len(t_list2)):
        if t_list2[x] <= t_list2[y]:
            pass
        else:
            fCount += 1
            print(t_list2[x], t_list2[y])
            print(t_list2[x] <= t_list2[y])
print(fCount)
if fCount % 2 == 0:
    print("진행")
    t_list3 = []
    for x in range(0, len(t_list2)):
        t_list3.append(t_list[t_list2[x]-1])

    print("터틀 순서:", t_list3)
else:
    print("다시뽑기")