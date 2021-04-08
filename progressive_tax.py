#reddit [easy] challenge - progressive taxation

#below are the tax rate brackets
income_tax_0 = 0
income_tax_1 = 0.10
income_tax_2 = 0.25
income_tax_3 = 0.40

income = 56789
tax = 0

#0% tax
if income < 10000:
    print(income * income_tax_0)
#10% tax
if income >= 10000 and income < 30000:
    print((income - 10000) * income_tax_1)
#25% tax
if income >= 30000 and income < 100000:
    income_10_30 = 30000 * income_tax_1
    print(income_10_30 + (income - 30000) * income_tax_2)
#40% tax
#if income > 

#income
jim_income = 7500
doris_income = 25000
gordon_income = 75000
michael_income = 650000
