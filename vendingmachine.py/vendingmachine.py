
#ITEMS OF THE MY VENDING MACHINE
class VendingMachine:
    def __init__(self):
        self.items = {
            'Drinks': {'Pepsi': 1.50, 'Water': 1.00, 'Sprite': 2.00, 'Coke': 3.00, 'Fanta': 3.00,
            'Dark Coffee': 5.00, 'Green Tea': 4.50, 'Espresso': 6.00},
            'snacks': {'Chips': 1.25, 'Chocolate': 1.75, 'Nuts': 1.50, 'Lays': 2.50, 'Doritos': 3.00},
        }
        self.balance = 0.0

#THE MENU HAVE A 2 DIFFERENT CATEGORIES DRIMKS AND SNACKS
    def display_menu(self):
        print("===== VENDING MACHINE MENU =====")
        print("1. Drinks")
        print("2. Snacks")
        

    def display_items(self, category):
        print(f"\n===== {category.upper()} =====")
        for i, (item, price) in enumerate(self.items[category].items(), 1):
            print(f"{i}. {item} - aed {price:.2f}") 

#YOU WILL CHOOSE WHAT CATEGORY DO YOU LIKE ON THE MENU
            
    def select_category(self):
        category = input("Please Select (1 for Drinks, 2 Snacks): ")
        return 'Drinks' if category == '1' else 'snacks'

    def select_item(self, category):
        item_number = int(input(f"Select an item number (1-{len(self.items[category])}): "))
        item_list = list(self.items[category].items())
        return item_list[item_number - 1]

#HERE IS THE CODE TO TRANSAC THE MONEY
    def insert_money(self):
        money = float(input("Insert money (in aed): "))
        return money

#HERE IS THE PROCESS OF TRANSACTION 
    def process_transaction(self, item):
        if self.balance >= item[1]:
            self.balance -= item[1]
            print(f"\nTransaction successful!.\nRemaining balance:  aed {self.balance:.2f}")
        else:
            print("Insufficient funds. Please insert more money.")

#THIS PART WILL SHOW THE SELECTED ITEM AND THE TRANSACTION PROCESS
    def run(self):
     while True:
        self.display_menu()
        category = self.select_category()
        self.display_items(category)
        selected_item = self.select_item(category)
        print(f"\nSelected item: {selected_item[0]} - aed {selected_item[1]:.2f}")
        self.balance += self.insert_money()
        self.process_transaction(selected_item)
        
        # Add a message indicating that the order has been dispensed
        print("Your order has been dispensed. Thank you!")

#HERE WILL ASK THE USER IF SHE/HE WANTS TO MAKE ANOTHER PURCHASE 
        another_purchase = input("Do you want to make another purchase? (y/n): ").lower()
        if another_purchase != 'y':
            break
    
if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.run()

