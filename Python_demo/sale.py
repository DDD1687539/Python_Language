# Coder: Lee
# Time:  2022/11/5 12:10

import prettytable as pt

def show_ticket(row_num):
    tb = pt.PrettyTable()
    tb.field_names = ['行号', '座位1', '座位2', '座位3', '座位4', '座位5']
    for i in range(row_num):
        lst = [f'第{i+1}行', '有票', '有票', '有票', '有票', '有票']
        tb.add_row(lst)
    print(tb)

if __name__ == '__main__':
    row = 13
    show_ticket(row)











