
input=open('2-1.txt','r')
lines=input.readlines()
colours={"red":0,"green":1,"blue":2}
nums='1234567890'
gamedict={}
total=0
maxs=[]

red=12
green=13
blue=14

for line in lines:
    lineno=str(line[5:].split(':')[0])
    templist=[]
    for round in line.split(':')[1].split(';'):
        temp=['0','0','0']
        for colr in round.split(','):
            tempnum=''
            for x in range(len(colr)):
                if colr[x] in nums:
                    tempnum+=colr[x]
            for key in colours:
                if key in colr:
                    temp[colours[key]]=tempnum
        templist.append(temp)
    gamedict[lineno]=templist



for game in gamedict:
    max=[0,0,0]
    for round in gamedict[game]:
        for i in range(0,3):
            if int(round[i])>max[i]:
                max[i]=int(round[i])
    maxs.append(max)

for max in maxs:
    total+=max[0]*max[1]*max[2]

print(total)

        

