#ask user for name

name = input('What is your name?: ')

#ask user for age

age = input('How old are you?: ')

#ask user for location

location = input('Where are you from?: ')

#ask user for hobby

hobby = input('What is your favorite thing to do?: ')

#create output including vars

sentence = "Your name is {} and you are {} years old. You live in {}, and you love to {}."
output = sentence.format(name,age,location,hobby)

#print output
###.format -> automatically changes all variable types to strings

print(output)


