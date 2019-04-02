from netmiko import ConnectHandler
from pprint import pprint
from openpyxl import load_workbook
import re

#================ READ EXCEL ===================

book = load_workbook('sample.xlsx')
current_sheet = book['wisnu']

def print_cell(column,row):
    return current_sheet[column+row].value

row = 4
loop = True
list_int = []
while loop:
    if print_cell('b',str(row)) is None:
        loop =  False
    else:
        list_int.append(print_cell('b',str(row)))
        row += 1

#print(list_int)
#================== CONNECT + PUSH COMMAND ==================

connect = ConnectHandler(device_type='cisco_ios', host='192.168.100.9', username='jawdat', password='jawdat123') 

list_bw_mentah = []

for interface in list_int:
    show_int = connect.send_command('sh int ' + str(interface))
    test = re.search()
    print(test)

#================== WRITE EXCEL ==================

#file_coba = book.active
#for data in data_int:
#    file_coba['c'+row]: test
