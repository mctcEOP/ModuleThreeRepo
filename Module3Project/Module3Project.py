# We'll create the menu first

flavors = ['chocolate', 'vanilla', 'strawberry', 'cookies \'n cream']
toppings = ['sprinkles', 'nuts', 'cherries', 'hot fudge', 'caramel']
prices = {"scoop": 2.50, "toppings": 0.50}

def display_menu():
    # Displays the menu

    print("\n--- Welcome to the Ice Cream Shop! ---")

    print("\nAvailable Flavors")
    for flavor in flavors:
        print(f"- {flavor}")
    
    print("\nAvailable Toppings")
    for topping in toppings:
        print(f"- {topping}")
    
    print("\nPrices:")
    print(f"Scoop: ${prices['scoop']:.2f} each")
    print(f"Toppings: ${prices['toppings']:.2f} each")

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

def calculate_total(num_scoops, num_toppings):
    # calculate total cost of order
    scoops_cost = num_scoops*prices["scoop"]
    toppings_cost = num_toppings*prices["toppings"]

    return scoops_cost + toppings_cost

def print_receipt(num_scoops, chosen_flavors, chosen_toppings):
    # prints the recipt to look pretty

    print("\n--- Your Ice Cream Order---")

    for i in range(num_scoops):
        print(f"Scoop {i + 1}: {chosen_flavors[i].title()}")

    if chosen_toppings:
        print("\nToppings:")
        for topping in chosen_toppings:
            print(f"- {topping.title()}")
    
    # prints the total
    total = calculate_total(num_scoops, len(chosen_toppings))
    print(f"\nTotal: ${total:.2f}")

    # Saves order to file
    with open("daily_orders.txt", "a") as file:
        file.write(f"\nOrder: {num_scoops} scoops - ${total:.2f}")

def main():
    display_menu()

    num_scoops, chosen_flavor = get_flavors()
    chosen_toppings = get_toppings()
    print_receipt(num_scoops, chosen_flavor, chosen_toppings)


if __name__ == "__main__":
    main()