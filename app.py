from model.customer import CustomerAccount

def get_selected_menu() -> str:
    return input("""1. Register a new Customer Account
2. Check Balance of Customer's Account
3. Show all Records
4. Exit
Choose [1-4]:""")

text = input(f"Welcome to {CustomerAccount.bank_name} CLI system.\nPress Enter to proceed...\n")

records = {}

opt = get_selected_menu()

while opt != "4":
    if opt == "1":
        acc_no = input("Input the Customer's account number:")
        acc_type = input("Input the Customer's type of account:")
        balance = input("Input the Customer's initial deposit amount:")
        customer = CustomerAccount(acc_no, acc_type, balance)
        records[acc_no] = customer
        print(f"{customer}is registered into the system.\n")
        opt = get_selected_menu()
    elif opt == "2":
        selected_acc_no = input("Enter the Customer's account number:")
        selected_customer = records[selected_acc_no] if selected_acc_no in records.keys() else None 
        if selected_customer is not None:
            print(f"{selected_customer}")
        else:
            print(f"Customer with account number {selected_acc_no} cannot be found!\n")
        opt = get_selected_menu()
    elif opt == "3":
        i = 1
        for key in records.keys():
            print(f"#{i}")
            print(f"{records[key]}\n")
            i += 1
        opt = get_selected_menu()
    else:
        break
