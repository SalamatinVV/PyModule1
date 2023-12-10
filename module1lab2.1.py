money_capital = 373193.97
salary = 20000
spend = 50000
increase = 0.03
mounth = 0

while True:
    money_capital = money_capital + salary - spend

    if money_capital > 0:
        mounth += 1
        spend = spend + spend * increase
    else :
        break

print("Месяцы без долгов:", mounth)
