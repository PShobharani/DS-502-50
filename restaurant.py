# DS502-50 - Introduction to Computer Science
# Shobharani Polasa
# restaurant version 2

keepGoing = "yes"
while keepGoing == "yes":
    vegetarian = False
    vegan = False
    gluten_free = False
    
    is_vegetarian = str(input('Is anyone in your party vegetarian? ')).lower()
    if is_vegetarian == 'yes':
        vegetarian = True
        
    is_vegan = str(input('Is anyone in your party vegan? ')).lower()
    if is_vegan == 'yes':
        vegan = True
        
    is_gluten_free = str(input('Is anyone in your party gluten free? ')).lower()
    if is_gluten_free == 'yes':
        gluten_free = True

    print('Here are your restaurant choices: ')

    if vegetarian == False and vegan == False and gluten_free == False:
        print('Joe\'s Gourmet Burgers')

    if vegan == False and gluten_free == False:
        print('Mama\'s Fine Italian')

    if vegan == False:
        print('Main Street Pizza')

    print('Corner Cafe')
    print('Chef\'s Kitchen')
    
    keepGoing = input("Do you want to keep going(yes/no)? ")
print("Thanks for searching for a restaurant!")
