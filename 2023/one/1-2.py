
textfile=open('1-1.txt','r')
lines=textfile.readlines()
total=0
nums='1234567890'
numdict={'one':'o1e','two':'t2o','three':'t3e','four':'f4r','five':'f5e','six':'6',
         'seven':'7n','eight':'e8t','nine':'n9e'}

list1=[]
list2=[]

for line in lines:
    for key in numdict:
        if key in line:
            line=line.replace(key,numdict[key])
    list1.append(line)

for string in list1:
    temp=''
    for i in range(0,len(string)):
        if string[i] in nums:
            temp+=string[i]
    list2.append(temp)

for x in list2:
    temp=''
    temp+=x[0]
    temp+=x[-1]
    total+=int(temp)

print(total)
