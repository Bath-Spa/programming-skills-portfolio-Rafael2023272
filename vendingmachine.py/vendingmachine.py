
#ITEMS OF THE MY VENDING MACHINE
#YOU CAN SEE THAT I PUT (COLD/HOT) IN A SPECIFIC DRINKS SO THAT THE USER WILL FULLY AWARE WHAT WAS THE ITEM HE ORDERED OR BUY.
class VendingMachine:
    def __init__(self):
        self.items = {
            'Drinks': {'Pepsi (COLD)': 1.50, 'Water (COLD)': 1.00, 'Sprite (COLD)': 2.00, 'Coke (COLD)': 3.00, 'Fanta (COLD)': 3.00,
            'Dark Coffee (HOT)': 5.00, 'Green Tea (HOT)': 4.50, 'Espresso (HOT)': 6.00},
            'Snacks': {'Oreo Cookies': 1.25, 'Chocolate Chips': 1.75, 'Nuts (CASHEW)': 1.50, 'Lays (Salt and vinegar)': 2.50, 'Doritos (Spicy)': 3.00},
        }
        self.balance = 0.0

#THE MENU HAVE A 2 DIFFERENT CATEGORIES DRIMKS AND SNACKS
    def display_menu(self):
        print("===== MENU =====")
        print("D. Drinks")
        print("S. Snacks")
        
#WILL DISPLAY THE ITEMS INCLUDED THEIR PRICES
    def display_items(self, category):
        print(f"\n===== {category.upper()} =====")
        for i, (item, price) in enumerate(self.items[category].items(), 1):
            print(f"{i}. {item} - {price:.2f} aed") 

#YOU WILL CHOOSE WHAT CATEGORY DO YOU LIKE ON THE MENU
#I USE D AND S AS A CODE FOR THE CATEGORY FOR DRINKS AND SNACKS    
    def select_category(self):
        category = input("Choose a Category (D for Drinks, S for Snacks): ")
        return 'Drinks' if category == 'D' else 'Snacks'

#I USE NUMBER 1 TO 8 FOR THE ITEMS SO IT WILL BE EASY TO UNDERSTAND
    def select_item(self, category):
        item_number = int(input(f" Please select an item number to proceed (1-{len(self.items[category])}): "))
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
            print(f"\nPayment successful!\nYour Change is: {self.balance:.2f} aed")

#THIS PART WILL SHOW THE SELECTED ITEM AND THE TRANSACTION PROCESS
    def run(self):
     while True:
        self.display_menu()
        category = self.select_category()
        self.display_items(category)
        selected_item = self.select_item(category)
        print(f"\nSelected item: {selected_item[0]} - Price {selected_item[1]:.2f} aed")
        self.balance += self.insert_money()
        self.process_transaction(selected_item)
        
        
    #Add a message indicating that the order has been dispensed
        print("Your order has been dispensed. Thank you! Have a Nice Day!")

#HERE WILL ASK THE USER IF SHE/HE WANTS TO MAKE ANOTHER PURCHASE 
        another_purchase = input("Do you want to make another purchase? (y/n): ").lower()
        if another_purchase != 'y':
            break
    
if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.run()

