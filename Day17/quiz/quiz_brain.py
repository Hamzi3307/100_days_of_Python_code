class BrainQuiz:
    def __init__(self, q_list):
        self.q_no = 0
        self.q_list = q_list
        self.score = 0
        
    def still_questions(self):
        return self.q_no < len(self.q_list)
    
    def check(self, answer, correct):
        if answer.lower() == correct.lower():
            print("You got it right")
            self.score += 1
        else:
            print("Wrong Answer \nCorrect Answer is ", correct.lower())
        print(f"Current Score is: ", self.score,"/",self.q_no)
    
    def new_question(self):
        current_question = self.q_list[self.q_no]
        self.q_no +=1
        user_input = input(f"Q.No.{self.q_no} : {current_question.text} (True/False)")
        self.check(user_input, current_question.answer)