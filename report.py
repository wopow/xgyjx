from openpyxl import load_workbook
from openpyxl.styles import Border, Side


def set_border():
    bd = Side(style='thin', color="000000")#设置单元格边框为细线，颜色为黑色
    border = Border(left=bd, top=bd, right=bd, bottom=bd)#设置上下左右边框
    return border


wb = load_workbook('report.xlsx')
#wb['Sheet1'].title='xgy'
ws = wb['xgy']
print(ws['A1'].value)
ws.insert_rows(6)
ws['C6'].border = set_border()
wb.save('report.xlsx')
