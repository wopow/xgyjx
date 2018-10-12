from openpyxl import Workbook
from openpyxl.styles import Border, Side, Alignment


def set_border():
    bd = Side(style='thin', color="000000")  #设置单元格边框为细线，颜色为黑色
    border = Border(left=bd, top=bd, right=bd, bottom=bd)  #设置上下左右边框
    return border


kh_book = Workbook()
kh_sheet = kh_book.active
kh_sheet.title = '外县'
kh_sheet.merge_cells('A1:F1')
kh_sheet['A1'] = '计算机协管员考核表'
kh_sheet['A1'].border = set_border()
kh_sheet['A1'].alignment = Alignment(horizontal='center')
kh_sheet['A2'] = '序号'
kh_sheet['A2'].border = set_border()
kh_sheet['B2'] = '员工编号代码'
kh_sheet['B2'].border = set_border()
kh_sheet['C2'] = '姓名代码'
kh_sheet['C2'].border = set_border()
kh_sheet['D2'] = '所在机构代码'
kh_sheet['D2'].border = set_border()
kh_sheet['E2'] = '所在部门代码'
kh_sheet['E2'].border = set_border()
kh_sheet['F2'] = '激励费'
kh_sheet['F2'].border = set_border()
kh_book.save('report.xlsx')
