# Задача 1. Улучшенная лингвистика 2
#
# Усовершенствуйте старую программу:
#
# У нас есть список из трёх слов, которые вводит пользователь. Затем вводится сам текст произведения,
# который вводится уже в одну строку. Напишите программу, которая посчитает, сколько раз слова пользователя встречаются в тексте.

list_word = ['Привет', 'утро', 'доброе']
text = input('Введите текст: ')

text_str = text.split()

for i in range(len(list_word)):
    print('\nСлово "{0}" встречается в тексте {1} раз'. format(
        list_word[i],
        text.count(list_word[i])
    ))

