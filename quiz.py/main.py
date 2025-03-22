from data import  question_data,logo_quiz_game
import random
from question_model import Question
import quiz_brain

co=0
n=1
print(logo_quiz_game)

print("Welcome to my quiz game")


while True:
    random_question=random.choice(question_data)
    question_data.remove(random_question)
    if len(question_data)==0:
        break
    q=random_question["question"]
    a=random_question["correct_answer"]
    new_question=Question(q,a)
    reponse=input(f"Q.{n}: {new_question.question}. (True/False)?: ")
    if reponse==new_question.answer:
        co+=1
        print("you got it right!")
        print(f"The correct answer was:{new_question.answer}")
        print(f"your current score is :{co}/{n}")
    else:
        print("Thats Wrong.")
        print(f"The correct answer was: {new_question.answer}")
        print(f"Your currenct score is:{co}/{n}")
    n+=1


quiz_brain.remarque(co)