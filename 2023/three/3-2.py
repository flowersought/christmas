#booo this isnt working yet

with open('test.txt','r') as inputfile:
    input=inputfile.read()
    lines=input.split('\n')

grid=[]
for line in lines:
    grid.append("."+line+".")

#[y value][x value]

symbols='*'
nums='1234567890'
scoords=[]
numbers=[]
gears=[]
total=0
yes=[]

for lineno,line in enumerate(lines):
    for i in range(len(line)):
        if line[i] in symbols:
            scoords.append((lineno,i))

for [i,j] in scoords:
    temp=[]
    for y in range(i-1,i+2):
        for x in range(j-1,j+2):
            temp.append((y,x))
    gears.append(temp)

for gear in gears:
    count=0
    for (y,x) in gear:
        if lines[y-1][x].isnumeric():
            count+=1
    if count==2:
        yes.append(gear)

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

for gear in yes:
    temp=[]
    for i in range(len(gear)):
        for x in range(len(numbers)):
            if gear[i] in numbers[x][1]:
                temp.append(numbers[x][0])
    total+=int(temp[0])*int(temp[1])


# for i in range(numbers):
#     if numbers[i][1]

print(total)


