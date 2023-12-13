from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create a variable to hold list of questions and answers
question_bank = []
# Grab each key and add them to the list using the method from the Question class
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
# Ask user the questions
quiz = QuizBrain(question_bank)

# Check if quiz still has questions remaining
while quiz.still_has_questions():
    quiz.next_question()
    # Check if the answer was correct
    if quiz.next_question():
        print("You got it!")