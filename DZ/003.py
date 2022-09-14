x = int(input('Введите координату X:'))
y = int(input('Введите координату Y:'))
if x >= 0 and y >= 0:
    print('1 четверть')
if x <= 0 and y >= 0:
    print('2 четверть')
if x <= 0 and y <= 0:
    print('3 четверть') 
if x >= 0 and y <= 0:
    print('4 четверть')           
