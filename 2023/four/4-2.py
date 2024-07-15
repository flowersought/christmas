pointd={}
cardcount={}
cardd={}

with open('test.txt','r') as infile:
    input=infile.read()
    rows=input.split('\n')

for card in rows:
    matches=0
    cardno=card.split(':')[0][5:]
    win=card.split(': ')[1].split(' | ')[1].split(' ')
    nums=card.split(': ')[1].split(' | ')[0].split(' ')

    for num in nums: 
        if num=='':
            nums.remove(num)

    for num in nums: 
        for w in win:
            if num==w:
                matches+=1
    
    pointd[cardno]=matches

print(pointd)
for card in pointd:
    if pointd[card]>0:
        for i in range(int(card),(int(card)+1+pointd[card])):
            if pointd[str(i)]     

