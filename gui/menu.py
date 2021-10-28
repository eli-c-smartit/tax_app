def draw_menu():
    
    print("******* main menu ******")
    print("1 - calc vat")
    print("2 - calc salary tax")

    user_option = 0
    
    while True:
        user_option = input("type otion")
        if user_option.isdecimal():
            break;

    return int(user_option)
#############################


def draw_calc_vat_menu():
    print("******** calc vat ******")
    amount = 0

    while True:
        amount = input("type amount :")
        if amount.isdecimal():
            return float(amount);

    return amount
#############################

def draw_cal_tax_menu():
    print("******** calc tax ******")
    amount = 0

    while True:
        amount = input("type amount :")
        if amount.isdecimal():
            return float(amount)

    return amount
#############################



    
