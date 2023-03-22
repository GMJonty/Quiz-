#Created by Jonty Weber
#Date 27/02/2023
#Demonstrate asking the user a question, provide multiple choice awnsers, get the user's awnser, check if its correct

#Set a variable called points to 0, this will track how many questions the user has got correct
points = 0

#This function is called check. We make it conpare awnser with the users input
def check(awnser , user_input):
    #If the users input is in the options I return true
    if user_input in options:
       return True
    #If the users input is not in the options I return false
    else:
       return False


#Ask the user for their name to store it as a variable for later on
name = input ("What is your name?\n\n")
#Asking the user if they want to do the quiz
WantToPlay = input("Hi {} are you ready to start this general knowledge quiz!\n\n".format(name)).lower().strip()


#If the user says no to playing the quiz I will deduct one point from their points variable I created
if WantToPlay == "no":
    points -=1 
    #Then I will tell them the reason why I have deducted one point of their points variable.
    print("\n\nScince you didnt want to play i will automatically minus one of your points:(")
    print("\nOk lets get started!")
    #If the user has said "yes" this means they want to start the quiz so I dont deduct 1 from the points variable
elif WantToPlay =="yes":
    print("\n\nOk lets get started!")
    #Any other input here is invalid. Or is just a joke, so we tell the user that they have entered somthing else and deduct one score of the points variable.
else: 
    print("\n\nPlease enter 'yes' or 'no' next time!")
    print("\nI am deducting 1 point for not awnsering!")
    points -=1


#This is Question 1
#The options here are the correct awnsers.
options = ["rome".lower().strip() , "b".lower().strip()]
#We ask the user the question and store it in a "Question" variable
Question = input("What city is known as the 'ETERNAL CITY'? \n A) Barcelona \n B) Rome \n C) Dubai \n D) Madrid\n\n>>").lower().strip()

#Run the function we created and check if the options is the same as the variable inputted for "Question"
if check(options, Question):
    #If it is then tell the user they got the question right and add one to the "points" variable
    print("You got the right awnser!\n\n")
    points += 1
else:
    #If the user has not entered anything in the options variable they have the awnser wrong so we dont add score 
    #And we tell them that they have the wrong awnser
    print("Wrong awnser!\n\n")


#This is Question 2
#The options here are the correct awnsers.
options = [ "sylvester stallone".lower().strip() , "b".lower().strip()]
#We ask the user the question and store it in a "Question" variable
Question = input ("Which actor played rocky? \n A) Tony Burton \n B) Sylvester Stallone\n C) Harrison Ford\n D) Jason Statham\n\n>> ").lower().strip()

#Run the function we created and check if the options is the same as the variable inputted for "Question"
if check(options, Question):
    #If it is then tell the user they got the question right and add one to the "points" variable
    print("You got the right awnser!\n\n")
    points += 1
else:
    #If the user has not entered anything in the options variable they have the awnser wrong so we dont add score 
    #And we tell them that they have the wrong awnser
    print("You got the wrong awnser\n\n")


#This is Question 3
#The options here are the correct awnsers.
options = [ "grand canyon".lower().strip() , "c".lower().strip()]
#We ask the user the question and store it in a "Question" variable
Question = input("What is the largest canyon in the world? \nA) Verdon Gorge\n B) Kings Canyon\n C) Grand Canyon\n D) Biggsettien Canyon\n\n>>").lower().strip()

#Run the function we created and check if the options is the same as the variable inputted for "Question"
if check(options, Question):
    #If it is then tell the user they got the question right and add one to the "points" variable
    print("You got the right awnser!\n\n")
    points += 1
else:
    #If the user has not entered anything in the options variable they have the awnser wrong so we dont add score 
    #And we tell them that they have the wrong awnser
    print("Wrong awnser!\n\n")


#This is Question 4
#The options here are the correct awnsers.
options = ["a".lower().strip() , "louvre".lower().strip() , "le lourve".lower().strip()]
#We ask the user the question and store it in a "Question" variable
Question = input ("In which museum can you find Leonardo Da Vinci’s Mona Lisa? \nA)Le Louvre  \nB)Uffizi Museum  \nC)British Museum  \nD)Metropolitan Museum of Art\n\n>>").lower().strip()

#Run the function we created and check if the options is the same as the variable inputted for "Question"
if check(options, Question):
    #If it is then tell the user they got the question right and add one to the "points" variable
    print("You got the right awnser!\n\n")
    points += 1
else:
    #If the user has not entered anything in the options variable they have the awnser wrong so we dont add score 
    #And we tell them that they have the wrong awnser
    print("You got the wrong awnser\n\n")


#This is Question 5
#The options here are the correct awnsers.
options = ["louis xiv".lower().strip() , "d".lower().strip()]
#We ask the user the question and store it in a "Question" variable
Question = input("Which French king was nicknamed the “Sun King”? \nA)Louis XVI \nB)Charlemagne \nC)Francis I \nD)Louis XIV \n\n>>").lower().strip()

#Run the function we created and check if the options is the same as the variable inputted for "Question"
if check(options, Question):
    #If it is then tell the user they got the question right and add one to the "points" variable
    print("You got the right awnser!\n\n")
    points += 1
else:
    #If the user has not entered anything in the options variable they have the awnser wrong so we dont add score 
    #And we tell them that they have the wrong awnser
    print("Wrong awnser!\n\n")


#This is Question 6
#The options here are the correct awnsers.
options = ["peyo".lower().strip() , "b".lower().strip()]
#We ask the user the question and store it in a "Question" variable
Question = input ("Which artist and author made the Smurfs comic strips? \nA)Hergé  \nB)Peyo  \nC)Morris \nD)Edgar P. Jacobs \n\n>>").lower().strip()

#Run the function we created and check if the options is the same as the variable inputted for "Question"
if check(options, Question):
    #If it is then tell the user they got the question right and add one to the "points" variable
    print("You got the right awnser!\n\n")
    points += 1
else:
    print("You got the wrong awnser\n\n")


#This is Question 7
#The options here are the correct awnsers.
options = ["d".lower().strip() , "6".lower().strip()]
#We ask the user the question and store it in a "Question" variable
Question = input("How many wives had Henry VIII? \nA)1 \nB)3 \nC)4 \nD)6\n\n>> ").lower().strip()

#Run the function we created and check if the options is the same as the variable inputted for "Question"
if check(options, Question):
    #If it is then tell the user they got the question right and add one to the "points" variable
    print("You got the right awnser!\n\n")
    points += 1
else:
    #If the user has not entered anything in the options variable they have the awnser wrong so we dont add score 
    #And we tell them that they have the wrong awnser
    print("Wrong awnser!\n\n")


#This is Question 8
#The options here are the correct awnsers.
options = ["1605".lower().strip() , "b".lower().strip()]
#We ask the user the question and store it in a "Question" variable
Question = input ("When were Guy Fawkes and The Gunpowder Plot discovered? \nA)1505 \nB)1605 \nC)1705 \nD)1805 \n\n>> ").lower().strip()

#Run the function we created and check if the options is the same as the variable inputted for "Question"
if check(options, Question):
    #If it is then tell the user they got the question right and add one to the "points" variable
    print("You got the right awnser!\n\n")
    points += 1
else:
    #If the user has not entered anything in the options variable they have the awnser wrong so we dont add score 
    #And we tell them that they have the wrong awnser
    print("You got the wrong awnser\n\n")


#This is Question 9
#The options here are the correct awnsers.
options = ["b".lower().strip() , "jfk".lower().strip() , "jhon f kennedy".lower().strip()]
#We ask the user the question and store it in a "Question" variable
Question = input("Who was assassinated on the 22nd of November 1963? \nA)Martin Luther King \nB)JFK \nC)MK Gandhi \nD)Malcolm X \n\n>>").lower().strip()

#Run the function we created and check if the options is the same as the variable inputted for "Question"
if check(options, Question):
    #If it is then tell the user they got the question right and add one to the "points" variable
    print("You got the right awnser!\n\n")
    points += 1
else:
    #If the user has not entered anything in the options variable they have the awnser wrong so we dont add score 
    #And we tell them that they have the wrong awnser
    print("Wrong awnser!\n\n")


#This is Question 10
#The options here are the correct awnsers.
options = ["mathmatician".lower().strip() , "d".lower().strip()]
#We ask the user the question and store it in a "Question" variable
Question = input ("What was Euclid? \nA) philosopher \nB) poet \nC)painter \nD)mathematician\n\n>> ").lower().strip()

#Run the function we created and check if the options is the same as the variable inputted for "Question"
if check(options, Question):
    #If it is then tell the user they got the question right and add one to the "points" variable
    print("You got the right awnser!\n\n")
    points += 1
else:
    #If the user has not entered anything in the options variable they have the awnser wrong so we dont add score 
    #And we tell them that they have the wrong awnser
    print("You got the wrong awnser\n\n")

#Telling the user how many they got right
print("Congrats you got {} right!\n\n".format(points))

#If the user got less then 5 of the questions correct we tell them they got a rating of D
if int(points < 5):
    print("Rating : D")
#Else if the user has got 6 points we tell them they got a C rating and passed
elif int(points == 6):
    print("PASSED: rating : C")
#Else if the user has got 7 points we tell them they got a C+ rating and passed
elif int(points == 7):
    print("PASSED: rating : C+")
#Else if the user has got 8 points we tell them they got a B rating and passed
elif int(points == 8):
    print("PASSED: rating : B")
#Else if the user has got 9 points we tell them they got a A rating and passed
elif int(points == 9):
    print("PASSED: rating : A")
#Else if the user has got 10 points we tell them they got a perfect score or got all of them right
elif int(points == 10):
    print("PERFECT SCORE!!!! WELL DONE")

