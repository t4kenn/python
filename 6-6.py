n = 0

start = int(input('開始数:'))
end = int(input('終了数:'))

for m in range(start, end+1):
    n += m

print('合計;', n, sep='')