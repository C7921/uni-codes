# Connor Sanders - Project 2
# Written in VSCode using Python 3.8.3 (64bit)

# ###---Setup Start---###

# #########################################################
# Note: This section could be a module e.g. housekeeping()
# #########################################################

# Required for displayMenu()
import time
delay = 1.5

# Range of orders.
# Increase to allow more orders
orderRange = range(1, 11)

# Tub costs based on size (Dict)
# To increase options, extend here in same format.
sizeCostDict = dict([('small', 5.50), ('regular', 15.00), ('party', 35.00)])

# Topping Costs based on sizes (Dict)
# To increase options, extend here in same format.
toppingCostDict = dict([('small', 2.00), ('regular', 4.50), ('party', 8.50)])

# Discount Codes - added to expand discount codes.
discountCodes = dict([('vip', 2.00), ('employee', 4.50), ('owner', 8.50)])

# Stores List of all costs entered. Sumed at end.
currentTotal = []

# ###---Setup End---###

# ###############################################

# ###---Modules Start---###

# Checks Discount Code.
def checkDiscountCode(customerCost):
    codeEntered = input("Please enter your coupon code. Press Enter to skip: ").lower()
    if codeEntered in discountCodes.keys():
        discount = discountCodes.get(codeEntered)
        print("Applying discount of", "${:.2f}".format(discount))
        cost = customerCost-discount
    else:
        print("Enter code not found, or none entered.")
        cost = customerCost
    return(cost)


# Ask for toppings, add to cost if yes.
def askToppings(size, customerCost):
    toppingChoice = 0
    while (toppingChoice != "y") or (toppingChoice != "n"):
        toppingChoice = input("Do you want to add toppings to this order? (Y/N) ").lower()
        if (toppingChoice[0] == "y"):
            cost = (customerCost+toppingCostDict.get(size))
            break
        elif (toppingChoice[0] == "n"):
            cost = customerCost
            break
        else:
            print("Sorry, that is not a valid input. ")
    return(cost)


# Asks user for size & validate.
def getSizeChoice(orderVol):
    i = 0
    while (i < orderVol):
      selectedSize = input("\nPlease enter a size selection: ").lower()
      if selectedSize in sizeCostDict.keys():
        customerCost = (sizeCostDict.get(selectedSize))
        customerCost = (askToppings(selectedSize, customerCost))
        print("Adding Value to Current Cost List:", "${:.2f}".format(customerCost))
        currentTotal.append(customerCost)
        i = i+1
        print("Selection:", i, "of", orderVol, "Completed. \nCurrent Order Cost:", "${:.2f}".format(sum(currentTotal)))
      else:
          print("Sorry, make a valid selection.")


# Get order volume. Checks between range.
def getOrderVol():
    orderVol = 0
    while (orderVol) < min(orderRange) or (orderVol > max(orderRange)):
        try:
            orderVol = int(input(
                f"Please enter how many tubs you would like to order ({min(orderRange)}-{max(orderRange)}): "))
        except ValueError:
            print("Sorry, that is not a valid input!")
        else:
            if (orderVol < min(orderRange) or (orderVol > max(orderRange))):
                print(
                f"Sorry, we cannot accept that number of orders. \nPlease enter between ({min(orderRange)}-{max(orderRange)}).")
    return orderVol


# Display menu
def displayMenu():
    print("Welcome to Yummy Galetaria!")
    print("==============================")
    time.sleep(delay)
    print("Please make a selection from the menu...")
    print("==============================")
    time.sleep(delay)
    print("Ice-Cream Tub Prices per Size:")
    for key, value in sizeCostDict.items():
        print(key.capitalize(), "==>", "${:.2f}".format(value))
    print("==============================")
    time.sleep(delay)
    print("Ice-Cream Topping Prices per Size:")
    for key, value in toppingCostDict.items():
        print(key.capitalize(), "==>", "${:.2f}".format(value))
    print("==============================")
    time.sleep(delay)


# ###---Modules End---###

# ###---Main Start---###
# Declarations are made at the top.
displayMenu()
customerVolume = getOrderVol()
print("Your have selected to order", customerVolume, "tubs of ice-cream.")

getSizeChoice(customerVolume)
totalCost = sum(currentTotal)

time.sleep(delay)
print("\nThank you for choosing Yummy Galetaria:\nYou ordered", customerVolume, "tubs of ice-cream.")
print("Your current cost is:", "${:.2f}".format(totalCost))
time.sleep(delay)

finalCost = checkDiscountCode(totalCost)
print("Your final discounted cost is: ${:.2f}".format(finalCost))
time.sleep(delay)
print("Come again soon. Bye!")

# ###---Main End---###
