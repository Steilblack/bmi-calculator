def calculate_bmi(weight, height):
    # реализовать расчет ИМТ
    pass
def interpret_bmi(bmi):
    # реализовать интерпретацию ИМТ
    pass
def ideal_weight(height, gender):
    height_cm = height * 100
    if gender.lower() == 'male':
        ideal = height_cm - 100 - (height_cm - 150) / 4
    elif gender.lower() == 'female':
        ideal = height_cm - 100 - (height_cm - 150) / 2.5
    else:
        raise ValueError("Пол должен быть 'male' или 'female'")
    return round(ideal, 2)

def save_result(name, bmi, category):
    # реализовать сохранение результата
    pass

def main():
    print("Добро пожаловать в BMI Calculator!")
    try:
        weight = float(input("Введите ваш вес (кг): "))
        height = float(input("Введите ваш рост (м): "))
        gender = input("Введите ваш пол (male/female): ")

        bmi = calculate_bmi(weight, height)
        ideal = ideal_weight(height, gender)

        print(f"Ваш ИМТ: {bmi}")
        print(f"Ваш идеальный вес: {ideal} кг")
    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()