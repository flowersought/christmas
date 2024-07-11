with open('3.txt','r') as inputfile:
    input=inputfile.read()
    lines=input.split('\n')

lineno=0
symbols='!@#$%^&*-=+_'
coords=[]

for line in lines:
    for i in range(0,len(line)):
        if line[i] in symbols:
            coords.append((i,lineno))
    lineno+=1

