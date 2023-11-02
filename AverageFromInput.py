# DS502-50 - Introduction to Computer Science
# Shobharani Polasa
# AverageFromInput

def main():
    file_object = open('numbers.txt' ,'r')
    x = 0
    total = 0
    for nums in file_object:
        x = x + 1
        amount = float(nums)
        total = total + amount
        print(f"I read in {x} number(s) "f"Current number is:     {amount:.1f}"f"  Total is: {total:.1f}")
    file_object.close()
    average = total / x
    print (f"Average: {average:.1f}")

main()
