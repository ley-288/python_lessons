#translator

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: "))) #will ask for input and change every vowel into a g


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))#same but accounts for upper and lower case

..

#try / except

try:
	#value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid input") #will account for input of string when we need int without breaking program

try:
    answer = 10/2
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("invalid input")#will catch multiple specified errord to avoid program break

..

#open a file #r, w, a, r+

employee_file = open("employees.txt", "r")

print(employee_file.readable()) #can we read it? w,a would be false

employee_file.close()




employee_file = open("employees.txt", "r")

print(employee_file.read())

employee_file.close() #to display all information




employee_file = open("employees.txt", "r")

print(employee_file.readline()) #reads first line
print(employee_file.readline())

employee_file.close()



employee_file = open("employees.txt", "r")

print(employee_file.readlines()[1]) #will store all info into an array and then we can index

employee_file.close()



employee_file = open("employees.txt", "r")
for employee in employee_file.readlines():
    print(employee)

employee_file.close() #will print each name in a list



..

#writing and appending files

employee_file = open("employees.txt", "a")

employee_file.write("\nBill - Management") #on a new line. VERY IMPORTANT

employee_file.close()



employee_file = open("employees1.txt", "w")# DIFF FILENAME creates a new file. because w will overwrite the entire previous document

employee_file.write("Kelly - Management")

employee_file.close()


..

go to 6.py













