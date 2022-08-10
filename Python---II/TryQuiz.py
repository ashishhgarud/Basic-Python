# Defining Score variables
x = 0
score = x

# Question One
print("What is 1 + 1")
answer_1 = input("a)1\nb)2\nc)3\nd)4\n:")
if answer_1.lower() == "b" or answer_1.lower() == "2":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, 1 + 1 is 2")

# Question Two
print("Who is the 45th president of the United States?")
answer_2 = input("a)Barack Obama\nb)Hillary Clinton\nc)Donald      Trump\nd)Tom Brady\n:")
if answer_2.lower() == "c" or answer_2.lower() == "donald trump":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, The 45th president is Donald Trump")

# Question Three
    print("True or False... The Toronto Maple Leafs have won 13 Stanley   Cups?")
    answer_3 = input(":")
    if answer_3.lower() == "true" or answer_3.lower() == "t":
        print("Correct")
        x = x + 1
    else:
        print("Incorrect")

# Question Four
    print("What was the last year the Toronto Maple Leafs won the Stanley   Cup?")
    answer_4 = input("a)1967\nb)1955\nc)1987\nd)1994\n:")
    if answer_4.lower() == "a" or answer_4 == "1967":
        print("Correct")
        x = x + 1
    else:
        print("Incorrect, The last time the Toronto Maple Leafs won the Stanley Cup was 1967")

# Question Five
    print("True or False... The current Prime Minister of Canada is Pierre Elliot Tredeau?")
    answer_5 = input(":")
    if answer_5.lower() == "false" or answer_5.lower() == "f":
        print("Correct")
        x = x + 1
    else:
        print("Incorrect, The current Prime Minster of Canada is Justin Tredeau")

# Total Score
    score = float(x / 5) * 100
    print(x, "out of 5, that is", score, "%")