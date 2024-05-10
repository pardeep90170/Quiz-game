class QuizBrain:
    def __init__(self, qlist):
        self.question_Number = 0
        self.question_list = qlist
        self.score=0
    
    def matched(self,ch):
        current_answer = self.question_list[self.question_Number]
        answer = current_answer.answer
        # print(answer)
        answer2 = answer == ch
        # print(answer2)
        return answer2
        
    
    def next_question(self):
        
        for _ in self.question_list:
             
            current_question = self.question_list[self.question_Number]
            ch=input(f"Q.no {self.question_Number + 1}: {current_question.text} (True/False)")
            answer=self.matched(ch)
            if answer :
                print("Correct!")
                self.question_Number += 1
                self.score +=1  
                   
            else:
                print("Incorrect")
                self.question_Number += 1
        print(f"final score:{self.score}")

        