def new_game():
    guesses = []
    correct_guess = 0
    question_num = 1

    for key in questions:
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter your answer (A,B,C, or D): ")
        guess = guess.upper()
        guesses.append(guess)
        question_num+= 1
def check_answer():
    pass
def display_score():
    pass
def play_again():
    pass

questions = {
"who created python? ": "A",
"what year was the python created? ": "B",
"python is tributed to which comedy group? ": "C",
"is the earth round? ": "A"
}

options = [["A. Guiod ven rossum", "B. elon mask", "C. bill gates", "D. mark zuckerburg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. lonely", "B. smosh", "C. monty python", "D. SNL"],
           ["A. true", "B. false", "C. sometimes", "D.idk"]]

new_game()