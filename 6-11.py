print('長方形を描画します。', '2~10までの整数値を入力してください')
n = int(input('行数の入力:'))
m = int(input('列数の入力:'))

for i in range(n):
    for j in range(m):
        print('*', end='')
print()