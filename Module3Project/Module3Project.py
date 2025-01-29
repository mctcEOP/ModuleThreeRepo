# We'll create the menu first

flavors = ['chocolate', 'vanilla', 'strawberry', 'cookies \'n cream', 'mint', "pistachio"]
toppings = ['sprinkles', 'nuts', 'cherries', 'hot fudge', 'caramel']
cones = ['waffle', 'cake', 'sugar']

prices = {"scoop": 2.50, "toppings": 0.50, "specialCones": 0.50}

def display_menu():
    # Displays the menu

    print("\n--- Welcome to the Ice Cream Shop! ---")

    print("\nAvailable Flavors")
    for flavor in flavors:
        print(f"- {flavor}")
    
    print("\nAvailable Toppings")
    for topping in toppings:
        print(f"- {topping}")
    
    print("\nAvailable Cones")
    for cone in cones:
        print(f"- {cone}")
    
    print("\nPrices:")
    print(f"Scoop: ${prices['scoop']:.2f} each")
    print(f"Toppings: ${prices['toppings']:.2f} each")
    print(f"None-Waffle Cones: ${prices['specialCones']:.2f}")

def get_flavors():
    # gets the flavor choice from customer
    chosen_flavors = []

    # gets number of scoops
    while True:
        try:
            num_scoops = int(input("\nHow many Scoops would you like? (1-3):"))
            if 1 <= num_scoops <= 3:
                break
            print("Please choose a number between 1 and 3 scoops.")
        except ValueError:
            print("Please enter in a valid number")

    print("\nFor each scoop, enter the flavor you'd like")

    # gets flavor for each scoop
    for i in range(num_scoops):
        while True:
            flavor = input(f"Scoop {i+1}: ").lower()
            if flavor in flavors:
                chosen_flavors.append(flavor)
                break
            print("Sorry, that flavor is unavailable.")

    return num_scoops, chosen_flavors

def get_toppings():
    # gets the toppings choice from customer
    chosen_toppings = []
    while True:

        topping = input("\nEnter your toppings of choice (When you're finish type 'done'): ").lower()
        if topping == 'done':
            break

        if topping in toppings:
            chosen_toppings.append(topping)
            print(f"Added {topping}!")
        else:
            print("Sorry, that topping is unavailable")
       
    return chosen_toppings


def get_cone():
    # more easier than flavors and toppings since you're not getting several cones for a single order
    while True:
        cone = input("\nEnter your desired cone type: ").lower()
        if cone in cones:
            break
        else:
            print("Sorry, that cone-type is unavailable")
    
    return cone    

def calculate_total(num_scoops, num_toppings, coneType):
    # calculate total cost of order
    scoops_cost = num_scoops*prices["scoop"]
    toppings_cost = num_toppings*prices["toppings"]

    #I'm charging extra for 'none-waffle cones' since 'waffle cones' are the standard
    if coneType != 'waffle':
        cone_cost = prices["specialCones"]
    else:
        #if waffle then there will be no cost
        cone_cost = 0


    total = scoops_cost + toppings_cost + cone_cost

    # %10 discounts for orders above ten dollars
    discountAdded = False
    if total > 10:
        discountAdded = True
        total = total - (total * 0.10)

    return total, discountAdded

def print_receipt(num_scoops, chosen_flavors, chosen_toppings, coneType):
    # prints the recipt to look pretty

    print("\n--- Your Ice Cream Order---")

    for i in range(num_scoops):
        print(f"Scoop {i + 1}: {chosen_flavors[i].title()}")

    if chosen_toppings:
        print("\nToppings:")
        for topping in chosen_toppings:
            print(f"- {topping.title()}")

    print(f"\nCone: {coneType.title()}")

    # prints the total
    total, discount = calculate_total(num_scoops, len(chosen_toppings), coneType)

    # prevents new line. Source: https://stackoverflow.com/questions/26697462/print-to-previous-line
    print(f"\nTotal: ${total:.2f}", end="")
    if discount:
        print(" %10 Discount added")

    # Saves order to file
    with open("daily_orders.txt", "a") as file:
        file.write(f"\nOrder: {num_scoops} scoops - ${total:.2f}")

def orderOrBrowseMenu():
    # Creates a menu screen where you can search flavors before ordering
    while True:
        try:
            orderOrBrowse = str(input("\nWould you like to order or browse the flavor catalog?(Enter 'order' or 'browse'): ")).lower()
            if orderOrBrowse == 'order':
                num_scoops, chosen_flavor = get_flavors()
                chosen_toppings = get_toppings()
                coneType = get_cone()
                print_receipt(num_scoops, chosen_flavor, chosen_toppings, coneType)
                break
            if orderOrBrowse == 'browse':
                search = str(input("What are you looking for today?: ")).lower()
                if search in flavors:
                    print("\nThis flavor is in stock!")
                else:
                    print("\nWe couldn't find the flavor you have requested, please try again.")
        except ValueError:
            print("Please enter a valid string")

def main():
    display_menu()
    orderOrBrowseMenu()

if __name__ == "__main__":
    main()