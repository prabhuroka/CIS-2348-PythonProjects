# Prabhu Roka
# 1986444
class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0
        self.item_description = "none"

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${int(self.item_price)} "
              f"= ${int(self.item_quantity * self.item_price)}")

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")


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
        for cart_item in self.cart_items:
            if cart_item.item_name == item.item_name:
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
        return int(total_cost)

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Number of Items:", self.get_num_items_in_cart())
        print()
        if self.cart_items:
            for item in self.cart_items:
                item.print_item_cost()
            print()
            print(f'Total: ${int(self.get_cost_of_cart())}')
        else:
            print("SHOPPING CART IS EMPTY\n")
            print("Total: $0")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}\n")
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()

    @staticmethod
    def print1():
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit\n")


def print_menu(shopping_cart):
    ShoppingCart.print1()
    while True:
        choice = input("Choose an option:\n")
        if choice == 'q':
            break
        elif choice == 'a':
            print("\nADD ITEM TO CART")
            item = ItemToPurchase()
            item.item_name = input("Enter the item name:\n")
            item.item_description = input("Enter the item description:\n")
            item.item_price = float(input("Enter the item price:\n"))
            item.item_quantity = int(input("Enter the item quantity:\n"))
            ShoppingCart.print1()
            shopping_cart.add_item(item)
        elif choice == 'r':
            print("\nREMOVE ITEM FROM CART")
            item_name = input("Enter name of item to remove:\n")
            shopping_cart.remove_item(item_name)
            ShoppingCart.print1()
        elif choice == 'c':
            print("\nCHANGE ITEM QUANTITY")
            item = ItemToPurchase()
            item.item_name = input("Enter the item name:\n")
            item.item_quantity = int(input("Enter the new quantity:\n"))
            shopping_cart.modify_item(item)
            ShoppingCart.print1()
        elif choice == 'i':
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            shopping_cart.print_descriptions()
            ShoppingCart.print1()
        elif choice == 'o':
            print("OUTPUT SHOPPING CART")
            shopping_cart.print_total()
            ShoppingCart.print1()
        else:
            pass


def main():
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")

    print("\nCustomer name:", customer_name)
    print("Today's date:", current_date)

    shopping_cart = ShoppingCart(customer_name, current_date)
    print_menu(shopping_cart)


if __name__ == "__main__":
    main()
