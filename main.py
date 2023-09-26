import math
import time
while True:
    print("Выбирите число от 1 до 12")
    print("1. Сложение              |   6.Квадратный корень ")
    print("2. Вычитание             |   7. Факториал числа")
    print("3. Умножение             |   8. Синус")
    print("4. Деление               |   9. Косинус")
    print("5. Возвести в степень    |   10. Тангенс")
    print("             11. Завершение программы ")

    choice = (input("Введите действие: "))

    if  choice.isdigit():
        choice = int(choice)
        if choice >= 1 and choice <= 11:
            if choice in [1, 2, 3, 4, 5]:
                try:
                    n1 = float(input("Введи первое число: "))
                    n2 = float(input("Введи второе число: "))
                except ValueError:
                    print("Не буквы, цифры!")
                    time.sleep(1.5)
                    continue
                if choice == 1:
                    print(f"{n1} + {n2} = {n1 + n2}")
                if choice == 2:
                    print(f"{n1} - {n2} = {n1 - n2}")
                if choice == 3:
                    print(f"{n1} * {n2} = {n1 * n2}")
                if choice == 4:
                    if n2 == 0:
                        print("На 0 делить нельзя :( ")
                    else:
                        print(f"{n1} / {n2} = {n1 / n2}")

                if choice == 5:
                    print(f"{n1} ** {n2} = {n1 ** n2}")

            if choice in [6, 7, 8, 9, 10]:
                try:
                    n1 = float(input("Введи первое число: "))
                except ValueError:
                    print("Не буквы, цифры!")
                    time.sleep(1.5)
                    continue
                if choice == 6:
                    if n1 < 0:
                        print("Ещё не умею находить корень из отрицательного числа")
                    else:
                        print(f"квадратный корень из {n1} равен {math.sqrt(n1)}")
                if choice == 7:
                    if n1 % 1 != 0:
                        print("нельзя найти факториал из дробного числа, может вы хотите  отбросить дробную часть? ")
                        print("1. Да   |  2. Нет")
                        answ = input("Введите ответ: ")
                        if answ == '1':
                            n1 = math.trunc(n1)
                            print(f"В таком случае, факториалом {math.trunc(n1)} является {math.factorial(n1)}")
                        elif answ == '2':
                            print("Хорошо, тогда попробуем в другой раз )")
                if choice == 8:
                    print(f"синусом {n1} является {math.sin(n1)}")
                if choice == 9:
                    print(f"косинусом числа {n1} является {math.cos(n1)}")
                if choice == 10:
                    print(f"тангенсом числа {n1} является {math.tan(n1)}")
            if choice == 11:
                print("Ну пока :( ")
                break

        else:
            print("Боба? Введи то что просят ^_^ ")
    else:
        print("Не буквы, цифры )")

    time.sleep(1.5)