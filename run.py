print("Welcome to my Mysteries Quiz!")

confirm = input("Do you want to play? ")

if confirm.lower() != "yes":
    print("Invalid input. Please type 'yes' to play.")
    quit()

print("Lets Play!")

print("An unidentified serial killer horrified London year 1888.")

question = "1. In what London district was Jack the Ripper active?\n\
a. Chelsea\n\
b. White Chapel\n\
c. Oxford Street\n\
d. ST. Giles\n\
Enter your answer (a, b, c, or d): "

answer = input(question)

if answer.lower() == "b":
    print("Correct")
else:
    print("Incorrect. The correct answer is b. White Chapel.")

print("Passanger flight MH370 went missing in 2014 with 227 passengers onboard")

question = "2. By wich country's airlines was the plane operated?\n\
a. Malaysia\n\
b. China\n\
c. Thailand\n\
d. Singapore\n\
Enter your answer (a, b, c, or d): "

answer = input(question)

if answer.lower() == "a":
    print("Correct")
else:
    print("Incorrect. The correct answer is a. Malaysia.")

print("Winston Churchill defined something as 'a riddle, wrapped in a mystery, inside an enigma")

question = "3. What was Churchill talking about??\n\
a. Mathematics\n\
b. Programming\n\
c. Russia\n\
d. The Bermuda Triangle\n\
Enter your answer (a, b, c, or d): "

answer = input(question)

if answer.lower() == "c":
    print("Correct")
else:
    print("Incorrect. The correct answer is c. Russia.")

print("'Sweet little mystery' is the second single from a group's first album in July 1987.")

question = "1. What's the name of the group?\n\
a. Oasis\n\
b. Red hot Chilli Peppers\n\
c. The Smashing Pumpkins\n\
d. Wet Wet Wet\n\
Enter your answer (a, b, c, or d): "

answer = input(question)

if answer.lower() == "d":
    print("Correct")
else:
    print("Incorrect. The correct answer is d. Wet Wet Wet.")



