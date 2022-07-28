# 1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
#'абвгдейка - это передача' = >" - это передача"

str = "абвгдейка - это передача"
print(str)
list_of_words = str.split() # разбиваем строку на отдельные символы через запятую
result_list =[]
for word in list_of_words:
    if not ('абв' in word) == True:
        result_list.append(word)
print(result_list)
result = ' '.join(result_list) #получаем строковое значение
print(f'Исходный текст: {str} \n Полученный текст: {result}')






