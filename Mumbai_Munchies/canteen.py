class Snack:
    def __init__(self, snack_id, snack_name, price, availability):
        self.snack_id = snack_id
        self.snack_name = snack_name
        self.price = price
        self.availability = availability


class SnackInventory:
    def __init__(self):
        self.inventory = []
        self.sales_records = []

    def add_snack(self, snack_id, snack_name, price, availability):
        snacks = Snack(snack_id, snack_name, price, availability)
        self.inventory.append(snacks)
        print(f"Snack '{snack_name}' added to inventory.")

    def remove_snack(self, snack_id):
        for snack in self.inventory:
            if snack.snack_id == snack_id:
                self.inventory.remove(snack)
                print(f"Snack with ID '{snack_id}' removed from inventory.")
                return
        print(f"Snack with ID '{snack_id}' not found in inventory.")

    def update_snack_availability(self, snack_id, availability):
        for snack in self.inventory:
            if snack.snack_id == snack_id:
                snack.availability = availability
                print(f"Availability of snack with ID '{snack_id}' updated to '{availability}'.")
                return
        print(f"Snack with ID '{snack_id}' not found in inventory.")

    def sell_snack(self, snack_id):
        for snack in self.inventory:
            if snack.snack_id == snack_id:
                if snack.availability == "yes":
                    self.sales_records.append(snack)
                    snack.availability = "no"
                    print(f"Snack with ID '{snack_id}' sold.")
                    return
                else:
                    print(f"Snack with ID '{snack_id}' is not available for sale.")
                    return
        print(f"Snack with ID '{snack_id}' not found in inventory.")

    def display_inventory(self):
        print("Current Snack Inventory:")
        if self.inventory:
            for snack in self.inventory:
                print(f"ID: {snack.snack_id}, Name: {snack.snack_name}, Price: {snack.price}, Availability: {snack.availability}")
        else:
            print("Inventory is empty.")

    def display_sales_records(self):
        print("Sales Records:")
        if self.sales_records:
            for snack in self.sales_records:
                print(f"ID: {snack.snack_id}, Name: {snack.snack_name}, Price: {snack.price}")
        else:
            print("No sales records found.")


def main():
    inventory = SnackInventory()

    while True:
        print("\n===== Snack Inventory Menu =====")
        print("1. Add a snack to the inventory")
        print("2. Remove a snack from the inventory")
        print("3. Update snack availability")
        print("4. Sell a snack")
        print("5. Display current inventory")
        print("6. Display sales records")
        print("0. Exit")

        choice = input("Enter your choice (0-6): ")

        if choice == "0":
            print("Exiting the program...")
            break
        elif choice == "1":
            snack_id = input("Enter snack ID: ")
            snack_name = input("Enter snack name: ")
            price = float(input("Enter snack price: "))
            availability = input("Is the snack available? (yes/no): ")
            inventory.add_snack(snack_id, snack_name, price, availability)
        elif choice == "2":
            snack_id = input("Enter snack ID to remove: ")
            inventory.remove_snack(snack_id)
        elif choice == "3":
            snack_id = input("Enter snack ID to update availability: ")
            availability = input("Enter new availability (yes/no): ")
            inventory.update_snack_availability(snack_id, availability)
        elif choice == "4":
            snack_id = input("Enter snack ID to sell: ")
            inventory.sell_snack(snack_id)
        elif choice == "5":
            inventory.display_inventory()
        elif choice == "6":
            inventory.display_sales_records()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
