def get_yes_or_no(message):
    valid_input = False
    while not valid_input:
        answer = input(message)
        answer = answer.upper()
        if answer =='Y' or answer =='N':
            valid_input = True
        else:
            print('Please enter Y for yes or N for no.')
            
