# Создайте такую программу:
# Программа хранит какую-либо цифру в переменной.
# Программа просит пользователя угадать цифру. Пользователь вводит цифру.
# Программа сравнивает цифру с той, что хранится в переменной.
# Если цифры не равны, программа пишет “попробуйте снова” и снова просит пользователя
# угадать цифру.
# Если пользователь угадывает цифру, программа пишет “Поздравляю! Вы угадали!” и
# завершается.
# Т.е. программа не завершается пока пользователь не угадает цифру.
#
# Подсказка: задание выполняется с помощью цикла while
guess_number = 3
while True:
    user_number = int(input('Guess the number! '))
    if user_number == guess_number:
        print('Congratulations! You guessed!')
        break
    else:
        print('Try again!')