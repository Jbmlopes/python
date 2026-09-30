
paid = 0 #base value before any money is inserted

while paid < 50:
    print("Amount Due:", 50 - paid)
    coin = int(input("Insert Coin: "))

    if coin == 25 or coin == 10 or coin == 5:
        paid = paid + coin
    else:
        print("Coin not accepted")

change = paid - 50
print("Change Owed:", change)
