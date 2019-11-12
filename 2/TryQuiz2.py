import string
from collections import namedtuple
Question = namedtuple("Question", "question answer choices correct")


questions = [Question("What is 1 + 1", "1 + 1 is 2",
                      ["1", "2", "3", "4"], {"b", "2"}), ...]


def quiz(questions):
    score = 0
    for question in questions:
        print(question.question)
        for line in zip(string.ascii_lowercase, question.choices):
            print(") ".join(line))
        user_answer = input().lower()
        if user_answer in question.correct:
            print("Correct")
            score += 1
        else:
            print("Incorrect", question.answer)
    print("{} out of {} that is {} %".format(score, len(questions), score / len(questions) * 100))

if __name__ == "__main__":
    # Use all questions but the first
    quiz(questions[1:])