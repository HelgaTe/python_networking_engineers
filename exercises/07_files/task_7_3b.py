# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
vlan_sel=input('Enter VLAN number: ')

with open('CAM_table.txt','r') as f:
    for line in f:
        item=line.split()
        if item and item[0].isdigit():
            vlan,mac,_,intf=item
            if vlan==vlan_sel:
                print('{:10}{:20}{:5}'.format(vlan,mac,intf))
