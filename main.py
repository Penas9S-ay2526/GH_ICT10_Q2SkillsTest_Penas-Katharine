from pyscript import display, document

def checking_details(e):
    document.getElementById('results').innerHTML = ' '
    user_input = document.getElementById('element').value.capitalize().strip()

    element_symbols = {
        'H':['H', 'Hydrogen', '1', '1.00'], 
        'N':['N', 'Nitrogen', '7', '14.00'],
        'O':['O', 'Oxygen', '8', '16.00'],
        'F':['F', 'Flourine', '9', '19.00'],
        'Cl':['Cl', 'Chlorine', '17', '35.45'],
        'Br':['Br', 'Bromine', '35', '79.90'],
        'I':['I', 'Iodine', '53', '126.90'],
        'S':['S', 'Sulfur', '16', '32.07'],
        'P':['P', 'Phosphorus', '15', '30.97'],
        'Se':['Se', 'Selenium', '34', '78.97'],
        'Si':['Si', 'Silicon', '14', '28.09'],
        'He':['He', 'Helium', '2', '4.00'],
        'C':['C', 'Carbon', '6', '12.01'],
        'Ne':['Neon', '10', '20.18'],
        'Ar':['Argon', '18', '39.95'],
        'Xe':['Xe', 'Xenon', '54', '131.29'],
        'Rn':['Rn', 'Radon', '86', '222'],
        }
    
    element_checker = user_input in element_symbols

    display_message = element_symbols.get(user_input, 'Element not found!')

    display(display_message, target='results')

    