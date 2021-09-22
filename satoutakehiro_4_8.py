print("0～100までの得点（整数値）を2つ入力してください")
pt1 = int(input("1つ目の得点："))
pt2 = int(input("2つ目の得点："))

if pt1 >= 60 and pt2 >= 60 :
    print("合格です")
else:
    print("不合格です")