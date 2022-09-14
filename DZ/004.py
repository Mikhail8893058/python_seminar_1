# quarter = int(input('Введите четверть:'))
# if quarter == 1: 
#     print('[+бесконечности;+бесконечности')
# if quarter == 2:
#     print('[-бесконечности;+бесконечности]')
# if quarter == 3:
#     print('[-бесконечности;-бесконечности]') 
# if quarter == 4:
#     print('[+бесконечности;-бесконечности]')  
# else:
#     print('Введите четверть от 1 до 4')    

while True:
    quarter = int(input('Введите четверть:'))
    if quarter == 1: 
        print('[+бесконечности;+бесконечности')
        break
    elif quarter == 2:
        print('[-бесконечности;+бесконечности]')
        break
    elif quarter == 3:
        print('[-бесконечности;-бесконечности]') 
        break
    elif quarter == 4:
        print('[+бесконечности;-бесконечности]') 
        break  
    else:
        print('Введите четверть от 1 до 4')    
