# Week 1 assignmment - trivia

import time


#### Introductions

print()
time.sleep(1)
print("Hello and Welcome to the amazing world of Aussie trivia.")
time.sleep(2)

print()
print("Let's introduce each other first. My name is Bruce!")
time.sleep(2)

print()
print("What is your name?")
time.sleep(1)

print()
name = input("Please type your name here: ")
print()

for i in range(2):    # show 2 rows of the word "Processing" before moving onto the next section
    print("Processing...")
    time.sleep(1)

print()
print(f"Welcome, {name}. It is a pleasure to meet you!")
print()
time.sleep(3)


#### Set scores to zero

correct = 0
incorrect = 0


#### Let's get started with some trivia

print("Let's get started!")
print()
time.sleep(2)

#### Question 1: Construct a dictionary 

question1 = {"1" : "Nowhere Else, Tasmania", 
            "2" : "Useless Inlet, Western Australia", 
            "3" : "Humpty Doo, Northern Territory", 
            "4" : "Yorkey's Knob, Queensland", 
            "5" : "Pointless Bay, Victoria", 
            "6" : "Come By Chance, New South Wales"}


#### Question 1: Print out the options (dictionary)

print("Question 1: Which of these is not a real place in Australia?")
print()
for question, answer in question1.items():
    print(f"{question}: {answer}")

print()
answer1 = input("Enter your choice (1-6): ")
print()

#### Question 1: Score the question

answer1 = int(answer1)    # Make sure the string entered by the user is changed to an integer
if answer1 == 5:
    print("Correct!")
    correct += 1    # Increment their score if they get the answer correct
else:
    print("Sorry champ...")
    time.sleep(1)
    print()
    print("The answer is '5. Pointless Bay, Victoria'")
    incorrect -= 1

time.sleep(2)
print()

#### Question 2

for i in range(2):    # show 2 rows of the word "Processing" before moving onto the next section
    print("Processing...")
    time.sleep(1)

print()
print("Question 2: Read this internet review and try to guess the Australian attraction... ")

print()
time.sleep(2)

print("Review #1... \n 'Damned waste of money from it’s inception. Too far from the city proper and more often than not, the shows are elitist rubbish. Poor parking!'")

print()
answer1 = input("What attraction is this? ... ")
print()
if answer1.lower() == 'sydney opera house':
    print("Correct!")
    correct += 1    # Increment their score if they get the answer correct
else:
    print("Sorry champ...")
    time.sleep(1)
    print()
    print("The answer is 'Sydney Opera House'")
    incorrect -= 1

time.sleep(2)
print()




#### Do a tally of scores

print()
print("Correct answers: " + str(correct))
print("Incorrect answers: " + str(incorrect))

total_score = incorrect - correct
print("Total score: " + str(total_score))

print()









