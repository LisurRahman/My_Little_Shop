# My Little Shop
print('   ASSALAMUALIKUM,Dear customer!\n  Welcome to My Little Shop.')
print("How can I help you?")
Foods = {'Pizza': 30,
        'Biscuits': 15,
        'Bread': 20,
        'Boiled egg': 15,
        'Chips': 10,
        'Apple': 30,
        'Banana': 30,
        'Popcon': 20,
        'Tea': 5,
        'Barger': 40,
        'Sweet': 15,
        'Noodles': 30,
        'Laddu': 5,
        'Singara': 5,
        'Piajue': 5}
cart = []
total = 0

print("__________Foods____________")
for key,value in Foods.items():
    print(f'{key:10}: {value} Taka')
print("________________________________")

while True:
    request = input("Select a item (f to finish):")
    if request == 'f':
        break
    elif Foods.get(request) is not None:
        cart.append(request)


print('____________Your order_____________')
for request in cart:
    total += Foods.get(request)
    print(request, end=' ')
print()
print(f"Total amount is: {total:.2f} tk")
amount = float( input("  Please pay your money!:"))

if amount == total:
    print('     Thanks for paying your total amount!\n   See you later.ASSALAMUALIKUM.')
else:
    print("   Please pay full amount!!!!!!!!!")