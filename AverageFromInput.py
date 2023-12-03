# DS502-50 - Introduction to Computer Science
# Shobharani Polasa
# AverageFromInput File with Exception Handling

import random

def generate_random_value():
    return random.uniform(1, 100)  # Generates a random float between 1 and 100

def main():
    try:
        total, count = sumNumbers()
        averageNumbers(total, count)
    except FileNotFoundError:
        print("The file could not be found.")
    except ValueError:
        print("Unexpected data. Please only input numbers.")
    except:
        print("An error occurred when trying to execute the program.")

def sumNumbers():
    try:
        infile = open('numbers.txt', 'r')
        total = 0
        count = 1
        for line in infile:
            try:
                number = float(line)
                total += number
                print(f"I read in {count} number(s). Current number is: {number:.2f} Total is: {total:.2f}")
                count += 1
            except ValueError:
                # If conversion fails, assign a random value
                number = generate_random_value()
                print(f"Error: Cannot convert '{line.strip()}' to a number. Assigned a random value: {number:.2f}")
                total += number
                count += 1
        infile.close()
        return total, count
    except FileNotFoundError:
        raise FileNotFoundError

def averageNumbers(total, count):
    try:
        average = total / (count - 1)
        print(f'Average: {average:.1f}')
    except ZeroDivisionError:
        print("Error: Cannot calculate the average of 0 numbers.")

# Call the main function.
if __name__ == '__main__':
    main()
