# DS502-50 - Introduction to Computer Science
# Shobharani Polasa
# Expense Pie Chart

#import pip
#pip.main(['install','matplotlib'])
#pip install matplotlib

import matplotlib.pyplot as plt

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
                        # Try to convert cost to an integer, if it fails, use 0
                        amount = int(cost)
                    except ValueError:
                        # If conversion fails, assign 0 as the default value
                        amount = 0
                        print(f"Error: '{cost}' is not a valid integer. Converted '{cost}' to an integer and assigned 0.")

                    categories.append(label)
                    amounts.append(amount)

        # create pie chart
        # We can change the chart name and pie slice colors as well
        # autopct='%.2f%%' show the pecentage of slice
        if len(amounts) > 0:
            plt.pie(amounts, labels=categories, colors=('blue', 'orange', 'green', 'red', 'magenta', 'brown', 'cyan'), autopct='%.2f%%')
            #plt.pie(amounts, labels=categories, colors=('blue', 'orange', 'green', 'red', 'magenta', 'brown', 'cyan'))
            plt.title('Monthly Expenses')
            plt.show()
        else:
            print("No valid data to create a chart.")

    except IOError:
        print("Error: Could not open file 'expenses.txt'.")

if __name__ == "__main__":
    main()






