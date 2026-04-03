def calculate_bmi(weight, height):
    # реализовать расчет ИМТ
    pass
def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Недостаточный вес"
    elif 18.5 <= bmi < 25:
        return "Нормальный вес"
    elif 25 <= bmi < 30:
        return "Избыточный вес"
    else:
        return "Ожирение"

def ideal_weight(height, gender):
    # реализовать расчет идеального веса
    pass
def save_result(name, bmi, category):
    # реализовать сохранение результата
    pass


def main():
    print("Добро пожаловать в BMI Calculator!")
    try:
        weight = float(input("Введите ваш вес (кг): "))
        height = float(input("Введите ваш рост (м): "))

        bmi = calculate_bmi(weight, height)
        category = interpret_bmi(bmi)

        print(f"Ваш ИМТ: {bmi}")
        print(f"Категория: {category}")
    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()