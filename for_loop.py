# names = ["ali","amin","aida","reza","karim"]
# b = []
# for name in names :
#     if name [-1] == "a":
#         b.append(name)
#         print(name)




a = ['ali','amin','reza','aida']
b = ['reza','ali','amin','hani']
c = []
for x in a :
    for y in b :
        if x == y :
            c.append(x)
            print(x)

