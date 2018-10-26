import xlrd
import os
import sqlite3
import datetime
import prettytable as pt

def checktime(t1,t2,lan):
    try :
        d1=datetime.datetime.strptime(t1,"%Y-%m-%d %H:%M:%S")
        d2=datetime.datetime.strptime(t2,"%Y-%m-%d %H:%M:%S")
    except ValueError as e:
        d2 = d1
    if lan == "企业网维护":
        if (d2-d1).days >1:
            return 1
        else:
            return 0
    else :
        if (d2-d1).seconds > 7200:
            return 1
        else:
            return 0

db = sqlite3.connect('d:\itsm\itsm.db')
cursor = db.cursor()
sql = 'select name,city,id from personnel_info where register <> 0'
cursor.execute(sql)
users = cursor.fetchall()
userdict = {}
userdata = cursor.fetchall()
usertable = pt.PrettyTable()
usertable.field_names = ['姓名','城市','建单数','超时数','超额数']
if  len(users) >0:
    for user in users:
        userdict.setdefault(user[0],[]).append(user[1])
        userdict.setdefault(user[0],[]).append(0)
        userdict.setdefault(user[0],[]).append(0)
        userdict.setdefault(user[0],[]).append(0)
        userdict.setdefault(user[0],[]).append(user[2])

else:
    print("语句：",sql,"有错误！")
filename = os.listdir('d:\\itsm\\xls')
xlsfile = []
for i in filename:
    j=i[i.rfind('.'):]
    if j == '.xls':
         xlsfile.append(i)

exceldate = '2018-05'
for x in xlsfile:
#读取命令行中的路径，并打开文件
    data=xlrd.open_workbook("d:\\itsm\\xls\\" + x)
#选择工作簿
    table=data.sheets()[0]
#选择数据列
    name=table.col_values(2)
    begintime=table.col_values(6)
    exceldate = begintime[2][0:7]
    endtime=table.col_values(7)
    lan=table.col_values(24)
    for i in range(1,table.nrows):
        if name[i] in userdict:
            userdict[name[i]][1]=userdict.get(name[i])[1]+1
            time=checktime(begintime[i],endtime[i],lan[i])
            userdict[name[i]][2]=userdict.get(name[i])[2]+time
        else:
            print("用户%s不在协管员名单中" %name[i])
for i in userdict:
    if userdict[i][0] == '延吉':
        if userdict[i][1] - 10 > 0:
            userdict[i][3] = userdict[i][1] - 10
        else:
            userdict[i][3] = 0
    else:
        if userdict[i][1] - 15 > 0:
            userdict[i][3] = userdict[i][1] - 15
        else:
            userdict[i][3] = 0
    usertable.add_row([i,userdict[i][0],userdict[i][1],userdict[i][2],userdict[i][3]])
sql = "select * from transaciton_log where strftime('%%Y%%m',transaciton_log.date)='%s'" %(exceldate[0:4] + exceldate[-2:])
cursor.execute(sql)
sqldata = cursor.fetchall()
if len(sqldata) == 0:
    for data in userdict:
        sql = 'insert into transaciton_log values (null,%s,%s,%s,%s,"%s",%s)' %(userdict[data][4],userdict[data][1],userdict[data][2],userdict[data][3],exceldate + '-01',0)
        cursor.execute(sql)
else:
    
    for data in userdict:
        sql = 'update transaciton_log set job=%d,overtime=%d,excess=%d where person=%d' %(userdict[data][1],userdict[data][2],userdict[data][3],userdict[data][4])

        cursor.execute(sql)
db.commit()
cursor.close()
print(usertable)
