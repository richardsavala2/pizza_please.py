from pizzapi import *
from pizzapi.console import ConsoleInput


def searchMenu(menu):
    print('You are now searching the menu...')
    item = input('Type an item to look for: ').strip().lower()

    if item != '' and len(item) > 1:
        item = item[0].upper() + item[1:]
        print(f'Results for: {item}')
        menu.search(Name=item)
        print()
    else:
        print('No Results...')


def addToOrder(order):
    print("Please type the codes of the items you'd like to order...")
    print('Press ENTER to stop ordering.')
    while True:
        item = input('Code: ').upper()
        try:
            order.add_item(item)
        except:
            if item == "":
                break
            print('Invalid Code...')


customer = ConsoleInput.get_new_customer()
address = Address('301 Cleveland Boulevard', 'Caldwell', 'ID', '83605')
store = address.closest_store()
print(address.closest_store())
print('\nMENU\n')

menu = store.get_menu()
order = Order(store, customer, address)

searchMenu(menu)
addToOrder(order)

while True:
    searchMenu(menu)
    addToOrder(order)
    answer = input('Would you like to add more items? (y/n) ')
    if answer.lower() not in ['yes', 'y']:
        break

total = 0
print('\nYour order is as follows: ')
for item in order.data['Products']:
    price = item['Price']
    print(item['Name'] + ' $' + price)
    total += float(price)

print('\nYour order total is: $' + str(total) + '+ TAX\n')

card = ConsoleInput.get_credit_card()

payment = input('\nWill you be paying CASH or CREDIT CARD? (CASH, CARD) ')
if payment.lower() in ['cash', 'credit card']:
    card = ConsoleInput.get_credit_card()
else:
    card = False

ans = input('Would you like to place this order? (y/n) ')
if ans.lower() in ['y', 'yes']:
    order.place(card)
    print('Order Placed!')
else:
    print('Goodbye!')
