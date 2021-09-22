def san(num):
    return num*3

input_num = int(input("整数を入力してください:"))

san_num = san(input_num)
kyuu = san(san_num)

print(input_num, "の9倍は", kyuu, "です。", sep="")