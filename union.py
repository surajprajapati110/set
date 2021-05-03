li=[1,2,3,4,5,6,7,8,2,3,6,10]
s1=set()
s2=set()
for x in li:
    if x not in s1:
        s1.add(x)
    else:
        s2.add(x)
print(s1)
print(s2)
