money_capital = 10000
salary = 5000
spend = 6000
i = 0.05
alive = 0  #сколько можно выжить
while (money_capital - spend) >= 0:
 money_capital += salary - spend
spend *= (1 + i)
alive += 1
print(alive)