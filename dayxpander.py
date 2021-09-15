#returns given


years = 0
months = 0
weeks = 0
days = 0
balance = 0

def conv(number):
    global balance
    global years
    global months
    global weeks
    global days

    if number >= 365:
        years = number // 365
        balance = number % 365
    
    elif number < 365 and number >= 30:
        months = number // 30
        balance = number & 30
    
    elif number < 30 and number >= 7:
        weeks = number // 7
        balance = number & 7
    
    elif number < 7:
        days = number
        balance = 0

    while balance != 0:
        conv(balance)
    
    return(f"Given number has {years} years, {months} months, {weeks} weeks, {days} days.")


days = int(input("Enter number of days"))
print(conv(days))
