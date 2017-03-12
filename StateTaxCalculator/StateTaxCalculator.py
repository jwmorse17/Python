# a simple tax calculator
# tabs were used

import csv
def main():

    firstChoice = input("You can find the tax rate of a specific state with \'rate\' \n or calculculate the tax at total with \'calculate\' : ")

    if firstChoice == "rate":
        stateTaxRate()
    elif firstChoice == "calculate":
        calculate()
    else:
        print("That is not a valid input.")

def stateTaxRate():

    with open('stateTaxRates.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')

        rate = []
        state = []

        for row in readCSV:
            rates = row[1]
            states = row[0]

            rate.append(rates)
            state.append(states)

    whatState = input("What state do you want to know the tax rate of? ")
    rateIndex = state.index(whatState)
    theRate = rate[rateIndex]

    print('The Tax rate of', whatState, 'is', theRate, "%")

def calculate():

    with open('stateTaxRates.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')

        rate = []
        state = []

        for row in readCSV:
            rates = row[1]
            states = row[0]

            rate.append(rates)
            state.append(states)

    amount = int(input("What is the order ammount? "))
    stateOfPurchase = input("What state are you makeing the purchase? ")

    rateIndex = state.index(stateOfPurchase)
    theRate = float(rate[rateIndex])

    # formatt theRate. I.E tax rate of of 4 is formatted to 0.04
    formatted_theRate = theRate / 100

    taxTotal = amount * formatted_theRate

    total = taxTotal + amount

    print("{} has a tax rate of {}".format(stateOfPurchase, formatted_theRate))
    print("The subtotal is {}".format(amount))
    print("the tax ammount is {}".format(taxTotal))
    print("The total is {}".format(amount))


main()
