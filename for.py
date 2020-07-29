# for loops hit each element in anything iterable!

# range(start, end, step)

for i in range(1,11):
    print(i)

for l in 'abcd':
    print(l)


# check for vowels and consonants

vowels = 0
consonants = 0


for letter in 'Hello':
    if letter.lower() in 'aeiou':
        vowels += 1
    elif letter == ' ':
        pass
    else:
        consonants +=1

print("There are {} vowel and {} consonants in Hello.".format(vowels, consonants))


# for loops and Dictionaries
# iterating through keys and their values

students = {
    'male':['Tom','Charlie','Harry','Frank'],
    'female':['Sarah','Huda','Samantha','Elizabeth','Emily']
    }

for key in students.keys():
    print(key)
    print(students[key])
    for name in students[key]:
        if 'a' in name:
            print(name)

# make a list of even numbers up to 100.. one line!

even_numbers = [x for x in range(1,101) if x % 2 == 0]
print(even_numbers)

# iterate over a list and do something with it

words = ['the','brown','dog','is','small']
word_length = [[w.upper(),len(w)] for w in words]
print(word_length)

