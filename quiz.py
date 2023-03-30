# Created by Jonty Weber
# Date 27/02/2023
# Demonstrate asking the user a question, provide multiple choice awnsers, get the user's awnser, check if its correct

# Set a variable called points to 0, this will track how many questions the user has got correct
ValidInputChecker = 0 
points = 0


# This function is called check. We make it conpare awnser with the users input
def check(awnser , user_input):
    if user_input in options and user_input in options[0:1]:
       return True
    else:
       return False

# Ask the user for their name to store it as a variable for later on
name = input ("What is your name?\n\n")
# Asking the user if they want to do the quiz
WantToPlay = input("Hi {} are you ready to start this general knowledge quiz!\n\n".format(name)).lower().strip()


# If the user says no to playing the quiz I will deduct one point from their points variable I created
if WantToPlay == "no":
    points -=1 
    # Then I will tell them the reason why 
    # I have deducted one point of their points variable.
    print("\n\nScince you didnt want to play i will automatically minus one of your points:(")
    print("\nOk lets get started!")
    # If the user has said "yes" this means they want
    # To start the quiz so I dont deduct 1 from the points variable
elif WantToPlay =="yes":
    print("\n\nOk lets get started!")
    # Any other input here is invalid. Or is just a joke,
    # so we tell the user that they have entered somthing else 
    # and deduct one score of the points variable.
else: 
    print("\n\nPlease enter 'yes' or 'no' next time!")
    print("\nI am deducting 1 point for not awnsering!")
    points -=1



# This is Question 1---


# These are the 8 valid inputs the user can enter
options = ["b", "rome", "a", "barcelona", "c", "dubai", "d", "madrid"]
# We create a loop that keeps on looping the code
# if the variable "ValidInputChecker" is below 4
while ValidInputChecker < 4:
    # This is our Question that asks the user the question
    # and puts it to lowercase and strips all unessecary spaces
    Question = input("What city is known as the 'ETERNAL CITY'? \n A) Barcelona \n B) Rome \n C) Dubai \n D) Madrid\n\n>>").lower().strip()
    # We call back to the function to check if the users input is valid
    # And check if its the 1st position,
    # if it is it will run this if statement or be true. 
    if check(options, Question):
        print("You got the right awnser!\n\n")
        # If they have got the right awnser we break the loop and add one point to the "points" variable.
        points += 1
        break
    # If the users input is valid but not in the 1st position
    # (via the right awnser)
    # Then we tell the user that they have the 
    # Wrong awnser and move on while breaking the loop
    # Also not giving them any 
    # points because they have it wrong
    elif Question in options and Question in options[2:]:
        print("Wrong awnser!")
        break
    # If the user has not entered one of these inputs in options, 
    # then their input is invalid and it will run this else statement
    else: 
        # If the user has not entered a valid input then we will loop the code.
        print("Please enter a valid input")
        ValidInputChecker += 1



# This is Question 2---

# These are the 8 valid inputs the user can enter
options = ["b", "sylvestestallone", "a", "tonyburton", "c", "harrisonford", "d", "jasonstatham"]
# We create a loop that keeps on looping the code if the variable
# "ValidInputChecker" is below 4
while ValidInputChecker < 4:
    # This is our Question that asks the user the question 
    # and puts it to lowercase and strips all unessecary spaces
    Question = input ("Which actor played rocky? \n A) Tony Burton \n B) Sylvester Stallone\n C) Harrison Ford\n D) Jason Statham\n\n>> ").lower().strip()
    # We call back to the function to check if the users input is valid
    # And check if its the 1st position, 
    # if it is it will run this if statement or be true. 
    if check(options, Question):
        print("You got the right awnser!\n\n")
        #If they have got the right awnser we break the loop and add one point to the "points" variable.
        points += 1
        break
    # If the users input is valid 
    # but not in the 1st position (via the right awnser)
    # Then we tell the user that they have the 
    # Wrong awnser and move on while breaking the loop
    # Also not giving them any points because they have it wrong
    elif Question in options and Question in options[2:]:
        print("Wrong awnser!")
        break
    # If the user has not entered one of these inputs in options, 
    # then their input is invalid and it will run this else statement
    else: 
        # If the user has not entered a valid input then we will loop the code.
        print("Please enter a valid input")
        ValidInputChecker += 1



# This is Question 3---


# These are the 8 valid inputs the user can enter
options = ["c", "grandcanyon", "b", "kingscanyon", "a", "verdongorge",
 "d", "biggsettiencanyon"]
# We create a loop that keeps on looping the
# code if the variable "ValidInputChecker" is below 4
while ValidInputChecker < 4:
    # This is our Question that asks the user the
    # question and puts it to lowercase and strips all unessecary spaces
    Question = input("What is the largest canyon in the world? \nA) Verdon Gorge\n B) Kings Canyon\n C) Grand Canyon\n D) Biggsettien Canyon\n\n>>").lower().strip()
    # We call back to the function to check if the users input is valid
    # And check if its the 1st position,
    # if it is it will run this if statement or be true.
    if check(options, Question):
        print("You got the right awnser!\n\n")
        # If they have got the right awnser we break the loop and add one point to the "points" variable.
        points += 1
        break
    # If the users input is valid
    # but not in the 1st position (via the right awnser)
    # Then we tell the user that they
    # have the Wrong awnser and move on while breaking the loop
    # Also not giving them any 
    # points because they have it wrong
    elif Question in options and Question in options[2:]:
        print("Wrong awnser!")
        break
    # If the user has not entered one of these inputs in options,
    # then their input is invalid and it will run this else statement
    else: 
        # If the user has not entered a valid input then we will loop the code.
        print("Please enter a valid input")
        ValidInputChecker += 1



# This is Question 4---


# These are the 8 valid inputs the user can enter
options = ["a", "lelouvre", "b", "uffizimuseum", "c", "britishmuseum", "d", "metropolitanmuseumofart" ]
# We create a loop that keeps on looping the code if the variable "ValidInputChecker" is below 4
while ValidInputChecker < 4:
    # This is our Question that asks the user the question and puts it to lowercase and strips all unessecary spaces
    Question = input ("In which museum can you find Leonardo Da Vinci’s Mona Lisa? \nA)Le Louvre  \nB)Uffizi Museum  \nC)British Museum  \nD)Metropolitan Museum of Art\n\n>>").lower().strip()
    # We call back to the function to check if the users input is valid
    # And check if its the 1st position, if it is it will run this if statement or be true. 
    if check(options, Question):
        print("You got the right awnser!\n\n")
        # If they have got the right awnser we break the loop and add one point to the "points" variable.
        points += 1
        break
    # If the users input is valid but not in the 1st position (via the right awnser)
    # Then we tell the user that they have the Wrong awnser and move on while breaking the loop
    # Also not giving them any points because they have it wrong
    elif Question in options and Question in options[2:]:
        print("Wrong awnser!")
        break
    # If the user has not entered one of these inputs in options, then their input is invalid and it will run this else statement
    else: 
        # If the user has not entered a valid input then we will loop the code.
        print("Please enter a valid input")
        ValidInputChecker += 1



# This is Question 5---


# These are the 8 valid inputs the user can enter
options = ["d", "louisxiv", "a", "louisxvi", "c", "charlemange", "d", "francisi"]
# We create a loop that keeps on looping the code if the variable "ValidInputChecker" is below 4
while ValidInputChecker < 4:
    # This is our Question that asks the user the question and puts it to lowercase and strips all unessecary spaces
    Question = input ("Which French king was named the 'Sun king' \nA) LouisXVI \nB) Charlemange\n C) Francis I \n D) LouisXIV ").lower().strip()
    # We call back to the function to check if the users input is valid
    # And check if its the 1st position, if it is it will run this if statement or be true. 
    if check(options, Question):
        print("You got the right awnser!\n\n")
        # If they have got the right awnser we break the loop and add one point to the "points" variable.
        points += 1
        break
    # If the users input is valid but not in the 1st position (via the right awnser)
    # Then we tell the user that they have the Wrong awnser and move on while breaking the loop
    # Also not giving them any points because they have it wrong
    elif Question in options and Question in options[2:]:
        print("Wrong awnser!")
        break
    # If the user has not entered one of these inputs in options, then their input is invalid and it will run this else statement
    else: 
        # If the user has not entered a valid input then we will loop the code.
        print("Please enter a valid input")
        ValidInputChecker += 1



# This is Question 6---


# These are the 4 valid inputs the user can enter
options = options = ["b", "peyo," "a", "morris","c","edgarp.jacobs", "d","hergo"]
# We create a loop that keeps on looping the code if the variable "ValidInputChecker" is below 4
while ValidInputChecker < 4:
    # This is our Question that asks the user the question and puts it to lowercase and strips all unessecary spaces
    Question = input ("Which artist and author made the Smurfs comic strips? \nA)Hergé  \nB)Peyo  \nC)Morris \nD)Edgar P. Jacobs \n\n>>").lower().strip()
    # We call back to the function to check if the users input is valid
    # And check if its the 1st position, if it is it will run this if statement or be true. 
    if check(options, Question):
        print("You got the right awnser!\n\n")
        # If they have got the right awnser we break the loop and add one point to the "points" variable.
        points += 1
        break
    # If the users input is valid but not in the 1st position (via the right awnser)
    # Then we tell the user that they have the Wrong awnser and move on while breaking the loop
    # Also not giving them any points because they have it wrong
    elif Question in options and Question in options[2:]:
        print("Wrong awnser!")
        break
    # If the user has not entered one of these inputs in options, then their input is invalid and it will run this else statement
    else: 
        # If the user has not entered a valid input then we will loop the code.
        print("Please enter a valid input")
        ValidInputChecker += 1



# This is Question 7---


# These are the 8 valid inputs the user can enter
options = ["d", "6", "a", "4", "c", "3", "b", "1"]
# We create a loop that keeps on looping the code if the variable "ValidInputChecker" is below 4
while ValidInputChecker < 4:
    # This is our Question that asks the user the question and puts it to lowercase and strips all unessecary spaces
    Question = input("How many wives had Henry VIII? \nA)1 \nB)3 \nC)4 \nD)6\n\n>> ").lower().strip()
    # We call back to the function to check if the users input is valid
    # And check if its the 1st position, if it is it will run this if statement or be true. 
    if check(options, Question):
        print("You got the right awnser!\n\n")
        # If they have got the right awnser we break the loop and add one point to the "points" variable.
        points += 1
        break
    # If the users input is valid but not in the 1st position (via the right awnser)
    # Then we tell the user that they have the Wrong awnser and move on while breaking the loop
    # Also not giving them any points because they have it wrong
    elif Question in options and Question in options[2:]:
        print("Wrong awnser!")
        break
    # If the user has not entered one of these inputs in options, then their input is invalid and it will run this else statement
    else: 
        # If the user has not entered a valid input then we will loop the code.
        print("Please enter a valid input")
        ValidInputChecker += 1



# This is Question 8---


# These are the 8 valid inputs the user can enter
options = ["b", "1605", "a", "1505", "c", "1705", "d", "1805"]
# We create a loop that keeps on looping the code if the variable "ValidInputChecker" is below 4
while ValidInputChecker < 4:
    # This is our Question that asks the user the question and puts it to lowercase and strips all unessecary spaces
    Question = input ("When were Guy Fawkes and The Gunpowder Plot discovered? \nA)1505 \nB)1605 \nC)1705 \nD)1805 \n\n>> ").lower().strip()
    # We call back to the function to check if the users input is valid
    # And check if its the 1st position, if it is it will run this if statement or be true. 
    if check(options, Question):
        print("You got the right awnser!\n\n")
        #If they have got the right awnser we break the loop and add one point to the "points" variable.
        points += 1
        break
    # If the users input is valid but not in the 1st position (via the right awnser)
    # Then we tell the user that they have the Wrong awnser and move on while breaking the loop
    # Also not giving them any points because they have it wrong
    elif Question in options and Question in options[2:]:
        print("Wrong awnser!")
        break
    # If the user has not entered one of these inputs in options, then their input is invalid and it will run this else statement
    else: 
        # If the user has not entered a valid input then we will loop the code.
        print("Please enter a valid input")
        ValidInputChecker += 1




# This is Question 9---


# These are the 8 valid inputs the user can enter
options = ["b", "jfk", "a", "martinlutherking", "c", "mkgandhi" ,"d","malcolmx"]
# We create a loop that keeps on looping the code if the variable "ValidInputChecker" is below 4
while ValidInputChecker < 4:
    # This is our Question that asks the user the question and puts it to lowercase and strips all unessecary spaces
    Question = input("Who was assassinated on the 22nd of November 1963? \nA)Martin Luther King \nB)JFK \nC)MK Gandhi \nD)Malcolm X \n\n>>").lower().strip()
    # We call back to the function to check if the users input is valid
    # And check if its the 1st position, if it is it will run this if statement or be true. 
    if check(options, Question):
        print("You got the right awnser!\n\n")
        # If they have got the right awnser we break the loop and add one point to the "points" variable.
        points += 1
        break
    # If the users input is valid but not in the 1st position (via the right awnser)
    # Then we tell the user that they have the Wrong awnser and move on while breaking the loop
    # Also not giving them any points because they have it wrong
    elif Question in options and Question in options[2:]:
        print("Wrong awnser!")
        break
    # If the user has not entered one of these inputs in options, then their input is invalid and it will run this else statement
    else: 
        # If the user has not entered a valid input then we will loop the code.
        print("Please enter a valid input")
        ValidInputChecker += 1




# This is Question 10---


# These are the 4 valid inputs that the user can enter
options = ["d","mathemtitian","a","philosopher","c","poet","b","painter"]
# We create a loop that keeps on looping the code if the variable "ValidInputChecker" is below 4
while ValidInputChecker < 4:
    # This is our Question that asks the user the question and puts it to lowercase and strips all unessecary spaces
    Question = input ("What was Euclid? \nA) philosopher \nB) poet \nC)painter \nD)mathematician\n\n>> ").lower().strip()
    # We call back to the function to check if the users input is valid
    # And check if its the 1st position, if it is it will run this if statement or be true. 
    if check(options, Question):
        print("You got the right awnser!\n\n")
        # If they have got the right awnser we break the loop and add one point to the "points" variable.
        points += 1
        break
    # If the users input is valid but not in the 1st position (via the right awnser)
    # Then we tell the user that they have the Wrong awnser and move on while breaking the loop
    # Also not giving them any points because they have it wrong
    elif Question in options and Question in options[2:]:
        print("Wrong awnser!")
        break
    # If the user has not entered one of these inputs in options, then their input is invalid and it will run this else statement
    else: 
        # If the user has not entered a valid input then we will loop the code.
        print("Please enter a valid input")
        ValidInputChecker += 1



# Telling the user how many they got right
print("Congrats you got {} right!\n\n".format(points))



# If the user got less then 5 of the questions correct we tell them they got a rating of D
if int(points < 5):
    print("Rating : D")
# Else if the user has got 6 points we tell them they got a C rating and passed
elif int(points == 6):
    print("PASSED: rating : C")
# Else if the user has got 7 points we tell them they got a C+ rating and passed
elif int(points == 7):
    print("PASSED: rating : C+")
# Else if the user has got 8 points we tell them they got a B rating and passed
elif int(points == 8):
    print("PASSED: rating : B")
# Else if the user has got 9 points we tell them they got a A rating and passed
elif int(points == 9):
    print("PASSED: rating : A")
# Else if the user has got 10 points we tell them they got a perfect score or got all of them right
elif int(points == 10):
    print("PERFECT SCORE!!!! WELL DONE")

