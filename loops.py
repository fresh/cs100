LIST = [1, 2, 3, 4, 5]

DICT = {1: 'a', 
        2: 'b', 
        3: 'c'}

"""There are for loops which iterate through
a sequence which can be a list, dictionary or string.
* There are more, but the course does not cover it."""

print("Printing: For Loop with Range")
#https://www.w3schools.com/python/gloss_python_for_range.asp
for i in range(0, 10, 1):
    #Iterate over a sequence of numbers defined in range()
    print(i)

print("Printing: For Loop with List")
for x in LIST:
    #Iterate over the LIST variable defined above.
    print(x)

print("For Loop with Dictionary")
for key in DICT:
    #Iterate over keys in the dictionary
    print(key)
    #To print the keys and their values use dict[key]
    print(key, DICT[key])
    #There are other ways to do this but it is not needed in this class.

newList = []

while len(newList) != 3: #Until length of list is not equal 3 it will run.
    userInput = input("[?] What would you like to add: ")
    #We then append userInput
    newList.append(userInput)

print(newList)