#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
#БЛОК 1. Ввод и проверка данных пользователя
## 1.1. Пол
line_sex = input("Твой пол (м/ж или мужской/женский): ")
line_sex = line_sex.strip().lower()
while line_sex not in ["м", "ж", "мужской", "женский"]:
    print("Ошибка: введите 'мужской' или 'женский' (можно кратко: м/ж).")
    line_sex = input("Твой пол (м/ж или мужской/женский): ")
    line_sex = line_sex.strip().lower()
### Приводим к одному виду:
if line_sex in ["мужской", "м"]:
    line_sex = "мужской"
else:
    line_sex = "женский"

## 1.2. Возраст
line_age = input("Твой возраст: ")
line_age = line_age.strip()
while line_age == "" or line_age.isdigit() == False:
    print("Ошибка: введите возраст цифрами")
    line_age = input("Твой возраст: ")
    line_age = line_age.strip()
line_age = int(line_age)
    
## 1.3. Вес
line_weight = input("Твой вес: ")
line_weight = line_weight.strip()
while line_weight == "" or line_weight.isdigit() == False:
    print("Ошибка: введите вес цифрами")
    line_weight = input("Твой вес: ")
    line_weight = line_weight.strip()
line_weight = int(line_weight)
    
## 1.4. Цель
line_goal = input("Выберите цель (похудение / массонабор): ")
line_goal = line_goal.strip().lower()
while line_goal not in ["похудение", "массонабор"]:
    print("Ошибка: выберите цель строго между заданными значениями")
    line_goal = input("Выберите цель: ")
    line_goal = line_goal.strip().lower()
#___________________________________________________ 

#КАТАЛОГ УПРАЖНЕНИЙ
exercise_catalog = {
    "грудь": [
        "Жим штанги лёжа",
        "Жим гантелей лёжа",
        "Жим гантелей на наклонной скамье",
        "Отжимания на брусьях (грудь)",
        "Разводка гантелей лёжа",
        "Сведение рук в кроссовере",
        "Pec Deck (бабочка)",
        "Отжимания от пола (широкая постановка)",
        "Пуловер с гантелью"
],
    "спина": [
        "Подтягивания на турнике",
        "Тяга верхнего блока к груди",
        "Тяга штанги в наклоне",
        "Тяга горизонтального блока",
        "Тяга гантели одной рукой",
        "Тяга Т-грифа",
        "Пулдаун прямыми руками",
        "Гиперэкстензия",
        "Face Pull"
],
    "плечи": [
        "Жим штанги стоя",
        "Жим гантелей сидя",
        "Разведения гантелей в стороны",
        "Разведения гантелей в наклоне",
        "Махи в кроссовере",
        "Тяга штанги к подбородку",
        "Face Pull с канатом",
        "Жим Арнольда",
        "Подъём блина перед собой"
],
    "ноги (квадрицепсы)": [
        "Присед со штангой",
        "Гакк-присед спиной к машине",
        "Жим ногами",
        "Болгарские выпады",
        "Выпады с гантелями",
        "Разгибания ног в тренажёре",
        "Goblet Squat",
        "Зашагивания на тумбу",
        "Присед в Смите (узкая постановка ног)"
],
     "ноги (задняя цепь)": [
        "Румынская тяга",
        "Становая тяга",
        "Гиперэкстензия с весом",
        "Сгибания ног лёжа",
        "Сгибания ног сидя",
        "Ягодичный мост",
        "Good Morning",
        "Тяга на прямых ногах с гантелями",
        "Glute Kickback"
],
     "бицепс + трицепс": [
        "Подъём штанги на бицепс",
        "Сгибания гантелей стоя",
        "Молотки",
        "Сгибания на скамье Скотта",
        "Концентрированные сгибания",
        "Жим узким хватом",
        "Разгибания рук на блоке",
        "Французский жим лёжа",
        "Разгибание гантели из-за головы"
],
     "кардио": [
         "Беговая дорожка",
         "Эллиптический тренажёр",
         "Велотренажёр",
         "Гребной тренажёр",
         "Ходьба в горку",
         "Скакалка",
         "Лёгкая прогулка"
]
}
#Карта сложности
level_map = {
            "1" : ("лёгкий", 3),
            "2" : ("средний", 4),
            "3" : ("тяжёлый", 5)
        }

def show_workout(muscle_group, level_name, exercises_count, exercise_catalog):
    print("\n==============================")
    print("Группа мышц:", muscle_group)
    print("Уровень сложности:", level_name)
    print("==============================")

#КАРДИО
    if muscle_group == "кардио":
        print("\nРазминка:")
        print("Кардио 5 минут (лёгкий темп)")
        print("\nОсновная часть: ")
        if level_name == "лёгкий":
            duration = 15
        elif level_name == "средний":
            duration = 20
        else:
            duration = 25
        cardio_type = random.choice(exercise_catalog["кардио"])
        print(f"{cardio_type} — {duration} минут в ровном темпе")
        print("\nЗаминка:")
        print("Кардио 10 минут (очень лёгкий темп)")
        print("==============================\n")
        input("Нажмите Enter, чтобы вернуться в меню...")
        return

#СИЛОВАЯ
    if muscle_group not in exercise_catalog:
        print("Ошибка: группа мышц не найдена в каталоге")
        return
    exercises = exercise_catalog[muscle_group]
    if len(exercises) < exercises_count:
        print("Ошибка: недостаточно упражнений в каталоге")
        return
    selected = random.sample(exercises, exercises_count)
    print("\nРазминка:")
    print("Кардио 5 минут")
    print("\nУпражнения:")
    for i, ex in enumerate(selected, 1):
        print(f"{i}. {ex}")
        print("   4 подхода: 12 / 10 / 8 / 6")

    print("\nЗаминка:")
    print("Кардио 10 минут")
    print("==============================\n")
    input("Нажмите Enter, чтобы вернуться в меню...")


def choose_level():
    print("Выберите уровень нагрузки:")
    print("1 — лёгкий")
    print("2 — средний")
    print("3 — тяжёлый")

    level = input("Выберите уровень нагрузки: ").strip()
    while level not in level_map:
        print("Ошибка: выберите уровень строго из списка")
        level = input("Выберите уровень нагрузки: ").strip()

    return level_map[level]

#БЛОК 2. Главное меню
while True:
    print("Меню пользователя:")
    print("1 — тренировка по дням недели")
    print("2 — тренировка по группе мышц")
    print("exit / q — выход")
    command = input("Ваш выбор: ")
    command = command.strip().lower()
    
## 2.1. Ветвление
    if command == "1":
# 2.2 Выбор тренировки по дням недели
        day_week = input("Выберите день недели (пн/вт/ср/чт/пт/сб/вс): " )
        day_week = day_week.strip().lower()
        while day_week not in ["пн", "вт", "ср", "чт", "пт", "сб", "вс"]:
            print("Ошибка: выберите день строго из списка")
            day_week = input("Выберите день недели: ")
            day_week = day_week.strip().lower()
## 2.3 Определить ГРУППЫ МЫШЦ ПО ДНЯМ недели
        day_map = {
            "пн" : "грудь",
            "вт" : "спина",
            "ср" : "плечи",
            "чт" : "ноги (квадрицепсы)",
            "пт" : "ноги (задняя цепь)",
            "сб" : "бицепс + трицепс",
            "вс" : "кардио"
        }
        muscle_group = day_map[day_week]
        level_name, exercises_count = choose_level()

        ## 2.6 Определить УРОВЕНЬ СЛОЖНОСТИ по номеру (1)    
        show_workout(muscle_group, level_name, exercises_count, exercise_catalog)
        
    elif command == "2":
# 2.4 Выбор тренировки по группе мышц
        print("Выберите номер группы мышц: ")
        print("1 — грудь")
        print("2 — спина")
        print("3 - плечи")
        print("4 — ноги (квадрицепсы)")
        print("5 — ноги (задняя цепь)")
        print("6 - бицепс + трицепс")
        print("7 - кардио")
        day_muscle = input("Выберите номер группы мышц: ")
        day_muscle = day_muscle.strip()
        while day_muscle not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("Ошибка: выберите номер группы строго из списка")
            day_muscle = input("Выберите номер группы мышц: ")
            day_muscle = day_muscle.strip()
## 2.5 Определить НАЗВАНИЕ ГРУППЫ МЫШЦ по номеру
        muscle_group_map = {
            "1" : "грудь",
            "2" : "спина",
            "3" : "плечи",
            "4" : "ноги (квадрицепсы)",
            "5" : "ноги (задняя цепь)",
            "6" : "бицепс + трицепс",
            "7" : "кардио"
        }
        muscle_group = muscle_group_map[day_muscle]
## 2.6 Определить УРОВЕНЬ СЛОЖНОСТИ по номеру (2)    
        level_name, exercises_count = choose_level()
        show_workout(muscle_group, level_name, exercises_count, exercise_catalog)
    elif command == "q" or command == "exit":
        break
    else:
        print("Ошибка: неизвестная команда")
#___________________________________________________ 

