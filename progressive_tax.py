#reddit [easy] challenge - progressive taxation
#link https://www.reddit.com/r/dailyprogrammer/comments/cdieag/20190715_challenge_379_easy_progressive_taxation/

class progressive_tax():

    income = 1234567

    #0% tax
    if income < 10000:
        print("Your tax on: £", income, "is £", income * 0)
    #10% tax
    if income >= 10000 and income < 30000:
        print("Your tax on: £", income, "is £", (income-10000) * 0.1)
    #25% tax
    if income >= 30000 and income <= 100000:
        print("Your tax on: £", income, "is £", ((income - 10000) * 0.1) + ((income - 30000) * 0.15)) 
    #40% tax
    if income > 100000:
        print("Your tax on: £", income, "is £", ((income-10000) * 0.10) + ((income - 30000) * 0.15) + ((income - 100000) * 0.15))
        
 