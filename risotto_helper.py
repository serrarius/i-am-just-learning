max_portions = 12
min_rice = 50
rice_in_portion = 62.5

# Since in Russia the decimal separator is a comma, we need be able to replace the comma in the entered value with a period to work with value.
def comma_to_period(value):
    return value.replace(',', '.')

def float_period(value):
    return float(comma_to_period(value))

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# If we need to print a floating point number, we change the period back to a comma.
def int_or_comma(value):
    if value % 1 == 0:
        return int(value)
    else:
        return (str(value)).replace('.', ',')

# Function for correct declination of the word "portion" in the output depending on the number of portions.
def portions_s_or_pl(value):
    if value == 1:
        return 'одной порции'
    else:
        return f'{int_or_comma(value)} порций'

while True:
    # The program prompts user to enter either the number of risotto servings or the weight of the rice with which we want to cook the risotto.
    # It's assumed that the user knows how to cook risotto.
    # It's also assumed that the portions should not be more than 12, and the rice should not be less than 50 grams.
    print('Введите в цифровом формате кол-во порций ризотто (не более 12) или вес риса в граммах (не менее 50): ', end='')
    entered_value = comma_to_period(input())
    if is_float(entered_value) == False:
        print('Введенное значение не является числом или введено в некорректном формате. Попробуйте еще раз.\n')
        continue
    else:
        entered_value = float(entered_value)
    if 0 >= entered_value:
        print('Введенное значение не может быть применено для расчета. Попробуйте еще раз.\n')
        continue
    elif max_portions < entered_value < min_rice:
        print('Либо слишком много порций, либо слишком мало риса. Попробуйте еще раз.\n')
        continue
    elif 0 < entered_value <= max_portions:
        amount_of_rice = entered_value * rice_in_portion
        print(f'''\nДля приготовления {portions_s_or_pl(entered_value)} ризотто нужно взять:
риса — {int(amount_of_rice)} г;''')
        break
    else:
        print(f'''Для приготовления ризотто из {int_or_comma(entered_value)} г риса нужно взять:''')
        amount_of_rice = int(entered_value)
        break
    
    
# The program calculates and prints the amount of other ingredients based on the amount of rice in the specified proportions.
print(f'''сливочного масла — {int(amount_of_rice * 0.3)} г,''',
f'''из которого взять для жарки {int(amount_of_rice * 0.3 / 3)} г''',
f'''и оставить на конец {int(amount_of_rice * 0.3 / 3 * 2)} г,
сыра — {int(amount_of_rice * 0.24)} г;
лука — {int(amount_of_rice * 0.2)} г;
бульона — {int(amount_of_rice * 5)} мл;
вина — {int(amount_of_rice * 0.38)} мл.''')
import os
os.system('pause')
