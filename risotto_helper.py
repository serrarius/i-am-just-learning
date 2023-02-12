# A function for checking if the entered value is an integer number or a floating point number.
def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
       return False
while True:
    # The program prompts user to enter either the number of risotto servings or the weight of the rice with which we want to cook the risotto.
    # It's assumed that the user knows how to cook risotto.
    # It's also assumed that the portions should not be more than 12, and the rice should not be less than 50 grams.
    print('Введите в цифровом значении кол-во порций ризотто (не более 12) или вес риса в граммах (не менее 50): ', end='')    
    num0 = input()
    # Since in Russia the decimal separator is a comma, we need be able to replace the comma with a period.
    # The period will be replaced back by a comma in the output.
    if ',' in num0:
        num0 = num0.replace(',', '.')
    if isfloat(num0) and float(num0) > 0:
        num0 = float(num0)
        if num0 >= 50:
            num1 = num0
            print('\nДля приготовления ризотто из', str(num1).replace('.',','), 'г риса нужно взять:')        
            break
        # The cycle begins again if the user enters a number greater than 12 or less than 50.
        elif num0 > 12:
            print('Либо слишком много порций, либо слишком мало риса. Попробуйте еще раз.\n')   
        else:
            # Multiply the number of servings by the weight of the rice for one serving.
            # We take 62.5 grams as the weight of the rice for one serving.
            num1 = int(62.5 * num0)
            # If num0 is a number with digits other than zero after the decimal separator, we do not convert num0 to an integer.
            # If not, we need this conversion.
            # The word "порция", meaning portion, is declined in the genitive case.
            # If num0 == 1, the word is declined in the singular, otherwise it is declined in the plural.
            if num0 == 1:
                print('\nДля приготовления одной порции ризотто нужно взять:')
            elif num0 % 1 == 0:
                print('\nДля приготовления', int(num0), 'порций ризотто нужно взять:')
            else:
                print('\nДля приготовления', str(num0).replace('.',','), 'порций ризотто нужно взять:')
            print('риса —', num1, 'г;') 
            break           
    # The cycle starts again if user enter zero, a negative number or a value that is not a number.
    else:
        print('Введенное значение не является числом, либо не может быть применено для расчета. Попробуйте еще раз.\n')
# The program calculates and prints the amount of other ingredients based on the amount of rice in the specified proportions.
print('сливочного масла —', int(num1 * 0.3), end=' г, ')
print('из которого взять для жарки', int(num1 * 0.3 / 3), 'г', end=' ')
print('и оставить на конец', int(num1 * 0.3 / 3 * 2), 'г;')
print('сыра —', int(num1 * 0.24), 'г;')
print('лука —', int(num1 * 0.2), 'г;')
print('бульона —', int(num1 * 5), 'мл;')
print('вина —', int(num1 * 0.38), 'мл.\n')
import os
os.system('pause') 
