# DS502-50 - Introduction to Computer Science
# Shobharani Polasa
# AverageFromInput

def main():
    try:
        total, count = sumNumbers()
        averageNumbers(total, count)
    except:
        print("An error occured when trying to execute the program.")
        
def sumNumbers():
    infile = open('numbers.txt', 'r')
    total = 0
    count = 1
    for line in infile:
        number = float(line)
        total += number
        print(f"I read in {count} number(s) "f"Current number is:     {number:.2f}"f"  Total is:  {total:.2f}")
        count+=1
    return total, count

def averageNumbers(total, count):
    average = total/(count-1)
    print(f'Average: {average:.1f}')

# Call the main function.
if __name__ == '__main__':
    main()
