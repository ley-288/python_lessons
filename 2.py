#functions

def sayhi():
    print("Hello User")

sayhi()

..

def sayhi():
    print("Hello User")

print("Top")
sayhi()
print("Bottom")

..

def say_hi(name):
    print("Hello " + name)

say_hi("Mike")
say_hi("Steve")

..

def say_hi(name, age):
    print("Hello " + name + ", you are " + age)

say_hi("Mike", "35")
say_hi("Steve", "26")

..

def say_hi(name, age):
    print("Hello " + name + ", you are " + str(age)) #convert int field to string
say_hi("Mike", 35)
say_hi("Steve", 26)

..

def cube(num): #defined function
    return num*num*num #return gives something back to whatever called the function

result = cube(4) #variable. equal to the function of cube
print(result) #called function, ran through function, return a value. printed that result.

..

is_male = True

if is_male:
    print("Male")
else:
    print("Not Male")

..

is_male = True
is_tall = True

if is_male or is_tall:
    print("Male or tall or both")
else:
    print("Neither")

..

is_male = True
is_tall = True

if is_male and is_tall:
    print("Male and tall")
else:
    print("Either nor neither")

..

is_male = True
is_tall = True

if is_male and is_tall:
    print("Male and tall")
elif is_male and not(is_tall):
    print("male but short")
elif not(is_male) and is_tall:
    print("tall but not male")
else:
    print("Either nor neither")


..

def ma_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1 #biggest
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(ma_num(3,4,5))

..

go to 3.py


