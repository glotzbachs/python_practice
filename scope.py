# two different scopes
#   -global
#   -local

#a is a global variable
a=100

def f1():
    # a is now redefined locally
    a=50
    print(a)

def f2():
    # a is redefined locally again
    #any variable from a seperate function will not be recognized in this function!
    a=300
    print(a)

# call functions

f1()
f2()
print(a) #global variable doesn't change!



# global values can be manipulated in functions, however

numbers = [1,2,3]
b=3
print(b)
def man(num):
    global b #using this within a function allows it to be changed
    b=4
    numbers.append(num) #this changes the list even though it was defined outside of the functions

man(4)
man(5)
print(numbers)
print(b)
