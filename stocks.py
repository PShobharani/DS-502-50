# DS502-50 - Introduction to Computer Science
# Shobharani Polasa
# Programming Exercise 2
# Stock Transaction Program

COMMISSION_RATE = float(input("Enter commission rate percentage (ex 0.03) on stock purchase: "))

sellingCommission= float(input("Enter commission rate percentage (ex 0.03) on stock sale: "))

NUM_SHARES= float(input("Enter number of shares purchased: "))

stockSoldFor = float(input("Enter number of shares sold: "))

PURCHASE_PRICE  = float(input("Enter purchase price per share: "))

SELLING_PRICE  = float(input("Enter sell price per share: "))

amountPaidForStock =(NUM_SHARES*PURCHASE_PRICE)
amountPaidForStock2=(f'{amountPaidForStock:,.2f}') 
print("\nAmount paid for the stock: $", amountPaidForStock2)

purchaseCommission = (COMMISSION_RATE*amountPaidForStock)
purchaseCommission2=(f'{purchaseCommission:,.2f}') 
print("Commission paid on the purchase:  $", purchaseCommission2)

totalPaid = (amountPaidForStock + purchaseCommission)

stockSoldFor = (NUM_SHARES*SELLING_PRICE)
stockSoldFor2=(f'{stockSoldFor:,.2f}') 
print("Amount the stock sold for: $", stockSoldFor2)

sellingCommission = (COMMISSION_RATE*stockSoldFor)
sellingCommission2=(f'{sellingCommission:,.2f}') 
print("Commission paid on the sale: $", sellingCommission2)

totalReceived = (stockSoldFor - sellingCommission)

profit = (totalReceived-totalPaid)
profit2=(f'{profit:,.2f}') 
print("Profit (or loss if negative): $", profit2)

