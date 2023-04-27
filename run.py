print("Welcome to my Sports Quiz!")

confirm = input("Do you want to play? ")

if confirm.lower() != "yes":
    print("Invalid input. Please type 'yes' to play.")
    quit()

print("Lets Play!")

print("An unidentified serial killer horrified London year 1888.")

question = "1. In what city was Jack the Ripper active?\n\
a. Chelsea\n\
b. White Chapel\n\
c. Oxford Street\n\
d. ST. Giles\n\
Enter your answer (a, b, c, or d) : "

answer = input(question)

if answer.lower() == "b":
    print("Correct")
else:
    print("Incorrect. The correct answer is b. White Chapel.")
