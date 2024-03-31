from func_accounting import account, balance, sales, purchase, warehouse, review, my_list, end, save_balance, load_balance, save_inventory,Load_Inventory, save_history, load_history

inventory = {
           "phone":    {"price":700,   "quantity":50},
           "keyboards":    {"price":700,   "quantity":50},
           "baterries":{"price": 65, "quantity":100},
           
}



account_balance = load_balance()
inventory = Load_Inventory()
price = 0
purchased_items = {}
sold_items = {}
history = load_history()

while True:
    
    
    print("\nWelcome to our Warehouse Accounting System, our options are as follow:) \n")
    print(f"""-1. balance\n-2. sales\n-3. purchase\n-4. account\n-5. list
-6. warehouse\n-7. review\n-8. End\n-9. Save balance\n-10. Save Inventory\n-11. Save History""")
    option = input("please choose the option from the list above : ").lower()


    if option == "account".lower() or option == "4":
        account(account_balance)
        
    elif option == "balance".lower()or option == "1":
        account_balance = balance(account_balance, history)
        #with open("balance.txt", "a") as balance_file:
         #       balance_file.writelines(f"balance is now : {account_balance} Euro\n")
        

    elif option == "sales".lower() or option == "2":  
        sales(account_balance, history, inventory)   
       
    elif option == "purchase".lower() or option == "3":
        purchase(account_balance, history, inventory)
       
    elif option == "list".lower() or option == "5":
        my_list(inventory)
       
    elif option == "warehouse".lower() or option == "6":
       warehouse(inventory)

    elif option == "review".lower() or option == "7":
        review(history)


    elif option == "End".lower()or option == "8":
         end()
         break
    elif option == "Save balance".lower() or option == "9":
        account_balance = save_balance(account_balance)
    
    #elif option == "12" or option == "Load Balance".casefold():
    #    load_balance()

    elif option == "Save Inventory" or option == "10":
        save_inventory(inventory)

    elif option == "Save History".lower() or option == "11":
        history = save_history(history)
    
   

   