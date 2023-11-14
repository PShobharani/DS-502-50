# DS502-50 - Introduction to Computer Science
# Bestsellers
# Shobharani Polasa, Victor Davidson

def create_booklist(filename):
    with open(filename, 'r') as book_list:
        booklist = []
        for line in book_list:
            data = line.strip().split('\t')
            if len(data) == 5:
                title, author, publisher, date, category = data
                booklist.append(data)

        print(f'Read {len(booklist)} books')  

    return booklist

def print_books(book):
    print(f"{book[0]} by: {book[1]} (pub date: {book[3]})")

def search_author(books, author):
    found = False
    for book in books:
        if author.lower() in book[1].lower():
            print_books(book)
            found = True
    if not found:
        print("No books found for this search.")

def search_title(books, title):
    found = False
    for book in books:
        if title.lower() in book[0].lower():
            print_books(book)
            found = True
    if not found:
        print("No books found for this search.")

def search_yearRange(books, year1, year2):
    found = False
    for book in books:
        date = book[3].split('/')
        year = int(date[-1])
        if year1 <= year <= year2:
            print_books(book)
            found = True
    if not found:
        print("No books found for this search.")

def search_specificDate(books, month, year):
    found = False
    for book in books:
        date = book[3].split('/')
        month_g = int(date[0])
        year_g = int(date[-1])
        if month == month_g and year == year_g:
            print_books(book)
            found = True
    if not found:
        print("No books found for this search.")

def menu():
    try:
        books = create_booklist('bestsellers.txt')
    except IOError:
        print("Error: Could not read from file")
        return

    while True:
        print("\nWhat would you like to do?")
        print("\t1: Look up year range")
        print("\t2: Look up month/year")
        print("\t3: Search for author")
        print("\t4: Search for title")
        print("\tQ. Quit")

        option = input("\t> ").upper()

        if option == "1":
            year1 = int(input("Enter start year: "))
            year2 = int(input("Enter end year: "))
            search_yearRange(books, year1, year2)
        elif option == "2":
            month = int(input("Enter month (1-12): "))
            year = int(input("Enter year: "))
            search_specificDate(books, month, year)
        elif option == "3":
            author = input("Enter search string: ")
            search_author(books, author)
        elif option == "4":
            title = input("Enter search string: ")
            search_title(books, title)
        elif option == "q" or option == "Q":
            print("Done")
            break
        else:
            print("I don't understand this command.")

if __name__ == '__main__':
    menu()
