def stran():
    count_all = {
        'Россия': 'Москва',
        'Греция': 'Афины',
        'Франция': 'Париж',
        'Сербия': 'Белград',
        'Италия': 'Рим'
    }
    for coun, stal in count_all.items():
        print(f"{coun}: {stal}")
    coun = "Россия"
    if coun in count_all:
        print(f" Столица страны {coun}: {count_all[coun]}")
    else:
        print(f" Страна {coun} не найдена в списке.")
    sorts = dict(sorted(count_all.items()))
    print( "Отсортированный список стран и их столиц:")
    for coun, stal in sorts.items():
        print(f"{coun}: {stal}")
def igra1():
    slovar = {
        1: ['а', 'в', 'е', 'и', 'н', 'о', 'р', 'с', 'т'],
        2: ['д', 'к', 'л', 'м', 'п', 'у'],
        3: ['б', 'г', 'ё', 'ь', 'я'],
        4: ['й', 'ы'],
        5: ['ж', 'з', 'х', 'ц', 'ч'],
        8: ['ш', 'э', 'ю'],
        10: ['ф', 'щ', 'ъ']
    }
    original_word = input("Введите слово: ")
    word = original_word.lower()
    for letter in word:
        if not ('а' <= letter <= 'я'):
            print("Ошибка: слово должно состоять только из русских букв.")
            break
    else:
        ball_all = sum(1 for letter in word if any(letter in group for group in slovar.values()))
        print(f"Стоимость слова '{original_word}' равна {ball_all} очков.")
def stydent():
    students = {
        "Саша": {"русский", "английский", "китайский"},
        "Ангелина": {"английский", "французский"},
        "Даша": {"китайский", "немецкий", "русский"},
        "Оля": {"английский", "немецкий"},
        "Женя": {"русский", "английский", "французский", "китайский"}
    }
    all_lan = set()
    for lan in students.values():
        all_lan.update(lan)
    print("Отсортированный список языков: ")
    for language in sorted(all_lan):
        print(language)
    s = input("Напишите выбранный язык: ")
    if s in all_lan:
        print("\n Студенты, которые знают данный язык: ")
        for student, language in students.items():
            if s in language:
                print(student,language)
    else:
        print("Проверьте правильность списанного слова ")
while True:
    print('1. Страны')
    print('2. Эрудит')
    print('3. Студенты')
    print('4. Выход')
    a = int(input('Выберите действие: '))
    if a == 1:
        stran()
    elif a == 2:
        igra1()
    elif a == 3:
        stydent()
    elif a == 4:
        break
    else:
        print('Неверное действие')