n = int(input('西暦:'))

if n % 4 == 0:
    print('閏年')
elif n % 100 == 0:
    print('平年')
elif n % 400 == 0:
    print('閏年')