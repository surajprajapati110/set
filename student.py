student={}
for x in range(3):
    name=input('student name')
    m=[]
    for y in range(3):
        i=(int)(input('mark'))
        m.append(i)
    student[name]=m
print(student)
sname=input('student name')
for x in student:
    if x==sname:
        print(sname,":",sum(student[x]))
