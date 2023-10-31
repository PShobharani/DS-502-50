# DS502-50 - Introduction to Computer Science
# Shobharani Polasa
# AverageFromInput

def read_numbers(file_name):
    objects = []
    with open(file_name, 'r') as file:
        for line in file:
            number = float(line.strip())
            objects.append(number)
    return objects

def calculate_average(objects):
    average = sum(objects) / len(objects)
    return average

def print_average(average):
    try:
        print("Average:", average)
        
    except FileNotFoundError:
        print("Error: File not found")
        return None
    except ValueError:
        print("Error: Invalid value in file")
        return None
    
def print_numbers(objects):
    x = 0
    total = 0
    for nums in objects:
        amount = float(nums)
        total = total + amount
        x = x + 1
        print(f"I read in {x} number(s) "f"Current number is:     {amount:.2f}"f"  Total is:  {total:.2f}")

def main():

    file_name = 'numbers.txt'
    objects = read_numbers(file_name)
    print_numbers(objects)
    average = calculate_average(objects)
    print_average(average)

if __name__ == '__main__':
    main()

