# Write a python program to Calculate Compound interest
principal = 10000
rate = 5        # 5% annual interest
time = 2        # 2 years
amount = principal * ((1 + rate / 100) ** time)
compound_interest = amount - principal
print("Compound Interest earned:", compound_interest)
