import decimal


def calc_pi(num: int) -> str:
    decimal.getcontext().prec = num + 100
    pi = decimal.Decimal(0)

    for k in range(num):
        pi += decimal.Decimal(1) / decimal.Decimal(16 ** k) * (decimal.Decimal(4) / (decimal.Decimal(8) * decimal.Decimal(k) + decimal.Decimal(1)) - decimal.Decimal(2) / (decimal.Decimal(8) * decimal.Decimal(k) + decimal.Decimal(4)) - decimal.Decimal(1) / (decimal.Decimal(8) * decimal.Decimal(k) + decimal.Decimal(5)) - decimal.Decimal(1) / (decimal.Decimal(8) * decimal.Decimal(k) + decimal.Decimal(6)))
    
    return str(pi)[:num + 2]


print(calc_pi(50_000))
