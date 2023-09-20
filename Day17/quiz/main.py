from data import question_data
from question_model import Question
from quiz_brain import BrainQuiz

bank_question = []

for question in question_data:
    q_text = question["text"]
    q_answer = question["answer"]
    new = Question(q_text, q_answer)
    bank_question.append(new)

brain = BrainQuiz(bank_question)
while brain.still_questions():
    brain.new_question()