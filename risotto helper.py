def isfloat(value):
    try:
       float(value)
    except ValueError:
       return False
    return True
while True:
    print('Введите в цифровом значении кол-во порций ризотто (не более 12) или вес риса в граммах (не менее 60): ', end='')    
    num0 = input()
    if isfloat(num0) and float(num0) > 0:
        num0 = float(num0)
        if num0 >= 60:
            num1 = num0
            print('Для приготовления ризотто из', num1, 'г риса нужно взять:')        
            break
        elif num0 > 12:
            print('Либо слишком много порций, либо слишком мало риса. Попробуйте еще раз.')   
        else:
            num1 = int(62.5 * num0)
            if num0 == 1:
                print('Для приготовления одной порции ризотто нужно взять:')
            else:
                print('Для приготовления', num0, 'порций ризотто нужно взять:')
            print('риса —', num1, 'г;') 
            break           
    else:
        print('Введенное значение не является числом, либо не может быть применено для расчета. Попробуйте еще раз.')
print('сливочного масла —', int(num1 * 0.3), end=' г, ')
print('из которого взять для жарки', int(num1 * 0.3 / 3), 'г', end=' ')
print('и оставить на конец', int(num1 * 0.3 / 3 * 2), 'г;')
print('сыра —', int(num1 * 0.24), 'г;')
print('лука —', int(num1 * 0.2), 'г;')
print('бульона —', int(num1 * 5), 'мл;')
print('вина —', int(num1 * 0.38), 'мл.')
import os
os.system('pause') 
