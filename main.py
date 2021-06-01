import random
import math

#Creates class called restaurant
class Restaurant:

    #Gives restaurant properties that can be called later in the game
    def __init__(self, owner, name, capacity, money, total):

        self.owner = owner
        self.name = name
        self.capacity = capacity
        self.money = money
        self.total = total
        self.employee = 1
        self.rating = 0


    #These following defs allow the program to change the properties of the restaurant
    def changeRating(self, num):
        self.rating += num

    def changeMoney(self, num):
        self.money += num

    def changeTotal(self, num):
        self.total += num

    def changeEmployees(self, num):
        self.employee += num

    def changeCapacity(self, num):
        self.capacity += num

    def resetMoney(self, num):
        self.money = num

    #These following defs return the contents of the variable in order to access them later in the program
    def getOwner(self):
        return self.owner

    def getRestaurantName(self):
        return self.name

    def getRating(self):
        return self.rating

    def getMoney(self):
        return self.money

    def getTotal(self):
        return self.total

    def getEmployee(self):
        return self.employee

    def getCapacity(self):
        return self.capacity

#creates class called food
class Food:

    #gives food properties that can be called later in the game
    def __init__(self, name, cost, type):

        self.name = name
        self.cost = cost
        self.type = type

    # These following defs allow the program to change the properties of the food
    def changeCost(self, num):
        self.cost += num

    def resetCost(self, num):
        self.cost = num

    # These following defs return the contents of the variable in order to access them later in the program
    def getFoodName(self):
        return self.name

    def getCost(self):
        return self.cost

    def getType(self):
        return self.type

global restaurant

#an array containing all the possible food items on the menu
entree = ["Noodles", "Pasta", "Burger", "Sandwich", "Pizza", "Rice", "Soup", "Ravioli", "Lasagna"]
appetizer = ["Muffin", "French Fries", "Garlic Bread", "Chips", "Cookies", "Popcorn", "Onion Rings", "Breadsticks"]
dessert = ["Ice Cream", "Apple Pie", "Pumpkin Pie", "Chocolate Cake", "Vanilla Cake", "Strawberry Cake"]
drink = ["Soda", "Milkshake", "Boba", "Tea", "Coffee", "Chai", "Mocktail", "Juice", "Smoothie"]

menu = []
revenue = []

#This def creates the restaraunt
def createRestaurant():
    global restaurant
    name = input("What is your name?\n")
    choice = input("\nHey " + name + "! You are going to own a restaurant!\nWhat would you like to name your restaraunt?\n")
    num = (random.randint(1, 5) * 100)
    restaurant = Restaurant(name, choice, random.randint(5, 10), num, num)

#This def will create all the food items in the restaraunt
def createMenu():

    #This removes food items from the food array in order to prevent repetition and adds it to the menu array
    for i in range(0, 5):
        temp = random.choice(entree)
        menu.append(Food(temp, round(random.uniform(5, 10), 2), "Entrée"))
        entree.remove(temp)

    for i in range(0, 2):
        temp = random.choice(appetizer)
        menu.append(Food(temp, round(random.uniform(2, 5), 2), "Appetizer"))
        appetizer.remove(temp)

    for i in range(0, 1):
        temp = random.choice(drink)
        menu.append(Food(temp, round(random.uniform(2, 5), 2), "Drink"))
        drink.remove(temp)


def printPart(course):
    #This prints all the items in the food menu
    print("\n" + course + ": \n")
    for x in menu:
        if x.getType() == course:
            print(str(x.getFoodName()) + ": $" + str(x.getCost()))

def printMenu():
    #This calls the printPart def 3 times with 3 different parameters
    #in order to print all the course options on the menu
    print("\n_______MENU_______")
    printPart("Entrée")
    printPart("Appetizer")
    printPart("Drink")


def printStats():
    global restaurant

    #Printing the stats of the restaurant
    print("\n" + restaurant.getRestaurantName() + "\nOwner: " + restaurant.getOwner() +
          "\nRating: " + str(restaurant.getRating()) + "\nMoney: $" + str(restaurant.getMoney())
          + "\nEmployees: " + str(restaurant.getEmployee()) + "\nCapacity: " + str(restaurant.getCapacity()))

def printInstructions():

    #Printing instructions
    print("\nHey, " + restaurant.getOwner() + "! You own the restaurant, " + restaurant.getRestaurantName()
          + ". Run your restaurant, earn money, make upgrades, and turn your little stand into a popular restaurant!")

def printRevenue():

    print("\nWeekly Total Profits\n")
    for i in range(1, len(revenue) + 1):
        print("Week " + str(i) +  ": $" + str(revenue[i - 1]))

def runRestaurant():
    global weeks

    print("\nHow many weeks do you want to run the restaurant?")
    inp = int(input(""))

    weeks += inp

    #Makes sure the user doesn't input a number greater than 5
    while inp > 5:
        print("\nThe number of weeks you want to run your restaurant is too large.")
        print("How many weeks do you want to run the restaurant?")
        inp = int(input(""))

    # Asks the player how many hours a week they want to run the restaurant
    print("\nHow many hours a week do you want to run the restaurant?")
    hours = int(input(""))

    # Makes sure the number of hours is less than 50 and greater than 25
    while hours > 50 or hours < 25:

        if hours > 50:
            print("\nWorking over 50 hours is very unhealthy.")
        else:
            print("\nWorking less than 25 hours a week is not enough")

        print("\nHow many hours a week do you want to run the restaurant?")
        hours = int(input(""))

    #Initializes a bunch of arrays that will contain the prices of different types of food
    entreeCost = []
    appetizerCost = []
    drinkCost = []

    #Runs through the entire menu and pushes price of food into its matching array
    for x in menu:
        if x.getType() == "Entrée":
            entreeCost.append(x.getCost())
        if x.getType() == "Appetizer":
            appetizerCost.append(x.getCost())
        if x.getType() == "Drink":
            drinkCost.append(x.getCost())

    #Finds the average price of each of the arrays
    temp1 = sum(entreeCost) / len(entreeCost)
    temp2 = sum(appetizerCost) / len(appetizerCost)
    temp3 = sum(drinkCost) / len(drinkCost)

    #Finds the average cost of a meal
    average = temp1 + temp2 + temp3

    #Variable that finds the weekly profits
    weekly = 0

    #Running calculation for weekly revenue the number weeks the user inputted
    for i in range(0, inp):
        #Avergae people visiting the restaurant
        num = random.randint(restaurant.getCapacity() - 5, restaurant.getCapacity())

        #Equation
        temp = restaurant.getEmployee() * num * hours * average

        #Rounds revenue to whole number
        temp = round(temp)
        weekly += temp

        restaurant.changeMoney(temp)
        revenue.append(restaurant.getMoney())

    #rounding numbers in order to prevent large number of digits
    #weekly = round(weekly)
    #money = round(restaurant.getMoney())

    #changes cost
    #restaurant.resetMoney(money)

    print("\nThe restaurant earned $" + str(weekly))
    print("The restaurant has a total of $" + str(restaurant.getMoney()))
    print("You have run the restaurant for a total of " + str(weeks) + " weeks")

def showOptions():
    optionMenu = True
    shopOpen = False

    # As long as the boolean optionMenu is true then the options will be continuously prompted
    while optionMenu:
        temp = input("\nOptions \n1: See Restaurant Stats \n2: See Menu \n3: See Instructions \n4: See Weekly Revenue"
                     "\n5: Upgrade Restaurant\n6: Exit\n")

        # Results of the number the user inputted
        if temp == "6":
            optionMenu = False
        elif temp == "1":
            printStats()
        elif temp == "2":
            printMenu()
        elif temp == "3":
            printInstructions()
        elif temp == "4":
            printRevenue()
        elif temp == "5":
            shopOpen = True

            # Opens shop and asks what they want to upgrade
            while shopOpen:
                print("\nUpgrades \nBank: $" + str(restaurant.getMoney()) + "\nWhat would you like to upgrade?"
                                                                            "\n1: Employees\n2: Menu\n3: Capacity\n4: Exit")
                inp = int(input(""))

                if inp == 4:
                    shopOpen = False
                else:
                    openUpgrades(inp)


def openUpgrades(choice):

    #If the player chooses to hire an employee
    if choice == 1:
        temp = int(input("\nHiring an employee costs $20,000 each, how many employees would you like to hire?\n"))

        #Checking that player has enough money to hire that many employees
        if restaurant.getMoney() >= (temp * 20000):
            restaurant.changeEmployees(temp)
            restaurant.changeMoney(-1 * temp * 20000)
            restaurant.changeRating(temp * .02)
        else:
            print("\nYou are too broke to buy " + str(temp) + " employees")

    #If the player chooses to upgrade menu
    elif choice == 2:
        print("\nWhat food item on the menu would you like to upgrade?\nIt costs $1000 to upgrade a food item once\n")

        temp = 1

        #Prints all the menu items
        for x in menu:
            print(str(temp) + ": " + x.getFoodName())
            temp += 1

        print("\nSpecial Menu Upgrades")
        print("\n" + str(temp) + ": Add Food Item - Cost: $3000")
        temp += 1
        print(str(temp) + ": Add Own Food Item - Cost: $5000")
        food = int(input(""))
        upgradeFood(food, temp)

    #If the player chooses to upgrade the capacity
    elif choice == 3:
        temp = int(input("\nIt takes $50,000 to increase the capacity once by 20 people."
                         "\nHow many times would you like to upgrade the capacity?\n"))

        #CHecking player has enough money to hire that many employees
        if restaurant.getMoney() >= (temp * 50000):
            restaurant.changeEmployees(20 * temp)
            restaurant.changeMoney(-1 * temp * 50000)
            restaurant.changeRating(temp * .2)
        else:
            print("\nYou are too broke to upgrade the capacity " + str(temp) + " times")


def upgradeFood(num, temp):

    #If the user chose to add own food item
    if temp == num:

        #Checking user has enough money
        if restaurant.getMoney() > 5000:
            restaurant.changeMoney(-5000)

            name = input("\nWhat would you like to name your food?\n")
            name = name.capitalize()

            type = int(input("\nWhat type of food item will this be?\n1: Entrée\n2: Appetizer\n3: Drink\n"))

            #Creating new object and adding to array based on the type of food that user chose
            if type == 1:
                menu.append(Food(name, round(random.uniform(5, 10), 2), "Entrée"))
            elif type == 2:
                menu.append(Food(name, round(random.uniform(2, 5), 2), "Appetizer"))
            else:
                menu.append(Food(name, round(random.uniform(2, 5), 2), "Drink"))

            printMenu()

        else:
            print("You are too broke to make this purchase.")

    #If user chose to add random food item
    elif temp - 1 == num:

        if restaurant.getMoney > 3000:
        # Picks which type of food to add to the menu
            restaurant.changeMoney(-3000)
            chance = random.randint(1, 3)

            if chance == 1:
                temp = random.choice(entree)
                menu.append(Food(temp, round(random.uniform(5, 10), 2), "Entrée"))
                entree.remove(temp)

            elif chance == 2:
                temp = random.choice(appetizer)
                menu.append(Food(temp, round(random.uniform(2, 5), 2), "Appetizer"))
                appetizer.remove(temp)

            else:
                temp = random.choice(drink)
                menu.append(Food(temp, round(random.uniform(2, 5), 2), "Drink"))
                drink.remove(temp)

            print("\nNew Food: " + temp)
            printMenu()


    else:
        print("\nThe current cost of " + menu[(num - 1)].getFoodName() + " is " + str(menu[(num - 1)].getCost()))
        inp = int(input("How many times would you like to upgrade the " + menu[(num - 1)].getFoodName() + "?\n"))

        #makes sure the player has enough money for purchase
        if restaurant.getMoney() > inp * 1000:

            #changes cost of the food item
            cost = menu[(num - 1)].getCost() + inp
            cost = round(cost, 2)
            menu[(num - 1)].resetCost(cost) 

            #Takes money from bank
            restaurant.changeMoney(-1 * inp * 1000)

        else:
            print("\nYou are too broke to upgrade " + menu[(num - 1)].getFoodName() + " " + str(inp) + " times")

        print("\nThe new cost is " + str(menu[(num - 1)].getCost()))

def randEvents():

    #This determines the 1 in 50 chance of winning a lottery or going bankrupt
    chance = random.randint(1, 50)
    if chance == 1:
        temp = random.randint(1, 10)
        print("\nYou won a lottery to finance your restaurant!")
        restaurant.changeMoney(temp * 100000)

    if chance == 2:
        print("\nYour restaurant went bankrupt!!")
        restaurant.resetMoney(0)

    #This determines a 1 in 10 chance of free employee or food item
    chance = random.randint(1, 10)
    if chance == 1:
        print("\nA chef was moved by you and decided to work at your restaurant for free")
        restaurant.changeEmployees(1)
        restaurant.changeRating(.02)

    if chance == 2:
        print("\nYou won the chance to add your own food item to the menu for free")
        restaurant.changeMoney(5000)
        upgradeFood(10, 10)

    #This determines the 1 in 20 chance of featured in magazine
    chance = random.randint(1, 20)
    if chance == 1:
        print("\nYour restaraunt was featured on a magazine with positive reviews.")
        restaurant.changeRating(1)

    if chance == 2:
        print("\nYour restaurant was featured on a magazine with negative reviews")
        restaurant.changeRating(-1)

    #This determines a 1 in 5 chance of a new food item in the menu
    chance = random.randint(1, 5)
    if chance == 1:
        print("\nYou won a new food item in the menu")
        restaurant.changeMoney(3000)
        upgradeFood(9, 10)


#def checkBank():

def main():
    global weeks

    playAgain = True
    createRestaurant()
    createMenu()
    printInstructions()
    weeks = 0

    while playAgain:
        printStats()
        runRestaurant()
        randEvents()
        #checkBank()

        #Makes sure the game doesn't run if player is bankrupt
        if restaurant.getMoney() > 0:
            temp = input("\nWould you like to continue playing? \n1: Yes\n2: No\n")
            if temp == "1":
                playAgain = True
                showOptions()
            else:
                playAgain = False
        else:
            print("\nSorry " + restaurant.getOwner() + ", but your restaurant went broke. Try Again!")
            printStats()
            playAgain = False
main()
    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
