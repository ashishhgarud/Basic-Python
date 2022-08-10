# Multiple Choices Questions Quiz
# Logic Implementation using "CONTAINERS and ZIP"
# avoid having to 'repeat the whole logic' for every question.
# using ZIP
#x = [1, 2, 3]
#y = [4, 5, 6]
#zipped = zip(x, y)
#list(zipped)
   #[(1, 4), (2, 5), (3, 6)]


score = 0

questions = [
            "What is square root of 81?",
            "What is capital of India?",
            "What is capital Maharashtra?"
           ]

mupltple_choices = [
                    "(a) 7 \n(b) 8 \n(c) 9",
                    "(a) Delhi \n(b) Mumbai \n(c) Madras",
                    "(a) Nagpur \n(b) Mumbai \n(c) Pune "
                   ]

correct_choices = [
                  ("c", "9"),
                  ("a", "Delhi"),
                  ("b", "Mumbai")
                  ]

def quiz():
    for i, j, k in zip(questions, mupltple_choices, correct_choices):
        print("QUESTIONS")
        user_answer = input(j).lower()
        if user_answer in correct_choices:
            print("correct!")
            score += 1
        else:
            print("incorrect!", correct_choices)
    print(score, "out of", len(questions), "that is", float(score / len(questions)) * 100, "%")

    if __name__ == "__main__":
        quiz()