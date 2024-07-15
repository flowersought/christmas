
with open('6.txt','r') as infile:
    input=infile.read()
    rows=input.split('\n')

time=rows[0].split(':')[1].split(' ')
dist=rows[1].split(':')[1].split(' ')

time = list(filter(None, time))
dist=list(filter(None,dist))

races={}

for i in range(0,len(time)):
    races[i]=[time[i],dist[i],0]

for race in races:
    wins=0
    for i in range(1,int(races[race][0])):
        timehold=i
        timeleft=int(races[race][0])-i
        speed=timehold

        dist1=speed*timeleft
        if dist1>int(races[race][1]):
            wins+=1
    races[race][2]=wins

total=1
for race in races:
    total*=races[race][2]

print(total)
