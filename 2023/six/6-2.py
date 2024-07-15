with open('6.txt','r') as infile:
    input=infile.read()
    rows=input.split('\n')

time=int(rows[0].split(':')[1].replace(" ",""))
dist=int(rows[1].split(':')[1].replace(" ",""))
wins=0

for i in range(1,time):
    timehold=i
    speed=i
    timeleft=time-i

    distance=speed*timeleft
    if distance > dist: 
        wins+=1
    if distance < dist and wins>=1:
        break
print(wins)
