import os
print(os.listdir())

with open('D:\Languages\GitHub\Python_mini_project\currency_cal\currencyData.txt') as f:
    lines = f.readlines()
    
currencyDict = {}
for line in lines:
    parsed = line.strip().split('\t')
    if len(parsed) == 3:
        currencyDict[parsed[0]] = parsed[2]

amount = float(input("Enter the amount: \n"))

print("Available currencies:")
for item in currencyDict.keys():
    print(item)

currency = input("\nEnter the currency you want to convert this amount to:\n")

if currency in currencyDict:
    converted_amount = amount * float(currencyDict[currency])
    print(f"{amount} INR is {converted_amount:.2f} {currency}")
else:
    print("Currency not found in the list.")
