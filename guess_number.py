from random import randint


random_number = randint(1, 100)
while True:
    number = int(input())
    if number < random_number:
        print('Ваше число меньше того, что загадано')
    elif number > random_number:
        print('Ваше число больше того, что загадано')
    else:
        break

print('Отличная интуиция! Вы угадали число :)')    
    
        