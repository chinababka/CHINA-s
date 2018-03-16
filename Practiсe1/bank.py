from account import credit_account
from exchange import money_exchange

def main():
    r = int(input("Введите процент кредита: "))
    p = int(input("Введите продолжительность кредита: "))
    m = int(input("Введите сумму кредита: "))

    result_calculator = credit_account(m, p, r)
    value = "рублей"
    result_exchange = money_exchange(result_calculator, value)

    print("\nПараметры счета: ")
    print("Сумма кредита: ", m, value)
    print("Продолжительность кредита: ", p, "месяцев")
    print("Процентная ставка: ", r, "%")
    print("Итоговая сумма выплаты по кредиту: ", result_calculator, value)
    print("Сумма с учетом перевода: ", result_exchange)


if __name__ == "__main__":
    main()