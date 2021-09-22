#n = '東京都千代田区神田神保町'
#print(n[3:11])

n = '東京都千代田区神田神保町'
m = '東京都'

l = n.index(m)

print(n[l + len(m):])