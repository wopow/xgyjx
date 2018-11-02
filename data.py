import sqlite3
from prettytable import PrettyTable


def db_conn():
    conn = sqlite3.connect('d:\itsm\itsm.db')
    return conn


def db_cursor():
    conn = db_conn()
    cursor = conn.cursor()
    return cursor


def query(sql):
    querycursor = db_cursor()
    querycursor.execute(sql)
    values = querycursor.fetchall()
    querycursor.close()
    return values


def db_update(register):
    conn = db_conn()
    updatecursor = conn.cursor()
    print_depa()
    name = input("请输入协管员姓名：")
    city = input("请输入协管员所在城市：")
    sql = 'update personnel_info set register = ' + register + ' where name = "' + name + '" and city="' + city + '"'
    updatecursor.execute(sql)
    conn.commit()
    user_info = query(
        "select * from personnel_info where name='%s' and city='%s'" % (name,
                                                                        city))
    if user_info:
        i = 0
        print_info()
        for person in user_info:
            reg_cn = ''
            if person[3] == 1:
                reg_cn = '在岗'
            elif person[3] == 0:
                reg_cn = '离岗'
        i += 1
        print("%d\t%d\t%s\t%s\t%s" % (i, person[0], person[1], person[2],
                                      reg_cn))
    else:
        print("协管员信息有误！")
    updatecursor.close()


def print_info(data, job):
    table = PrettyTable(["编号", "序号", "姓名", "单位", "是否在岗"])
    i = 0
    for person in data:
        i += 1
        table.add_row([i, person[0], person[1], person[2], job])
    print(table)


def print_depa():
    data = query("select * from department;")
    table = PrettyTable(["序号", "部门名称", "机构代码", "所在城市"])
    i = 0
    for person in data:
        i += 1
        table.add_row([person[0], person[1], person[2], person[3]])
    print(table)


print("请选择所需功能：")
print("                1  增加新协管员")
print("                2  调离协管员")
print("                3  协管员归来")
print("                4  查询在岗协管员")
print("                5  查询不在岗协管员")
num = input("您想要进行哪个功能：")
if num == "1":
    conn = db_conn()
    addcursor = conn.cursor()
    print_depa()
    name = input("请输入协管员姓名：")
    city = input("请输入协管员所在城市：")
    person_code=input("请输入协管员员工编号：")
    sql = "INSERT INTO personnel_info VALUES (null,'" + name + "','1',"+ city + ",'"+ person_code +"')"
    addcursor.execute(sql)
    conn.commit()
    addcursor.close()
elif num == "2":
    db_update("0")
elif num == "3":
    db_update("1")
elif num == "4":
    data = query("select * from  onthejob;")
    print_info(data, "在岗")
elif num == "5":
    data = query("select * from absences;")
    print_info(data, "离岗")
