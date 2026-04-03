def calculate_bmi(weight, height):
    # реализовать расчет ИМТ
    pass
def interpret_bmi(bmi):
    # реализовать интерпретацию ИМТ
    pass
def ideal_weight(height, gender):
    # реализовать расчет идеального веса
    pass
def save_result(name, bmi, category):
    with open("results.txt", "a", encoding="utf-8") as file:
        file.write(f"Имя: {name}, ИМТ: {bmi:.2f}, Категория: {category}\n")
    print("Результат сохранен в файл results.txt")

def main():
    print("Добро пожаловать в BMI Calculator!")
    try:
        name = input("Введите ваше имя: ")
        weight = float(input("Введите ваш вес (кг): "))
        height = float(input("Введите ваш рост (м): "))

        bmi = calculate_bmi(weight, height)
        category = interpret_bmi(bmi)

        print(f"Ваш ИМТ: {bmi}")
        print(f"Категория: {category}")

        save_result(name, bmi, category)
    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()