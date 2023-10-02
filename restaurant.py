# DS502-50 - Introduction to Computer Science
# Shobharani Polasa
# restaurant

vegetarian = False
vegan = False
gluten_free = False


is_vegetarian = str(input('Is anyone in your party vegetarian?')).lower()
if is_vegetarian == 'yes' or is_vegetarian == 'Yes':
    vegetarian = True
    
is_vegan = str(input('Is anyone in your party vegan?')).lower()
if is_vegan == 'yes' or is_vegan == 'Yes':
    vegan = True
    
is_gluten_free = str(input('Is anyone in your party gluten free?')).lower()
if is_gluten_free == 'yes' or is_gluten_free == 'Yes':
    gluten_free = True

print('Here are your resaurant choices:')

if vegetarian == False and vegan == False and gluten_free == False:
    print('Joe\'s Gourmet Burgers')

if vegan == False and gluten_free == False:
    print('Mama\'s Fine Italian')

if vegan == False:
    print('Main Street Pizza')

print('Corner Cafe')
print('Chef\'s Kitchen')
