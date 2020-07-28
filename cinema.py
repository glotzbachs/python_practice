movies = {
    'Finding Dory':[3,5],
    'Bourne':[18,5],
    'Tarzan':[15,5],
    'Ghost Busters':[12,5]
    }

while True:
    choice = input('What movie would you like to watch?: ').strip().title()

    if choice in movies:
        age = int(input('How old are you?: ').strip())

        if age>= movies[choice][0]:
            if movies[choice][1]>0:
                print('Enjoy the movie! There are {} tickets left.'.format(movies[choice][1]))
                movies[choice][1] = movies[choice][1] - 1
            else:
                print('Sorry we are sold out!')   
        else:
            print('You are to young to see that film!')
    else:
        print("We don't have that film.")

    
