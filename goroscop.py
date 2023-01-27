# взял даты отсюда
# https://avon-c.ru/wp-content/uploads/2/7/9/2793e2eec60ffabc11aba54ae7a96713.jpeg
date = int(input('Введите дату рождения: '))
month = input('Введите название месяца рождения со прописной буквы: ')
if (date >= 22 and date <= 31 and month == 'декабрь') or (month == 'январь' and date >= 1 and date <= 19):
    print("Козерог")
elif (date >= 20 and date <= 31 and month == 'январь') or (month == 'февраль' and date >= 1 and date <= 19):
    print("Водолей")
elif (date >= 20 and date <= 31 and month == 'февраль') or(month == 'март' and date >= 1 and date <= 21):
    print("Рыбы")
if (date >= 22 and date <= 31 and month == 'март') or (month == 'апрель' and date >= 1 and date <= 21):
    print("Овен")
elif (date >= 22 and date <= 31 and month == 'апрель') or (month == 'май' and date >= 1 and date <= 21):
    print("Телец")
elif (date >= 22 and date <= 31 and month == 'май') or (month == 'июнь' and date >= 1 and date <= 21):
    print("Близнецы")
elif (date >= 22 and date <= 31 and month == 'июнь') or (month == 'июль' and date >= 1 and date <= 21):
    print("Рак")
elif (date >= 22 and date <= 31 and month == 'июль') or (month == 'август' and date >= 1 and date <= 21):
    print("Лев")
elif (date >= 22 and date <= 31 and month == 'август') or (month == 'сентябрь' and date >= 1 and date <= 21):
    print("Дева")
elif (date >= 22 and date <= 31 and month == 'сентябрь') or (month == 'октябрь' and date >= 1 and date <= 21):
    print("Весы")
elif (date >= 22 and date <= 31 and month == 'октябрь') or (month == 'ноябрь' and date >= 1 and date <= 20):
    print("Скорпион")
elif (date >= 21 and date <= 31 and month == 'ноябрь') or (month == 'декабрь' and date >= 1 and date <= 21):
    print("Стрелец")

# date = int(input('Введите дату рождения: '))
# month = int(input('Введите месяц рождения: '))

# if (date >= 22 and date <= 31 and month == 12) or (month == 1 and date >= 1 and date <= 19):
#     print("Козерог")
# elif (date >= 20 and date <= 31 and month == 1) or (month == 2 and date >= 1 and date <= 19):
#     print("Водолей")
# elif (date >= 20 and date <= 31 and month == 2) or(month == 3 and date >= 1 and date <= 21):
#     print("Рыбы")
# if (date >= 22 and date <= 31 and month == 3) or (month == 4 and date >= 1 and date <= 21):
#     print("Овен")
# elif (date >= 22 and date <= 31 and month == 4) or (month == 5 and date >= 1 and date <= 21):
#     print("Телец")
# elif (date >= 22 and date <= 31 and month == 5) or (month == 6 and date >= 1 and date <= 21):
#     print("Близнецы")
# elif (date >= 22 and date <= 31 and month == 6) or (month == 7 and date >= 1 and date <= 21):
#     print("Рак")
# elif (date >= 22 and date <= 31 and month == 7) or (month == 8 and date >= 1 and date <= 21):
#     print("Лев")
# elif (date >= 22 and date <= 31 and month == 8) or (month == 9 and date >= 1 and date <= 21):
#     print("Дева")
# elif (date >= 22 and date <= 31 and month == 9) or (month == 10 and date >= 1 and date <= 21):
#     print("Весы")
# elif (date >= 22 and date <= 31 and month == 10) or (month == 11 and date >= 1 and date <= 20):
#     print("Скорпион")
# elif (date >= 21 and date <= 31 and month == 11) or (month == 12 and date >= 1 and date <= 21):
#     print("Стрелец")