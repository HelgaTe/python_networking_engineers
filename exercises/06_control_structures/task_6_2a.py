# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip=input('Enter IP-address : ')
octets = ip.split('.')

# если разделителем являеться точка, то метод выдаст элементы (ровно 4) для
# дальнейшей проверки; если разделитель не точка, метод split() отработает
# некорректно и будем иметь дело с одним элементом

correct_ip=True

if len(octets)!=4: # проверить что адрес состоит из 4-х элементов
    correct_ip=False # если не правда -> состоит не из 4-х элементов -> продолжаем проверку дальше
else:
    for item in octets:
        if not(item.isdigit() and int(item) in range(256)): #проверка, что состоит из 4 чисел и каждое число в диапазоне от 0 до 255
            correct_ip=False # если не правда -> условия не выполнены, просим повторно внести ip-address (блок ниже)
            break
if not correct_ip:
    print('Неправильный IP-адрес')
    ip=input('Enter IP-address : ')
else:
    if int(octets[0]) in range(1,224):
        print('unicast')
    elif int(octets[0]) in range(224,240):
        print('multicast')
    elif ip=='255.255.255.255':
        print('local broadcast')
    elif ip=='0.0.0.0':
        print('unassigned')
    else:
        print('unused')
