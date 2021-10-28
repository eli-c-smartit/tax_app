def calc_vat(amount):
    return amount * 1.18

def calc_tax(salary):
    if salary < 5000:
        return 0
    elif salary < 7000:
        return salary * 0.1
    elif salary < 10000:
        return salary * 0.2
    else:
        return salary * 0.5