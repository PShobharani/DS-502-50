# DS502-50 - Introduction to Computer Science
# Shobharani Polasa
# Expense Pie Chart

#import pip
#pip.main(['install','matplotlib'])
#pip install matplotlib

import matplotlib.pyplot as plt
import random

def generate_random_value():
    return random.randint(100, 1000)  # Generates a random value between 100 and 1000

def main():
    # initialize variables
    categories = []
    amounts = []

    # open file and read data
    try:
        with open('expenses.txt', 'r') as file:
            for line in file:
                line = line.strip()
                # checks to make sure the line is not empty
                if len(line) > 0: 
                    label, cost = line.split('\t')
                    try:
                        # Try to convert cost to an integer, if it fails, use 0 or generate a random value
                        amount = int(cost)
                    except ValueError:
                        # If conversion fails, assign 0 as the default value
                        # For text entries, generate a random value
                        amount = generate_random_value()
                        print(f"Error: '{cost}' is not a valid integer. Assigned a random value: {amount}")

                    categories.append(label)
                    amounts.append(amount)

        # create pie chart
        if len(amounts) > 0:
            colors = ('blue', 'orange', 'green', 'red', 'magenta', 'brown', 'cyan')
            plt.pie(amounts, labels=categories, colors=colors, autopct='%.2f%%')
            plt.title('Monthly Expenses')
            plt.show()
        else:
            print("No valid data to create a chart.")

    except IOError:
        print("Error: Could not open file 'expenses.txt'.")

if __name__ == "__main__":
    main()
