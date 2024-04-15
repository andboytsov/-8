def calculate_investment_amount(initial_amount, interest_rate, years):
    final_amount = initial_amount * (1 + interest_rate) ** years
    return final_amount

initial_amount = float(input("Введите начальную сумму: "))
interest_rate = float(input("Введите процентную ставку (в виде десятичной дроби): "))
years = int(input("Введите количество лет: "))

final_amount = calculate_investment_amount(initial_amount, interest_rate, years)
print(f"Через {years} лет ваша инвестиция вырастет до: {final_amount:.2f}")


