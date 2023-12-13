from question_model import Question
from data import question_data

# Create a variable to hold list of questions and answers
question_bank = []
# Grab each key and add them to the list using the method from the Question class
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
# TODO: Ask user the questions

# TODO: Check if the answer was correct

# TODO: Check if we're at the end of the quiz
print(question_bank[0].text, question_bank[0].answer)