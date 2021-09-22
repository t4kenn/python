n = int(input('0~100までの得点(整数値)を入力してください'))

if n > 100 or n < 0:
    print('入力値が不正です')
elif n == 100:
    print('満点合格です')
elif n and 60 < 100:
    print('合格です')
else:
    print('不合格です')