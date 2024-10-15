acievable_points = int(input("total points possible: "))
achieved_points = int(input("how many points did they get: "))
percent = achieved_points / acievable_points *100

if percent <= 50:
    print("F")
elif percent <=60 and percent >50:
    print("D")
elif percent <=88 and percent > 75:
    print("B")
elif percent <<75 and percent > 68:
    print("C")
elif percent >=100 and percent >89:
    print("A")