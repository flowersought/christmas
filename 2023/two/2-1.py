
input=open('2-1.txt','r')
lines=input.readlines()
colours={"red":0,"green":1,"blue":2}
nums='1234567890'
gamedict={}
count=[]

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
    for round in gamedict[game]:
        if int(round[0])>red or int(round[1])>green or int(round[2])>blue:
            if game not in count:
                count.append(game)

total=5050
for num in count:
    total-=int(num)    

print(total)

        

