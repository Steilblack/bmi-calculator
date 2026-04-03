def calculate_bmi(weight, height):
    if weight <= 0 or height <= 0:
        raise ValueError("Вес и рост должны быть положительными числами")
    bmi = weight / (height ** 2)
    return round(bmi, 2)
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
        bmi = calculate_bmi(weight, height)
        category = interpret_bmi(bmi)
        print(f"Ваш ИМТ: {bmi}")
        print(f"Категория: {category}")
        gender = input("Введите ваш пол (male/female): ")
        ideal = ideal_weight(height, gender)
        print(f"Ваш идеальный вес: {ideal} кг")
    except ValueError as e:
        print(f"Ошибка: {e}")
if __name__ == "__main__":
    main()

