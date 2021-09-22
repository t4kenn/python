n = {"id" : 100,"name" : "大原太郎", "age" : 19}

n["age"] = 20

for key,value in n.items():
    print(key, ":", value, sep="")