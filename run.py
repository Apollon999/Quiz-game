import time

def get_valid_input(options):
    """
    This function repeatedly prompts the user to enter 
    an option until a valid input is provided. It returns the valid input.
    """
    while true:
        user_input = input("Enter your answer ({}): ".format(", ".join(options)))
        if user_input.lower() in options:
            return user_input.lower()
        print("Invalid input. Please enter one of the following options: {}.".format(", ".join(options)))

print("Welcome to my Mysteries Quiz!")

confirm = input("Do you want to play? ")

while confirm.lower() != "yes":
    confirm = input("Invalid input. Please type 'yes' to play.")

print("The Quiz begins in 5 seconds...")
time.sleep(5)    

print("Lets Play!")

start_time = time.time()

score = 0

print("(1 Point) An unidentified serial killer horrified London year 1888.")

question = "1. In what London district was Jack the Ripper active?\n\
a. Chelsea\n\
b. White Chapel\n\
c. Oxford Street\n\
d. ST. Giles\n\
Enter your answer (a, b, c, or d): "

answer = input(question)

while answer.lower() not in ["a", "b", "c", "d"]:
    answer = input("Invalid input. Please enter a, b, c, or d." )

if answer.lower() == "b":
    print("Correct")
    score += 1 
else:
    print("Incorrect. The correct answer is b. White Chapel.")

print("(1 Point)Flight MH370 went missing in 2014 with 227 passengers onboard.")

question = "2. By wich country's airlines was the plane operated?\n\
a. Malaysia\n\
b. China\n\
c. Thailand\n\
d. Singapore\n\
Enter your answer (a, b, c, or d): "

answer = input(question)

while answer.lower() not in ["a", "b", "c", "d"]:
    answer = input("Invalid input. Please enter a, b, c, or d." )

if answer.lower() == "a":
    print("Correct")
    score += 1
else:
    print("Incorrect. The correct answer is a. Malaysia.")

print("(2 Points)'a riddle, wrapped in a mystery, inside an enigma'.")

question = "3. What was Winston Churchill talking about??\n\
a. Mathematics\n\
b. Programming\n\
c. Russia\n\
d. The Bermuda Triangle\n\
Enter your answer (a, b, c, or d): "

answer = input(question)

while answer.lower() not in ["a", "b", "c", "d"]:
    answer = input("Invalid input. Please enter a, b, c, or d." )

if answer.lower() == "c":
    print("Correct")
    score += 2
else:
    print("Incorrect. The correct answer is c. Russia.")

print("(2 Points)'Sweet little mystery' is a single made in July 1987.")

question = "1. What's the name of the group?\n\
a. Oasis\n\
b. Red hot Chilli Peppers\n\
c. The Smashing Pumpkins\n\
d. Wet Wet Wet\n\
Enter your answer (a, b, c, or d): "

answer = input(question)

while answer.lower() not in ["a", "b", "c", "d"]:
    answer = input("Invalid input. Please enter a, b, c, or d." )

if answer.lower() == "d":
    print("Correct")
    score += 2
else:
    print("Incorrect. The correct answer is d. Wet Wet Wet.")

end_time = time.time()

total_time = end_time - start_time

print("You completed the Quiz in {:.2f} seconds. Awasome!".format(total_time))

print("Your score is: {} out of 6.".format(score))



