#creating a basic grocery calculator app
sum = 0
print("Welcome to the Grocery Calculator!")
while True:
    try:
        item = input("Enter the grocery item (or 'exit' to quit): ")
        if item.lower() == 'exit':
            print("Exiting the grocery calculator. Goodbye!")
            break
        
        price = float(input(f"Enter the price of {item}: "))
        quantity = int(input(f"Enter the quantity of {item}: "))
        
        total_cost = price * quantity
        print(f"The total cost for {quantity} {item}(s) is: ${total_cost:.2f}")
        sum += total_cost
        print(f"Current total cost of all items: ${sum:.2f}\n")
    
    except ValueError:
        print("Invalid input. Please enter numeric values for price and quantity.")
    except Exception as e:
        print(f"An error occurred: {e}")