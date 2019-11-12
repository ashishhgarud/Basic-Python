# Multiple Choices Questions Quiz
# Logic Implementation by "ONE BY ONE STRAIGHT FORWARD"

score = 0

answer1 = input("What is square root of 81? \n(a) 7 \n(b) 8 \n(c) 9 \nAnswer: ").lower()
if answer1 == "c" or answer1 == "9":
    print("Correct!")
    score += 1
    print("Score: ", score, "\n")
else:
    print("Incorrect! The answer is (c) 9")
    print("Score: ", score, "\n")


answer2 = input("What is capital of India? \n(a) Delhi \n(b) Mumbai \n(c) Madras \nAnswer: ")
if answer2 == "a" or answer2 == "Delhi".lower():
    print("Correct!")
    score += 1
    print("Score: ", score, "\n")
else:
    print("Incorrect! The answer is (a) Delhi")
    print("Score: ", score, "\n")

# Final result and message
if score == 0:
    print("Your score is:", score, "You suck!")
elif score == 1:
    print("Your score is:", score, "Not bad")
else:
    print("Your score is:", score, "Excellent!")
