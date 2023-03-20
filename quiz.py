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
name = input ("What is your name?")
#Asking the user if they want to do the quiz
WantToPlay = input("Hi {} are you ready to start this general knowledge quiz!".format(name)).lower()


#If the user says no to playing the quiz I will deduct one point from their points variable I created
if WantToPlay == "no":
    points -=1 
    #Then I will tell them the reason why I have deducted one point of their points variable.
    print("Scince you didnt want to play i will automatically minus one of your points:(")
    print("Ok lets get started!")
    #If the user has said "yes" this means they want to start the quiz so I dont deduct 1 from the points variable
elif WantToPlay =="yes":
    print("Ok lets get started!")
    #Any other input here is invalid. Or is just a joke, so we tell the user that they have entered somthing else and deduct one score of the points variable.
else: 
    print("Please enter 'yes' or 'no' next time!")
    print("I am deducting 1 point for not awnsering!")
    points -=1


#This is Question 1
#The options here are the correct awnsers.
options = ["rome".lower() , "b".lower()]
#We ask the user the question and store it in a "Question" variable
Question = input("What city is known as the 'ETERNAL CITY'? \n A) Barcelona \n B) Rome \n C) Dubai \n D) Madrid\n>>").lower()

#Run the function we created and check if the options is the same as the variable inputted for "Question"
if check(options, Question):
    #If it is then tell the user they got the question right and add one to the "points" variable
    print("You got the right awnser!")
    points += 1
else:
    #If the user has not entered anything in the options variable they have the awnser wrong so we dont add score 
    #And we tell them that they have the wrong awnser
    print("Wrong awnser!")


#This is Question 2
#The options here are the correct awnsers.
options = [ "sylvester stallone".lower() , "b".lower()]
#We ask the user the question and store it in a "Question" variable
Question = input ("Which actor played rocky? \n A) Tony Burton \n B) Sylvester Stallone\n C) Harrison Ford\n D) Jason Statham\n>> ").lower()

#Run the function we created and check if the options is the same as the variable inputted for "Question"
if check(options, Question):
    #If it is then tell the user they got the question right and add one to the "points" variable
    print("You got the right awnser!")
    points += 1
else:
    #If the user has not entered anything in the options variable they have the awnser wrong so we dont add score 
    #And we tell them that they have the wrong awnser
    print("You got the wrong awnser")


#This is Question 3
#The options here are the correct awnsers.
options = [ "grand canyon".lower() , "c".lower()]
#We ask the user the question and store it in a "Question" variable
Question = input("What is the largest canyon in the world? \nA) Verdon Gorge\n B) Kings Canyon\n C) Grand Canyon\n D) Biggsettien Canyon\n>>").lower()

#Run the function we created and check if the options is the same as the variable inputted for "Question"
if check(options, Question):
    #If it is then tell the user they got the question right and add one to the "points" variable
    print("You got the right awnser!")
    points += 1
else:
    #If the user has not entered anything in the options variable they have the awnser wrong so we dont add score 
    #And we tell them that they have the wrong awnser
    print("Wrong awnser!")


#This is Question 4
#The options here are the correct awnsers.
options = ["a".lower() , "louvre".lower() , "le lourve".lower()]
#We ask the user the question and store it in a "Question" variable
Question = input ("In which museum can you find Leonardo Da Vinci’s Mona Lisa? \nA)Le Louvre  \nB)Uffizi Museum  \nC)British Museum  \nD)Metropolitan Museum of Art\n>>").lower()

#Run the function we created and check if the options is the same as the variable inputted for "Question"
if check(options, Question):
    #If it is then tell the user they got the question right and add one to the "points" variable
    print("You got the right awnser!")
    points += 1
else:
    #If the user has not entered anything in the options variable they have the awnser wrong so we dont add score 
    #And we tell them that they have the wrong awnser
    print("You got the wrong awnser")


#This is Question 5
#The options here are the correct awnsers.
options = ["louis xiv".lower() , "d".lower()]
#We ask the user the question and store it in a "Question" variable
Question = input("Which French king was nicknamed the “Sun King”? \nA)Louis XVI \nB)Charlemagne \nC)Francis I \nD)Louis XIV \n>>").lower()

#Run the function we created and check if the options is the same as the variable inputted for "Question"
if check(options, Question):
    #If it is then tell the user they got the question right and add one to the "points" variable
    print("You got the right awnser!")
    points += 1
else:
    #If the user has not entered anything in the options variable they have the awnser wrong so we dont add score 
    #And we tell them that they have the wrong awnser
    print("Wrong awnser!")


#This is Question 6
#The options here are the correct awnsers.
options = ["peyo".lower() , "b".lower()]
#We ask the user the question and store it in a "Question" variable
Question = input ("Which artist and author made the Smurfs comic strips? \nA)Hergé  \nB)Peyo  \nC)Morris \nD)Edgar P. Jacobs \n>>").lower()

#Run the function we created and check if the options is the same as the variable inputted for "Question"
if check(options, Question):
    #If it is then tell the user they got the question right and add one to the "points" variable
    print("You got the right awnser!")
    points += 1
else:
    print("You got the wrong awnser")


#This is Question 7
#The options here are the correct awnsers.
options = ["d".lower() , "6".lower()]
#We ask the user the question and store it in a "Question" variable
Question = input("How many wives had Henry VIII? \nA)1 \nB)3 \nC)4 \nD)6\n>> ").lower()

#Run the function we created and check if the options is the same as the variable inputted for "Question"
if check(options, Question):
    #If it is then tell the user they got the question right and add one to the "points" variable
    print("You got the right awnser!")
    points += 1
else:
    #If the user has not entered anything in the options variable they have the awnser wrong so we dont add score 
    #And we tell them that they have the wrong awnser
    print("Wrong awnser!")


#This is Question 8
#The options here are the correct awnsers.
options = ["1605".lower() , "b".lower()]
#We ask the user the question and store it in a "Question" variable
Question = input ("When were Guy Fawkes and The Gunpowder Plot discovered? \nA)1505 \nB)1605 \nC)1705 \nD)1805 \n>> ").lower() 

#Run the function we created and check if the options is the same as the variable inputted for "Question"
if check(options, Question):
    #If it is then tell the user they got the question right and add one to the "points" variable
    print("You got the right awnser!")
    points += 1
else:
    #If the user has not entered anything in the options variable they have the awnser wrong so we dont add score 
    #And we tell them that they have the wrong awnser
    print("You got the wrong awnser")


#This is Question 9
#The options here are the correct awnsers.
options = ["b".lower() , "jfk".lower() , "jhon f kennedy".lower()]
#We ask the user the question and store it in a "Question" variable
Question = input("Who was assassinated on the 22nd of November 1963? \nA)Martin Luther King \nB)JFK \nC)MK Gandhi \nD)Malcolm X \n>>").lower()

#Run the function we created and check if the options is the same as the variable inputted for "Question"
if check(options, Question):
    #If it is then tell the user they got the question right and add one to the "points" variable
    print("You got the right awnser!")
    points += 1
else:
    #If the user has not entered anything in the options variable they have the awnser wrong so we dont add score 
    #And we tell them that they have the wrong awnser
    print("Wrong awnser!")


#This is Question 10
#The options here are the correct awnsers.
options = ["mathmatician".lower() , "d".lower()]
#We ask the user the question and store it in a "Question" variable
Question = input ("What was Euclid? \nA) philosopher \nB) poet \nC)painter \nD)mathematician\n>> ").lower()

#Run the function we created and check if the options is the same as the variable inputted for "Question"
if check(options, Question):
    #If it is then tell the user they got the question right and add one to the "points" variable
    print("You got the right awnser!")
    points += 1
else:
    #If the user has not entered anything in the options variable they have the awnser wrong so we dont add score 
    #And we tell them that they have the wrong awnser
    print("You got the wrong awnser")

#Telling the user how many they got right
print("Congrats you got {} right!".format(points))

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