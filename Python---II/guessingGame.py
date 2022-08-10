secret_word = 'beinghuman'

guess_count = 0
guess_limit = 2

out_of_guesses = False

guess_word = ''
while guess_word != secret_word and not (out_of_guesses):
    if guess_count <= 2:
       guess_word = input('Enter guess word: ').lower().strip()
       guess_count +=1
    else:
        out_of_guesses = True
if out_of_guesses:
    print('you crossed the guessing limit, you are out of guesses. you lose!')
else:
    print('you won!')