# ASSIGNMENT ==> #4 
###################

# Exercise 3-1: Names
#####################

# Create a list of names and store name of friends
names = ["Jawad", "Nadeem", "Amanullah", "Mubashir"]

# Print each name by accessing each element in the list
# Individual list items
print (names[0])
print (names[1])
print (names[2])
print (names[3])
print ("")

# By using loop
print ("Using For Loop")
for friendsName in names:
    print(friendsName)

print ("----------------------------------------------------------")
 
#Exercise 3-2: Greetings
########################
"""
  Start with the list you used in Exercise 3-1, 
  but instead of just printing each person’s name, print a message to them. 
  The text of each message should be the same, 
  but each message should be personalized with the person’s name
"""
message = ", Greetings for the new year 2025. Stay blessed."

print (names[0]+message)
print (names[1]+message)
print (names[2]+message)
print (names[3]+message)
print ("----------------------------------------------------------")

#Exercise 3-3: Your Own List
############################
""" 
Think of your favorite mode of transportation, such as a motorcycle or a car, 
and make a list that stores several examples. Use your list to print a series of 
statements about these items, such as “I would like to own a Honda motorcycle.”
 """

# Create a list of favorite modes of transportation
transportationMode = ["CD70 Motorcycle (1991)", "Mercedes E180 (2005)", "Toyota Prado (2007)", "Toyota Sequoia v8 (2010)", "Toyota Corolla (2020)"]

# Printing the statement 
for mode in transportationMode:
    print(f"I have owned a {mode}.")

print ("Alhamdolillah")
print ("----------------------------------------------------------")

#Exercise 3-4: Guest List
#########################
""" 
If you could invite anyone, living or deceased, to dinner, who would you invite? 
Make a list that includes at least three people you’d like to invite to dinner. 
Then use your list to print a message to each person, inviting them to dinner.
"""

inviteList = ["Dad", "Mom", "Father-in-Law"]
inviteText = """ 
It would have been great to have you over the dinner.
Indeed would have loved your company. May Allah give you highest place in Jannah
"""

# Printing the statement 
for invitee in inviteList:
    invitee = "My Dear "+invitee
    print(invitee+", "+inviteText)

print ("=============     Ameen     ================")
print ("")

# Exercise 3-5: Changing Guest List
###################################


inviteText2 = """ 
It would be great to have you over the dinner.
Indeed would love your company.
Stay Blessed
"""

# Printing the statement saying cannot come
print (inviteList[0]+", "+inviteList[1]+" and "+inviteList[2]+" cannot make to the dinner. Will replace with Wife")

# Removing from the list - Deceased
inviteList.pop(int(0)) # with updated list
inviteList.pop(int(0)) # with updated list
inviteList.pop(int(0)) # with updated list

# Adding the living ones
newEntry0 = "Wifey"
inviteList.append(newEntry0)

for invitee in inviteList:
    invitee = "My Dear "+invitee
    print(invitee+", "+inviteText2)

print ("----------------------------------------------------------")
print ("")

#Exercise 3-6: More Guests
##########################

newEntry1 = 'Daughter #1'
newEntry2 = 'Daughter #2'
inviteList.insert(0,newEntry1)
inviteList.append(newEntry2)

for invitee in inviteList:
    invitee = "My Dear "+invitee
    print(invitee+", "+inviteText2)

print ("----------------------------------------------------------")
print("")

# Exercise 3-7: Shrinking Guest List
####################################

print ("Can invite only two people as table is for two only")
print ("")
lastOne = len(inviteList)
inviteList.pop(lastOne-1)

inviteText3 = "You are welcome as priority guests."

for invitee in inviteList:
    invitee = "My Dear "+invitee
    print(invitee+", "+inviteText3)

print ("")
print ("----------------------------------------------------------")


print ("")
print ("Current List")
print (inviteList)
print ("")
lenForQ3_9 = len(inviteList)
del inviteList[0:2]
print ("Emptied List")
print (inviteList)
print ("----------------------------------------------------------")

#################################################################################

placesList = []

num = 5
for no in range(num):
   places = input("Enter the place to visit => ")
   placesList.append(places)

print (placesList) # Original List
print (sorted(placesList,reverse=True)) # Sorted in reverse alphabetically
print (sorted(placesList,reverse=False)) # Sorted Alphabetically
placesList.sort(reverse=True) # Forced list reversed in alphabetical order
print (placesList)
placesList.sort() # Forced list sorted Alphabetically
print (placesList)

print ("")
print ("----------------------------------------------------------")
print ("")

# Exercise 3-9: Dinner Guests
#############################

print ("Total Invitees = "+str(lenForQ3_9))
print ("")
print ("----------------------------------------------------------")
print ("")
# Exercise 3-10: Every Function
###############################

# List, insert(), append(), pop(), sorted(), sort(), len(), del

thingsList = ["K2", "Pakistan", "Riyadh", "Toyota", "Ravi"]

print (thingsList)
thingsList.insert(0,"Margla")
print (thingsList)
thingsList.append("Everest")
print (thingsList)
lenOfThingList = len(thingsList)
print (lenOfThingList)
thingsList.sort()
print (thingsList)
thingsList.sort(reverse=False)
print (sorted(thingsList, reverse=True))
thingsList.pop(0)
print (thingsList)
del thingsList[0:lenOfThingList] # To handle the error for exercise 3.11
print (thingsList)

print ("")
print ("----------------------------------------------------------")
print ("")


# Exercise 3-11: Intentional Error
##################################

# handled above in del function with thingsList
