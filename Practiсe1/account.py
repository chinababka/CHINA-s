def credit_account(money, period, rate):
    # Формула расчета ежемесячных выплат S = x * p**n * (p-1) / p**n - 1
    money_per_month = money * (rate / 100 + 1) ** period \
                      * (rate / 100) / ((rate / 100 + 1) ** period - 1)
    # Итоговая сумма выплаты по кредиту
    result = round(money_per_month * period)
    return result

def main():
    rate = 10
    money = 100000
    period = 12

    print("Параметры счета:")
    print("Сумма кредита:", money, "рублей")
    print("Ставка:", rate, "%")
    print("Срок выплаты:", period, "месяцев")
    print("Итоговая сумма выплаты по кредиту:", credit_account(money, period, rate), "рублей")


if __name__ == "__main__":
    main()
