def take(a,hairetu):
    if a==a in hairetu:
        print("{}は配列に含まれています。".format(a))
    else:
        print("{}は配列に含まれていません。".format(a))

a=int(input("整数を入力してください:"))
hairetu=[4,10,59,679,1991,3994,6789,19324]
take(a,hairetu)