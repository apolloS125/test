def show_menu():
    print("รายการสินค้าและราคา:")
    print("1. Khanom Jak             7 Baht")
    print("2. Khanom Kruy           13 Baht")
    print("3. Khanom Keemod          9 Baht")
    print("4. Khanom Co              3 Baht")
    print("5. Khanom Dokdon         22 Baht")

def cal_change(item_price, amount_paid):
    return amount_paid - item_price

def cal_coins(change):
    coin_values = [10, 5, 2, 1]
    coins = {10: 0, 5: 0, 2: 0, 1: 0}

    for coin in coin_values:
        while change >= coin:
            coins[coin] += 1
            change -= coin

    return coins

def display_change(coins):
    print("Change:", sum(coins.values()), "Baht")
    for value, count in coins.items():
        if count > 0:
            print(f"{value}: {count} coin")

def vending_machine():
    show_menu()
    order = int(input("Enter your order: "))
    quantities = int(input("Enter quantity: "))

    item_prices = {1: 7, 2: 13, 3: 9, 4: 3, 5: 22}
    selected_item_price = item_prices.get(order, 0) * quantities

    print(f"Total: {selected_item_price} Baht")

    amount_paid = 0
    while amount_paid < selected_item_price:
        amount = int(input('Enter your money: '))
        remaining = selected_item_price - amount_paid
        if amount < remaining:
            print("Insufficient amount. Please enter the correct amount.")
        else:
            amount_paid += amount

    change = cal_change(selected_item_price, amount_paid)
    if change > 0:
        coins = cal_coins(change)
        display_change(coins)
    print("Thank you")

vending_machine()
