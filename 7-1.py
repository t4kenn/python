a = 1
b = 100
c = 0
while a <= b:
    # c = c + a と同じ意味
    c += a
    a += 1
print('合計:', c)