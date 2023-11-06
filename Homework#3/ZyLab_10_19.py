# Name: Huzaifa Shoeb, ID: 1925670

class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_description(self):
        print(self.item_description)


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2016"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, item):
        for i, cart_item in enumerate(self.cart_items):
            if cart_item.item_name == item.item_name:
                if item.item_description != "none":
                    cart_item.item_description = item.item_description
                if item.item_price != 0:
                    cart_item.item_price = item.item_price
                if item.item_quantity != 0:
                    cart_item.item_quantity = item.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        num_items = 0
        for item in self.cart_items:
            num_items += item.item_quantity
        return num_items

    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += (item.item_price * item.item_quantity)
        return total_cost

    def print_total(self):
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
            return

        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Number of Items:", self.get_num_items_in_cart())
        print()

        for item in self.cart_items:
            print(f"{item.item_name} {item.item_quantity} @ ${item.item_price} = ${item.item_price * item.item_quantity}")

        print()
        print("Total:", "$" + str(self.get_cost_of_cart()))

    def print_descriptions(self):
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
            return

        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print()
        print("Item Descriptions")

        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")

        print()


def print_menu(cart):
    print("\nMENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit\n")


def main():
    print("Enter customer's name:")
    customer_name = input()
    print("Enter today's date:")
    current_date = input()

    print("\nCustomer name:", customer_name)
    print("Today's date:", current_date)

    cart = ShoppingCart(customer_name, current_date)


    while True:
        print_menu(cart)
        choice = input("Choose an option:\n")

        if choice == "a":

            print("\nADD ITEM TO CART")
            item_name = input("Enter the item name:\n")
            item_description = input("Enter the item description:\n")
            item_price = int(input("Enter the item price:\n"))
            item_quantity = int(input("Enter the item quantity:\n"))

            item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            cart.add_item(item)

        elif choice == "r":

            print("\nREMOVE ITEM FROM CART")
            item_name = input("Enter name of item to remove:\n")
            cart.remove_item(item_name)

        elif choice == "c":

            print("\nCHANGE ITEM QUANTITY")
            item_name = input("Enter the item name:\n")
            new_quantity = int(input("Enter the new quantity:\n"))
            item = ItemToPurchase(item_name, item_quantity=new_quantity)
            cart.modify_item(item)

        elif choice == "i":

            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()

        elif choice == "o":

            print("\nOUTPUT SHOPPING CART")
            cart.print_total()

        elif choice == "q":
            break




if __name__ == "__main__":
    main()
