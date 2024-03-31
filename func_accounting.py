from ast import literal_eval
inventory = {
           "phone":    {"price":700,   "quantity":50},
           "keyboards":    {"price":700,   "quantity":50},
           "baterries":{"price": 65, "quantity":100},        
}

def load_balance():
     try:
        with open("balance.txt", "r") as Loaded_balance:
          loaded_Bal = Loaded_balance.read()
          #print(loaded_Bal)
        return int(loaded_Bal)

     except :
           print("File not found1")
           return 25000
     
def Load_Inventory():
     try:
          with open("inventory.txt", "r") as loaded_Inventory:
               inventory_list = loaded_Inventory.read()
               inventory_dict = literal_eval(inventory_list)
          return inventory_dict
     except:
          print("No inventory file  found")
          return {
           "phone":    {"price":700,   "quantity":50},
           "keyboards":    {"price":700,   "quantity":50},
           "baterries":{"price": 65, "quantity":100},        
           }

def load_history():
     try:
        with open("history.txt", "r") as Loaded_history:
          loaded_hist = Loaded_history.read()
          history_list = literal_eval(loaded_hist)
          #print(loaded_Bal)
        return (history_list)

     except :
           print("File not found")
           return []
           


     

def account(account_balance):
    print(f"\nBalance now is : {account_balance} Euro")

def balance(account_balance, history):
        print(f"- add\n- substract\n- check balance")
        command = input("please choose the option from the list above : ").lower()
        if  command == "add":
            amount= int(input("amount of money added is : "))
            account_balance += amount
            print(f"Balance now is : {account_balance} Euro")
            history.append(f"added {amount} Euro")
            return account_balance
            
        elif command == "substract".lower():
            amount= int(input("amount of money substracted is : "))
            account_balance -= amount
            print(f"Balance now is : {account_balance} Euro")
            history.append(f"substaracted amount is {amount} Euro")
            return account_balance
        
        elif command == "check balance".lower():
            print(f"{account_balance}")
            return account_balance
            
        else:
            print("\nError! Enter a valid option ")
        

def sales(account_balance, history, inventory):
    for k, v in inventory.items():
            print(f"\n{k.capitalize()} :")
            for s, t in v.items():
                print(f"-{s} - {t}")
    sold_items = {}

    item_name = input("what item you're selling: ").lower()
    if item_name in inventory:
        print(item_name)
        print( inventory[item_name]["quantity"])
        price = float(input("Provide price per item: "))
        quantity_sold = int(input("Provide the quantity of items you sold: "))
        if quantity_sold <= inventory[item_name]["quantity"]:
            sold_items[item_name]={"price" :price, "quantity": quantity_sold}
            inventory[item_name]["quantity"] = inventory[item_name]["quantity"] - quantity_sold
            account_balance += quantity_sold * price
            history.append(f"We sold {quantity_sold} {item_name} and we got {quantity_sold * price} Euro for them")
        else:
                print("Not enough quantity in stock")
    

    
    else:
        print("Item not found in our inventory list of items")

def purchase(account_balance, history, inventory ):
    purchased_items = {}

    item_to_buy = input("Provide item name you looking to buy: ").lower()
    price = float(input("Provide price per item: "))
    quantity_to_buy = int(input("Provide the quantity of items you want to purchase: "))

    purchased_items[item_to_buy] = {"price": price, "quantity" : quantity_to_buy }
    print("purchased Items : ", purchased_items)
    if item_to_buy in inventory :
        
        purchased_items[item_to_buy] = {"price": price, "quantity" : quantity_to_buy }
        inventory[item_to_buy]["quantity"] += quantity_to_buy
        account_balance -= quantity_to_buy * price
        history.append(f"We bought {quantity_to_buy} {item_to_buy} for  {quantity_to_buy * price} Euro")

    else:
        inventory.update(purchased_items )
        account_balance -= quantity_to_buy * price
        history.append(f"We bought {quantity_to_buy} {item_to_buy} for  {quantity_to_buy * price} Euro")

def my_list(inventory):
     #print(inventory)
       for k, v in inventory.items():
            print(f"\n{k.capitalize()} :")
            for s, t in v.items():
                print(f"{s} - {t}")   

def warehouse(inventory):
      product = input("what product you are looking for ? >")
      if product in inventory:
            print(f"we have {inventory[product]["quantity"]} {product}(s) in store and they cost {inventory[product]["price"]} for each")
      else:
            print(f"sorry no {product} in store at the moment")   

def review(history):
     for event in history:
            print (event) 

def save_balance(account_balance):
      with open ("balance.txt", "w") as balance_file:
            balance_file.write(str(account_balance))
            return account_balance
      
def save_inventory(inventory):
     try:
          with open("inventory.txt", "w") as inventory_file:
               inventory_file.write(str(inventory))
          
     except Exception as e:
          print(f"Error saving Inventory{e}")

def save_history(history):
     try:
          with open("history.txt", "w") as history_file:
               history_file.write(str(history))
          
     except Exception as e:
          print(f"Error saving Inventory{e}")

def end():
     print("Exiting ...\nbye")
