import random

# параметры автомата
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

# размерность автомата
ROWS = 3
COLS = 3

# все возможные значения в слотах
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 2
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


# проверка победы
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)
    return winnings, winnings_lines


# Генерация колонок слотовой машины, но пока в строках
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symb, symb_count in symbols.items():
        for _ in range(symb_count):
            all_symbols.append(symb)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols.copy()
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


# Транспонирование строк в колонки и печать на экран
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row])


# Определение суммы депозита
def deposit():
    while True:
        amount = input("Какую сумму вы бы хотели внести? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("\nДепозит должен быть больше нуля.")
        else:
            print("\nПожалуйста, введите сумму депозита.")
    return amount


# Определение количество линий в ставке от 1 до 3
# (выбираются автоматически начиная с верхней)
def get_number_of_lines():
    while True:
        number_of_lines = input(
            f"Выбери количество линий от 1 до {MAX_LINES}: ")
        if number_of_lines.isdigit():
            number_of_lines = int(number_of_lines)
            if 1 <= number_of_lines <= MAX_LINES:
                break
            else:
                print(f"\nКоличество линий должно быть от 1 до {MAX_LINES}.")
        else:
            print(f"\nПожалуйста, введите число от 1 до {MAX_LINES}.")
    return number_of_lines


# Опредение суммы ставки на линии
def get_bet():
    while True:
        bet = input("Какую ставку вы хотели бы сделать? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"\nСтавка должна быть от ${MIN_BET} до ${MAX_BET}.")
        else:
            print("\nПожалуйста, введите сумму ставки.")
    return bet


# одно вращение
def spin(balance):
    print()
    lines = get_number_of_lines()
    print()
    # проверка, больше ли итоговая
    # ставка(линии*ставки на линии)баланса(депозита)
    while True:
        bet = get_bet()
        print()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Итоговая сумма ставки "
                  f"превышает баланс, твой текущий баланс = ${balance}.")
        else:
            break
    print()
    print(f"Ты делаешь ставку ${bet} на {lines} "
          f"линии(-ю). Итоговая сумма ставки равна ${total_bet}.")
    print()
    # генерация слотов
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    # печать слотов
    print_slot_machine(slots)
    # проверка победы
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f'\nТвой выигрыш: ${winnings}.')
    if winnings != 0:
        print("Твои выигрышные линии:", *winning_lines)
    return winnings - total_bet


# запуск игры
def main():
    balance = deposit()
    while True:
        print(f"\nТекущий баланс: ${balance}")
        answer = input(
            "Нажмите ENTER, что бы запустить вращение, \"q\" для выхода.")
        if answer.lower() == "q" or answer.lower() == "й":
            break
        balance += spin(balance)
    print(f"Твой итоговый баланс ${balance}")


if __name__ == "__main__":
    main()
