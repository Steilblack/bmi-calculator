def calculate_bmi(weight, height):
    if weight <= 0 or height <= 0:
        raise ValueError("Вес и рост должны быть положительными числами")
    bmi = weight / (height ** 2)
    return round(bmi, 2)
def interpret_bmi(bmi):
    # реализовать интерпретацию ИМТ
    pass
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
        print(f"Ваш ИМТ: {bmi}")
    except ValueError as e:
        print(f"Ошибка: {e}")
if __name__ == "__main__":
    main()