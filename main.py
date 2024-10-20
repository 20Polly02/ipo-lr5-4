str=input("Введите несколько слов :").lower()#ввод слов с клавиатуры
list_of_word = str.split()#создаем список из слов введенной строки
first_letter=[ letter[0] for letter in list_of_word]#создаем список из первых букв каждого введенного слова
str2=''.join(first_letter)#с помощью join() склеиваем первые буквы в одно слово
print(str2)#вывод слова на консоль
