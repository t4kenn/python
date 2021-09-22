print('３つのテスト(国語、数学、英語)の得点を入力してください')
n = int(input('国語'))
m = int(input('数学'))
l = int(input('英語'))
total = n + m + l

if total >= 230:
    print('合格')
elif total >= 210 and (n >= 85 or m >= 85 or l >= 85):
    print('合格')
else:
    print("補講対象")