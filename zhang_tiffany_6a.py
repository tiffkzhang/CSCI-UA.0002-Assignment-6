import keyword

# variable = input('Enter your Python variable name: ')

def variable(name):

    if name[0].isdigit() or keyword.iskeyword(name) == True:
        print('This is not a valid variable name.')
    else:
        for i in name[1:]:
            if (i.isalpha() == False) and (i.isdigit() == False) and (i != '_'):
                print('This is not a valid variable name.')
                return # exits the function 
        print('This is a valid variable name.')

variable('tiffany')
