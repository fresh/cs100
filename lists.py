ourList = []
#Lists are defined by [] (square brackets)

#To append to our list we can do this
ourList.append("apple")
print("After first append:", ourList)
#This appends the word apple to our list as a string
#We can also append numbers
ourList.append(1)
print("After second append:", ourList)

#For loop with List
print("For Loop with List")
for x in ourList:
    print(x)

#If you want to check the length of the list
print("Length of List")
length = len(ourList)
#This can be shortened to print(len(ourList))
print(length)

#We can also index the item
item = ourList[0] #Gets the first element
print("First element with index:", item)
