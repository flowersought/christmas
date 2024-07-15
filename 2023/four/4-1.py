
total=0

with open('4.txt','r') as infile:
    input=infile.read()
    rows=input.split('\n')

for card in rows:
    xplier=-1
    win=card.split(': ')[1].split(' | ')[1].split(' ')
    nums=card.split(': ')[1].split(' | ')[0].split(' ')

    for num in nums: 
        if num=='':
            nums.remove(num)

    for num in nums: 
        for w in win:
            if num==w:
                xplier+=1
    
    if xplier>=0:
        total+=(2**xplier)

print(total)