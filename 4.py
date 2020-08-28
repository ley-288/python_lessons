#while loops

i = 1
while i <= 10:
    print(i)
    i += 1

print("done with loop")

..

#secret guess

secret_word = "giraffe"
guess = ""

while guess != secret_word:
    guess = input("Enter guess: ")

print("You win!")

..

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("out of guesses")
else:
    print("You win!")

..

#for loop

friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
    print(friend)

friends = ["Jim", "Karen", "Kevin"]
for index in range(10):
    print(index)

friends = ["Jim", "Karen", "Kevin"]
for index in range(3, 10):
    print(index)

friends = ["Jim", "Karen", "Kevin"]

for index in range(len(friends)):
    print(friends[index])

friends = ["Jim", "Karen", "Kevin"]

for index in range(len(friends)):
    print(friends[0]) #will print Kevins name 3 times. becuase for length of friends. which is 3. 3 names

friends = ["Jim", "Karen", "Kevin"]

for index in range(5):
    if index == 0:
        print("first iteration") #will print 1 time
    else:
        print("not first") #will print 4 times to complete the range

..

#exponent function

print(2**3) #2 cubed

..

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num): #loop through calc. base times base, number of pow_num times
        result = result * base_num
    return result

print(raise_to_power(3, 2)) #two to the third power

..

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8 ,9],
    [0]
]

print(number_grid[0][0])#row 0 column 0. number 1

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8 ,9],
    [0]
]

for row in number_grid:
    print(row) #will print all rows

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8 ,9],
    [0]
]

for row in number_grid:
    for col in row:
        print(col) #will print in 1 column

..

go to 5.py









