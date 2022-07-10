import random
a = random.randint(1,15)
print('\nLet us start the number gussing game.' )
print('You have four chances to guess the number.')
print('Hint : The number is between 1 and 15 both included \n')

for _ in range(4):
    b = int(input('Enter Your Guess : '))
    if b == a :
        print('You guessed the correct number.')
        print('You Won !')
        break
    elif b > a :
        print('You guessed the wrong number.')
        print('The number is lesser than' , b ,'\n')
    else :
        print('You guessed the wrong number.')
        print('The number is greater than' , b, '\n')

if b != a : 
    print('You lost !')
    print('Try Again')