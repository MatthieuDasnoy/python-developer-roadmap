import random, logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

guess = ''

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails: ')
    guess = input()
    logging.debug('guess = ' + guess)

coin = {0: 'tails', 1: 'heads'}     # Correction to BUG 1
toss = coin[random.randint(0, 1)]
logging.debug('toss  = ' + toss)

if toss == guess:                   # BUG 1: Was comparing int with string .
    print('You got it!')
    
else:
    print('Nope! Guess again!')
    guess = input()                 # BUG 2: Guess was typed with 3 s characters
    logging.debug('guess = ' + guess)
    logging.debug('toss  = ' + toss)
    
    if toss == guess:
        print('You got it!')

    else:
        print('Nope. You are really bad at this game.')
