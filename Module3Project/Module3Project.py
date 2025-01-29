# We'll create the menu first

flavors = ['Chocolate', 'Vanilla', 'Strawberry', 'Cookies \'n Cream']
toppings = ['Sprinkles', 'Nuts', 'Cherries', 'Hot Fudge', 'Caramel']
prices = {"scoop": 2.50, "toppings": 0.50}

def display_menu():

    print("\n--- Welcome to the Ice Cream Shop! ---")
    print("\n Available Flavors")
    for flavor in flavors:
        print(f"- {flavor}")
    
    print("\n Available Toppings")
    for topping in toppings:
        print(f"- {topping}")

    print(f"Scoop: ${prices['scoop']:.2f} each")
    print(f"Toppings: ${prices['toppings']:.2f} each")


def main():
    display_menu

if __name__ == "__main__":
    main()