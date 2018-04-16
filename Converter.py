amount_of_lvl = input("Please enter amount of LVL, which You want to convert to Euro: ")
amount_of_lvl = float(amount_of_lvl)
lvl_eur_rate = float(1.42)
eur_amount = amount_of_lvl * lvl_eur_rate
eur_amount = round(eur_amount, 2)

if amount_of_lvl >= 0:
    print(eur_amount)
else: print("Amount is wrong")


