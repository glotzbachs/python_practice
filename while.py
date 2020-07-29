i=1
print('whole numbers to ten')

while i<=10:
    print(i)
    i+=1

 
# print odds

o=1
print('odd numbers to ten')
    
while o<10:
    print(o)
    o+=2


# print evens

e=2
print('even numbers to ten')

while e<=10:
    if e % 2 == 0: 
        print(e)
    e+=1


# make a team of people with 3 people

l=[]

while len(l)<=3:
    name = input('Please add a member to your team: ').strip().capitalize()
    l.append(name)

print('Sorry your team is already full!')
