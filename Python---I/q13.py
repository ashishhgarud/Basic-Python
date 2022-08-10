# accepts a sentence and calculate the number of letters and digits.
phrase = input(" ")
phrase_dic = {"DIGITS": 0, "LETTERS": 0}

for i in phrase:
    if i.isdigit():
        phrase_dic["DIGITS"] += 1
    elif i.isalpha():
        phrase_dic["LETTERS"] += 1
    else:
        pass
print("DIGITS", phrase_dic["DIGITS"])
print("LETTERS", phrase_dic["LETTERS"])

