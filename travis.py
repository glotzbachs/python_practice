users = ['Alice','Bob','Claire','Dan', 'Emma', 'George', 'Harry']

while True:
    print('Hi! My name is Sarah')
    name = input('What is your name?: ').strip().capitalize()
    
    if name in users:
        print('Hello, {}!'.format(name))
        remove = input('Would you like to be removed from the database? y/n : ').strip().lower()

        if remove == 'y':
            users.remove(name)
        elif remove == 'n':
            print("Oh good! I didn't want you to leave, anyway.")
        
    else:
        print("I don't think I've met you yet, {}.".format(name))
        add_me = input('Would you like to be added to the database? y/n : ').strip().lower()

        if add_me == 'y':
            users= users + [name]
        elif remove == 'n':
             print("No worries. Hope to see you again soon!")


# ways to remove element from list
#   - del list[index]
#   - list.remove(item)

# ways to add an element to a list
#   - list.append(item) --- dangerous.. be careful! NOT list = list.append()
#   - list = list + [list]
#   - list = list + list(string) --- iterated over string to create an element for each letter
#   - list = list + [[list]] --- adds the list as an element
#   - list = insert(index, item) --- also dangerous!
        
