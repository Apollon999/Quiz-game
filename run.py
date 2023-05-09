import time

def get_valid_input(options):
    """
    This function repeatedly prompts the user to enter 
    an option until a valid input is provided. It returns the valid input.
    """
    while True:
        user_input = input("Enter your answer ({}): ".format(", ".join(options)))
        if user_input.lower() in options:
            return user_input.lower()
        print("Invalid input. Please enter one of the following options: {}.".format(", ".join(options)))

def ask_question(question, options, correct_answer, points):
    """
    This function takes a question, a list of options, the 
    correct answer, and the number of points the question 
    is worth as an input. It displays the questions
    and options to the user, prompts them to enter
    an answer, validates the input, and returns the score 
    based on wether the answer is correct or not.
    """
    print("({} point) {}".format(points, question))
    for i in range(len(options)):
        print("{}. {}".format(chr(i+97), options[i]))
    answer = get_valid_input([chr(i+97) for i in range(len(options))])
    if answer == correct_answer:
        print("correct")
        return points
    else: 
        print("Incorrect. The correct answer is {}.".format(correct_answer.upper()))
        return 0

def play_quiz():
    """
    This function contains the main game loop for the quiz.
    It displays the welcome message and prompts the user to
    start the game. It then asks a series of questions and
    keeps track of the score. Finally, it displays the score
    and the total time taken to complete the quiz.
    """

print("Welcome to my Mysteries Quiz!")
confirm = input("Do you want to play? ")
while confirm.lower() != "yes":
    confirm = input("Invalid input. Please type 'yes' to play.")
print("The Quiz begins in 5 seconds...")
time.sleep(5)    
print("Lets Play!")
start_time = time.time()
score = 0
score += ask_question("In what London district was Jack the Ripper active?", ["Chelsea", "White Chapel", "Oxford Street", "ST Giles"], "b", 1)
score += ask_question("By which country's airlines was Flight MH370 operated?", ["Malaysia", "China", "Thailand", "Singapore"], "a", 1)
score += ask_question("What was Winston Churchill talking about when he said 'a riddle, wrapped in a mystery, inside an enigma'?", ["Mathematics", "Programming", "Russia", "China"], "c", 2)
score += ask_question("'Sweet little mystery' is a single made in July 1987 by which group?", ["Oasis", "Red Hot Chilli Peppers", "The Smashing Pumpkins", "Wet Wet Wet"], "d", 2)
end_time = time.time()
total_time = end_time - start_time
print("You completed the Quiz in {:.2f} seconds. Awesome!".format(total_time))
print("Your score is: {} out of 6.".format(score))

play_quiz()