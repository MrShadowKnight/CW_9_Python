import json

# with open("test.json", "r") as file:
#     accounts = json.load(file)

# def money_withdraw(id, amount):
#     for i in accounts['accounts']:
#         for a in range(len(accounts[i])):
#             for b in accounts[i]:
#                 identefication = a + 1

#             if id == identefication and amount <= b['balance']:
#                 print
    
# def new_account(name):
    
#     accounts['accounts'].dump

# while True:
#     account_id = int(input("Введіть Id вашого акаунту: "))
#     for item in accounts['accounts']:
#         if account_id == item['id']:
#             break
#         else:
#             print("Такого акаунту не існує!")


# while True:
#     print("Меню")
#     print("1 --- Створити новий рахунок")
#     print("2 --- Зняти кошти з рахунку")
#     print("3 --- Поповнити рахунок")
#     print("4 --- Перевести кошти з одного рахунку на інший")
#     print("5 --- Перевірити баланс рахунку")
#     print("6 --- Вийти з програми")

#     choice = int(input("Виберіть пункт з меню: "))

#     if choice == 1:
#         print
#     elif choice == 5:
#         for item in accounts['accounts']:
#             print("Ваш баланс: ", item["balance"])
#     elif choice == 6:
#         print("Ви вийшли із системи!")
#         break
#     else:
#         print("Такої функції немає! Повторіть спробу!")

# try:
#     num = 1/0
# except Exception as err:
#     print(err)
# finally:
#     print("Some text")

# def sumNumbers(a, b):
#     return a + b

# def runProgram():
#     sumNumbers(1, 2)
#     temperature = int(input("Введіть температуру:"))
#     if temperature > 0:
#         print("teplo")
#     else:
#         print("Cholodno")

# active = True
# while active:
#     try:
#         runProgram()
#     except Exception as err:
#         print(err)
#     finally:
#         chois = input("Чи бажаєте продовжити користування(Y | N): ")
#         if chois.lower() == "n":
#             active = False

# def initials(first_name, second_name, father_name):
#     try:
#         print(f"{first_name.capitalize()} {second_name[0].capitalize()}. {father_name[0].capitalize()}.")
#     except Exception as err:
#         print("сталася помилка в створені ініціалів!")

# def runProgram():
#     first_name = input("Введіть прізвище: ")
#     second_name = input("Введіть імя: ")
#     father_name = input("Введіть побатькова: ")
#     initials(first_name, second_name, father_name)
#     temperature = int(input("Введіть температуру:"))
#     if temperature > 0:
#         print("teplo")
#     else:
#         print("Cholodno")
# active = True
    # name = input("Введіть ім'я тварини: ")
    # breed = input("Введіть породу тварини: ")
    # recomed_food = input("Введіть рекомендовану їжу для тварини: ")
# while active:
#     try:
#         runProgram()
#     except Exception as err:
#         print(err)
#     finally:
#         chois = input("Чи бажаєте продовжити користування(Y | N): ")
#         if chois.lower() == "n":
#             active = False






try:
    with open("zoo.json", "r", encoding="utf-8") as file:
        zoo = json.load(file)

except Exception as err:
    print("Для початку програми добавте першу тварину!")
    name_animal = input("Введіть ім'я тварини: ")
    breed_animal = input("Введіть породу тварини: ")
    recomed_food_animal = input("Введіть рекомендовану їжу для тварини: ")
    type_animal = input("введіть тип тварини: ")
    frame = {
        "name": name_animal,
        "breed": breed_animal,
        "recomend food": recomed_food_animal,
        "type": type_animal
    }
    zoo["animals"].append(frame)
    with open("zoo.json", "r", encoding="utf-8") as file:
        json.dump(zoo, file)

def addAnimals(name, breed, recomed_food, type):
    with open("zoo.json", "r", encoding="utf-8") as file:
        zoo = json.load(file)
    frame = {
        "name": name,
        "breed": breed,
        "recomend food": recomed_food,
        "type": type
    }
    zoo["animals"].append(frame)
    with open("zoo.json", "r", encoding="utf-8") as file:
        json.dump(zoo, file)
    
def scretchAnimal(breed):
    with open("zoo.json", "r", encoding="utf-8") as file:
        zoo = json.load(file)
    for item in zoo['animals']:
        if item["breed"] == breed:
            print(item["name"])
            print(item["food"])
            break
        elif breed.lower() == "q":
            break
        else:
            print("Такої породи тварин немає!")
while True:
    print("Меню:\n 1 --- Додати тварину.\n 2 --- Знайти тварину за породою.\n q --- Вийти зі системи.")
    ch = input("Виберіть дію: ")
    if ch == "1":
        name_animal = input("Введіть ім'я тварини: ")
        breed_animal = input("Введіть породу тварини: ")
        recomed_food_animal = input("Введіть рекомендовану їжу для тварини: ")
        type_animal = input("введіть тип тварини: ")
        addAnimals(name_animal, breed_animal, recomed_food_animal, type_animal)
    elif ch == "2":
        breed = input("Введіть породу тварини(або q для виходу): ")
        scretchAnimal(breed)
    elif ch.lower() == "q":
        break
    else:
        print("Такої дії немає: ")