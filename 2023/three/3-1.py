with open('3.txt','r') as inputfile:
    input=inputfile.read()
    lines='.'+input.split('\n')+'.'

lineno=0
symbols='!@#$%^&*-=+_'
nums='0123456789'
symb=[]
numb=[]
ok=[]

print(lines)

for line in lines:
    for i in range(0,len(line)):
        if line[i] in symbols:
            symb.append(i,lineno)
        if line[i] in nums:
            numb.append(i,lineno)
    lineno+=1

for line in lines:
    for (x,y) in nums: 
        if 