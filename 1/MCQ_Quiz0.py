# Multiple Choices Questions Quiz
# Logic Implementation using "OBJECT-ORIENTED"


from question_template import question
question_prompt_list = [
    'what color are bananas? \n (a) pink \n (b) red \n (c) yellow \\n',
    'what color are apples? \n (a) yellow \n (b) green \n (c) black \\n',
    'what color is sky? \n (a) blue \n (b) white \n (c) black'
]
questions_answer_list = [
    question(question_prompt_list[0], 'c'),
    question(question_prompt_list[1], 'b'),
    question(question_prompt_list[2], 'a'),
]

def run_test(questions_answer_list):
    score = 0
    for question in questions_answer_list:
        answer = input(question_prompt_list)
        if answer == question.answer:
            score += 1
     #print('you got ' + str(score) + '/' + str(len(questions_answer_list)))
