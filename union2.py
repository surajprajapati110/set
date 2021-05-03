s1={1,2,3,4,5,6,7}
s2={3,4,5,6,7,8,9}
li=[]
for x,y in zip(s1,s2):
    li.extend([x,y])
print(li)
