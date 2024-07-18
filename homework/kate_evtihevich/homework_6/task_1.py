# Напишите программу, которая добавляет ‘ing’ к словам (к каждому слову)
# в тексте “Etiam tincidunt neque erat, quis molestie enim imperdiet vel.
# Integer urna nisl, facilisis vitae semper at, dignissim vitae libero”
# и после этого выводит получившийся текст на экран.
# Знаки препинания не должны оказаться внутри слова.
# Если после слова идет запятая или точка, этот знак препинания должен идти
# после того же слова, но уже преобразованного.
some_text = (
    'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
    'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
)
words = some_text.split()
fin_words = []
for word in words:
    if word.endswith(',') or word.endswith('.'):
        word = word[:len(word)-1] + 'ing' + word[len(word)-1:]
    else:
        word += 'ing'
    fin_words.append(word)

print(' '.join(fin_words))
