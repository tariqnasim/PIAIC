# Part 1 : Working with Variables, Input, and Strings
#####################################################

# 1. Prompt for user input

print ("1. Prompt for user input")
print (" ")

full_name = input ("Please Enter your name: ")
print (" ")
print ("Hello, "+full_name+"! Welcome to the Python assignment.")
print (" ")

# 2. String methods
print ("2. Sting Methods")
print (" ")
print ("Uppercase letters : "+full_name.upper())
print ("Lowercase letters : "+full_name.lower())
print ("Length of the Username : "+str(len(full_name)))
print ("Replacing space with Hyphens : "+full_name.replace(" ","-"))
print ("Without removing (Original) trailing spaces from the string >>"+full_name+"<<")
print ("removing trailing spaces from the string >>"+full_name.strip()+"<<")
print (" ")

# 3. Type casting and numeric operations
print ("3. Type casting and numeric operations")
print (" ")

from datetime import datetime
yearOfBirth = input("Please enter your birth year : ")
currentYear = datetime.now().year
print (" ")
print ("You are approximately "+str((currentYear - int(yearOfBirth)))+" years old.")
#RQ1 - Since integer and string cannot do arithmetic operations str needs to be converted to int and
#      later to convert back to string to concatenate. 
print (" ")

######################################################

# Part 2: Lists and Indexing
############################

# 1. Create a list from user input
print ("1. Create a list from user input")
print (" ")

favoriteFruits = input("Enter three of your favorite fruits, separated by commas: ")
fruitList = favoriteFruits.split(",")
print("Your favorite fruits are in list as :", fruitList)
print (" ")

#
#

print (" ")
print ("Last List Item :"+fruitList[-1])
print ("First List Item :"+fruitList[0])
print ("Second List Item :"+fruitList[1])
print (" ")

newFruit = input("Enter another fruit to the list : ")
fruitList.append(newFruit)
print(fruitList)
print (" ")

lengthOfList = len(fruitList)
print("Length of the list: ", lengthOfList)

print (" ")
delListElement = input("Which element to delete - Enter the number [List Starts from 0 till "+str(lengthOfList-1)+"] ")

fruitList.pop(int(delListElement))

print (" ")
print ("Updated list based on index selection for deletion list is -> ")
print (fruitList)
print (" ")

############################################

# Part 3 (Optional Challenge): Combining Concepts
#################################################

# 1. String & List Interaction
##############################

print(" ")
letterList = list(full_name.replace(" ", ""))
print (letterList)
print(" ")
print (letterList[0:3]) # Prints first three letters in list
print (letterList[-3:]) # Prints last three letters in list
print(" ")

###############################################

# 2. Manipulate and Reconstruct
###############################

print(" ")
letterList = list(full_name.replace(" ", ""))
print (letterList)
print(" ")
print (letterList[0:3]) # Prints first three letters in list
print (letterList[-3:]) # Prints last three letters in list
print(" ")

n = 3 # First three letters
for i in range(len(letterList)):
    if i < n:  # Letters as defined by n
        letterList[i] = letterList[i].upper()
    else:      # as such list elements
        letterList[i] = letterList[i].lower()

reconstructed_string = "".join(letterList)
print ("Reconstructed string:", reconstructed_string)

########################################################

# 3. Simple Arithmetic on a List of Numbers
###########################################

numberInput = input("Please enter 5 numbers separated by spaces (e.g., '10 20 30 40 50'): ")
numbers_list = [int(num) for num in numberInput.split()]

sumOfNumbers = sum(numbers_list)
average = sumOfNumbers / len(numbers_list)
print ("Numbers List: ", numbers_list)
print ("Sum of Numbers: ", sumOfNumbers)
print ("Average: ", average)
print (" ")
print ("End of assignment# 3")

######################



