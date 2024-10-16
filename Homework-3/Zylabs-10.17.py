# Prabhu Roka
# 1986444
class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${int(self.item_price)} "
              f"= ${int(self.item_quantity * self.item_price)}")


if __name__ == "__main__":
    print("Item 1")
    item1 = ItemToPurchase()
    item1.item_name = input("Enter the item name:\n")
    item1.item_price = float(input("Enter the item price:\n"))
    item1.item_quantity = int(input("Enter the item quantity:\n"))

    print("\nItem 2")
    item2 = ItemToPurchase()
    item2.item_name = input("Enter the item name:\n")
    item2.item_price = float(input("Enter the item price:\n"))
    item2.item_quantity = int(input("Enter the item quantity:\n"))

    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()

    total_cost = int((item1.item_price * item1.item_quantity)
                     + (item2.item_price * item2.item_quantity))
    print("\nTotal: $" + str(total_cost))
