#Defining Function with its calculations.
def compute_tax(chargeable_income):
    if chargeable_income <= 20000:
        tax = 0
    elif chargeable_income <= 30000:
        tax = (chargeable_income - 20000) * 0.02
    elif chargeable_income <= 40000:
        tax = (chargeable_income - 30000) * 0.035 + 200
    elif chargeable_income <= 80000:
        tax = (chargeable_income - 40000) * 0.07 + 550
    elif chargeable_income <= 120000:
        tax = (chargeable_income - 80000) * 0.115 + 3350
    elif chargeable_income <= 160000:
        tax = (chargeable_income - 120000) * 0.15 + 7950
    else:
        tax = (chargeable_income - 160000) * 0.18 + 13950 
    return tax

#Prompt user to enter Name, Annual income and total reliefs.
name = (input('Enter your name: '))

#While loop applied to annual income and total reliefs to make sure user inputs valid integer
while True:
    try:
        annual_income = int(input('Enter your annual income: $'))
    except:
        print('Please input a valid number in the annual income.')
        continue
    else:
        break
while True:
    try:
        total_relief = int(input('Enter your total reliefs: $'))
    except:
        print('Please input a valid number in the total reliefs.')
        continue
    else:
        break

chargeable_income = annual_income - total_relief

#call the function to compute tax
tax = compute_tax(chargeable_income)

#print out the results
print ('Your chargeable income: ${:0.2f}'.format(chargeable_income)) 
print ('Your total income tax: ${:0.2f}'.format(tax))