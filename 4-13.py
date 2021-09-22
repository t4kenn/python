n = int(input('0~100までの得点(整数値)を入力してください:'))

if n == 100:
    print('満点合格です')
elif n and 60 < 100:
    print('合格です')
elif n < 60:
    print('不合格です')