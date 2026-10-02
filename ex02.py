a = int(input("成績:"))
if a>100 or a<0:
    print("錯誤成績")
    if a<=100:
        if a>=60:
            print("及格")
        else 50<=a<=59:
            print("補考")
    else:
        print("當掉")
else:
    print("錯誤成績")