#I FORGOT TO ADD / INTO THTE SYMBOLS LIST KMS 

with open('3.txt','r') as inputfile:
    input=inputfile.read()
    lines=input.split('\n')

grid=[]
for line in lines:
    grid.append("."+line+".")

#[y value][x value]

symbols='!@#$%^&*-_=+/'
nums='1234567890'
scoords=[]
morecoords=[]
numbers=[]
total=0

for lineno,line in enumerate(lines):
    for i in range(len(line)):
        if line[i] in symbols:
            scoords.append((lineno,i))

for [i,j] in scoords:
    for y in range(i-1,i+2):
        for x in range(j-1,j+2):
            morecoords.append((y,x))
# print(morecoords)

for y,line in enumerate(grid):
    temp=''
    coo=[]
    for x in range(len(grid[y])):
        if line[x] in nums:
            temp+=line[x]
            coo.append((y,x-1)) 
        elif temp!='' and [temp,coo] not in numbers:
            numbers.append([temp,coo])
            temp=''
            coo=[]

for num,coords in numbers:
    for i in range(len(coords)):
        if coords[i] in morecoords:
            total+=int(num)
            print(num)
            break

print(total)

