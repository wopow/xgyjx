import sqlite3
import prettytable as pt
db = sqlite3.connect('itsm.db')
cursor = db.cursor()
sql = 'select transaciton_log.id,personnel_info.name,department.name,\
transaciton_log.job,transaciton_log.overtime,transaciton_log.excess,\
transaciton_log.date,transaciton_log.settle from transaciton_log,\
personnel_info where transaciton_log.person=personnel_info.id \
and transaciton_log.settle <> 1 and department.id=personnel_info.department'

cursor.execute(sql)
userdata = cursor.fetchall()
usertable = pt.PrettyTable()
usertable.field_names = ['流水号', '姓名', '城市', '建单数', '超时数', '超额数', '日期', '是否结账']
userdict = {}
if len(userdata) > 0:
    for user in userdata:
        usertable.add_row(user)
        userdict.setdefault(user[1], []).append(user[0])
        userdict.setdefault(user[1], []).append(user[2])
        userdict.setdefault(user[1], []).append(user[3])
        userdict.setdefault(user[1], []).append(user[4])
        userdict.setdefault(user[1], []).append(user[5])
        userdict.setdefault(user[1], []).append(user[6])
        userdict.setdefault(user[1], []).append(user[7])
else:
    print("语句：" + sql + "有错误！")
print(usertable)
