"""# Convert decimal to binary (as string)
bin(34)  # returns '0b100010' (0b just means binary)

# Convert binary to decimal
int('100010', 2)  # returns 34
int(0b100010)     # returns 34

"""

def Allergies(score):
    allergens = ['eggs', 'peanuts', 'shellfish', 'strawberries',
                 'tomatoes', 'chocolate', 'pollen', 'cats']
    lst = [allergens[i] for i in range(len(allergens)) if score & (1 << i)]
    return type('Allergies', (), {'lst': lst, 'is_allergic_to': lambda self, allergen: allergen in self.lst})()