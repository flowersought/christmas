
textfile=open('1-1.txt','r')
lines=textfile.readlines()
total=0
num='0123456789'

numz=[]
numz2=[]

for line in lines:
    temp=''
    for i in range(0,len(line)):
        if line[i] in num:
            temp+=line[i]
    numz.append(temp)
    
for x in numz:
    temp=''
    temp+=x[0]
    temp+=x[-1]
    numz2.append(int(temp))

for y in numz2:
    total+=y

print(total)