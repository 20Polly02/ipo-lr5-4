str=input("Введите несколько слов :").lower()
list_of_word = str.split()
first_letter=[ letter[0] for letter in list_of_word]
str2=''.join(first_letter)
print(str2) 