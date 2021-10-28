from my_system import get_path
import my_customers

#print("app.py " + __name__)

#print(get_customer_list())
#print(my_customers.get_customer_list())
#print(get_path())


import gui.menu as mnu
import bl.tax as tax

selected_menu = mnu.draw_menu()
if selected_menu == 1:
    amount = mnu.draw_calc_vat_menu()
elif selected_menu == 2:
    amount = mnu.draw_cal_tax_menu()

print(f'calculating menu {selected_menu}, for amount: {amount}')
if selected_menu == 1:
    print(tax.calc_vat(amount))
elif selected_menu == 2:
    print(tax.calc_tax(amount))
else:
    print("error selection")

