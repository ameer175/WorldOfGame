from currency_converter import CurrencyConverter
import random


def get_money_interval(d):
    random_number = random.randint(1, 100)
    c = CurrencyConverter()
    Usd_To_Ils = c.convert(1, 'USD', 'ILS')
    t = random_number * Usd_To_Ils
    resMin = (t - (5 - d))
    resMax = (t + (5 - d))
    return resMax,resMin

def get_guess_from_user(Difficulty):
    try:
        guessedvalue = int(input("hat he thinks is the value of the generated number from USD to ILS?: "))
        Max, Min = get_money_interval(Difficulty)
        if (guessedvalue >= Min and guessedvalue <= Max):
            return True
        else:
            return False
    except Exception as e:
        print(type(e),"is not integer number get me number again: ")
        get_guess_from_user(Difficulty)

def play(Difficulty):
    return get_guess_from_user(Difficulty)
