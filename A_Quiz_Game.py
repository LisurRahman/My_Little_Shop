# A Quiz Game
name = input("Enter your name:")
print(f"Asalamualikum Dear '{name}'.Welcome to the quiz game.")

# Give some question

questions = ("Our national Fruit is ___?",
            "Our national Tree is ___?",
            "Our national Poet is ___?",
            "Our national Fish is ___?",
            "Our national Flower is ___?")
# Give options
options = (("A. Mango", "B. Banana", "C. Jackfruit", "D. Guava"),
           ("A. Mango Tree", "B. Banana Tree", "C. Lichi Tree", "D. Black Bary Tree"),
           ("A. Kaji Najrul", "B. Jashim Uddin", "C. Jebon Anando", "D. Motahir Hosen"),
           ("A. Barb", "B. Climbing parch", "C. Rohu", "D. Hilsa"),
           ("A. Rose", "B.Lily ", "C. Jasmin", "D. Tulip"))

# Answers of question
answers = ("C", "A", "A", "D", "B")

# Important tools
score = 0
guesses = []
question_num = 0


# Question and Answer showing
for question in questions:
    print("__________________________")
    print(question) # Question show

    for option in options[question_num]:
        print(option) # Option show

    guess = input("Choose the correct answer from [A, B, C, D]:  ").upper() # Take answer
    guesses.append(guess)
    if guess == answers[question_num]: # Wishing condition
        score += 2
        print("   Congratulation.  \n This is correct Answer !")
    else:
        print(f"Wrong answer.Correct answer is |{answers[question_num]}|")

    question_num += 1 # Swap question and answer

print(f"Your score is: [{score}]") # Score showing

# Reword
if score >= 6: 
    print("Good job.You are a topper boy.")
else:
    print("Ok. No problem, I wish that you will do better in next time.")
