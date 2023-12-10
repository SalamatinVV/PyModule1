mounth = 10
money_capital = 0
salary = 20000
spend = 50000
increase = 0.03

for i in range(mounth) :
    money_capital = money_capital + spend - salary
    spend = spend + spend * increase

money_capital = round(money_capital, 2)
print(money_capital)