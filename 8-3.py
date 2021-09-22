n = []
m = []

for i in range(10):
    num = int(input(str(i+1) + "件目:整数を入力 = "))

    if num % 2 == 0:
        n.append(num)
    else:
        m.append(num)

print("偶数値配列 =", n)

print("奇数値配列 =", m)