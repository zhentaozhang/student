import pymysql

list_shouye = '''
+-----------------+     
      首页
欢迎来到学生管理系统
1.学生管理
2.教师管理
3.学生分数管理
4.退出系统
+-----------------+
'''
list_1 = '''

欢迎来到学生管理系统
+-----------------+
1.学生注册
2.开除学生
3.修改学生信息
4.查询学生个人信息
5.返回到首页
+-----------------+
'''

list_2 = '''
+-----------------+
欢迎来到教师管理系统
+-----------------+
1.新教师注册
2.修改教师信息
3.查询教师信息
4.删除教师信息
5.返回到首页
+-----------------+
'''

list_3 = '''
+-----------------+
欢迎来到学生分数管理
+-----------------+
1.期中考试
2.期末考试
3.返回首页
+-----------------+
'''


def pymysql_conn(host, user, password, db):
    try:
        conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db,
        )
        return conn
    except pymysql.Error as a:
        print("数据库连接失败！", a)
        return None


def pymysql_query(query):
    conn = pymysql_conn(
        "192.168.121.145",
        "root",
        "682535",
        "student"
    )
    cur = conn.cursor()
    try:
        aff_rows = cur.execute(query)
        print(aff_rows)
        conn.commit()
    except:
        conn.rollback()
    conn.close()
    cur.close()


def pymysql_select(id):  # 查询学生信息
    conn = pymysql_conn(
        "192.168.121.145",
        "root",
        "682535",
        "student"
    )
    cur = conn.cursor()
    try:
        cur.execute("SELECT name,age,sex,who_teacher  FROM stu WHERE id='{}'".format(id))
        myresult = cur.fetchall()
        for i in myresult:
            print(id, "的信息为：", i)
        conn.commit()
        return myresult
    except:
        conn.rollback()
    conn.close()
    cur.close()


def pymysql_select_1(id):  # 查询教师信息
    conn = pymysql_conn(
        "192.168.121.145",
        "root",
        "682535",
        "student"
    )
    cur = conn.cursor()
    try:
        cur.execute("SELECT name,age,sex,sub FROM tea WHERE id='{}'"
                    .format(id))
        myresult = cur.fetchall()
        print(myresult)
        conn.commit()
        return myresult
    except:
        conn.rollback()
    conn.close()
    cur.close()


def delete_stu(name):
    conn = pymysql_conn(
        "192.168.121.145",
        "root",
        "682535",
        "student"
    )
    cur = conn.cursor()
    try:
        cur.execute("DELETE  FROM stu WHERE name='{}'".format(name))
        print("{}已被开除".format(name))
        cur.execute("ALTER TABLE stu DROP COLUMN id")
        cur.execute("ALTER TABLE stu ADD COLUMN id int PRIMARY KEY AUTO_INCREMENT first ")
        conn.commit()
    except:
        conn.rollback()
    conn.close()
    cur.close()


def delete_tea(name):
    conn = pymysql_conn(
        "192.168.121.145",
        "root",
        "682535",
        "student"
    )
    cur = conn.cursor()
    try:
        cur.execute("DELETE  FROM tea WHERE name='{}'".format(name))
        print("{}已被删除".format(name))
        cur.execute("ALTER TABLE tea DROP COLUMN id")
        cur.execute("ALTER TABLE tea ADD COLUMN id int PRIMARY KEY AUTO_INCREMENT first ")
        conn.commit()
    except:
        conn.rollback()
    conn.close()
    cur.close()


def gra(name):
    conn = pymysql_conn(
        "192.168.121.145",
        "root",
        "682535",
        "student"
    )
    cur = conn.cursor()
    try:
        cur.execute("SELECT "
                    "stu.name,gra.chinese,gra.math,gra.English "
                    "FROM stu "
                    "INNER JOIN gra ON stu.id=gra.id AND stu.name ='{}'".format(name))
        myresult = cur.fetchall()
        print("姓名| 语文| 数学| 英语\n")
        for i in myresult:
            print(i)
        conn.commit()
        return myresult
    except:
        conn.rollback()
    conn.close()
    cur.close()


if __name__ == "__main__":
    while True:
        print(list_shouye)
        select = input("请输入你的选择: ")
        if select == "1":
            while True:
                print(list_1)
                select = input("请输入你的选择: ")
                if select == "1":
                    name = input("请输入该学生的名字: ")
                    age = int(input("请输入该学生年龄: "))
                    sex = input("请输入该学生性别: ")
                    who_teacher = input("输入该学生班主任姓名: ")
                    query = '''INSERT INTO stu  \
                               (name,age,sex,who_teacher)  \
                               VALUES \
                               ('{0}','{1}','{2}','{3}')''' \
                        .format(name, age, sex, who_teacher)
                    pymysql_query(query)
                    print("{}同学注册完成".format(name))

                elif select == "2":
                    name = input("输入要开除学生的姓名: ")
                    delete_stu(name)
                elif select == "3":
                    id_1 = input("请输入要修改学生的id: ")
                    name = input("修改为: ")
                    query = "UPDATE stu SET name='{0}' WHERE id='{1}'" \
                        .format(name, id_1)
                    print("序号为{}的学生姓名修改为{}".format(id_1, name))
                    pymysql_query(query)

                elif select == "4":
                    id = int(input("请输入要查询学生的id: "))
                    pymysql_select(id)

                elif select == "5":
                    pass
                break
        elif select == "2":
            while True:
                print(list_2)
                select = input("请输入你的选择: ")
                if select == "1":
                    name = input("请输入新教师的姓名：")
                    age = int(input("请输入新教师的年龄："))
                    sex = input("请输入新教师的性别：")
                    sub = input("请输入新教师所教科目：")
                    query = '''INSERT INTO tea (name,age,sex,sub) 
                    VALUES ('{}','{}','{}','{}')''' \
                        .format(name, age, sex, sub)
                    pymysql_query(query)
                    print("{}老师的信息注册完成".format(name))
                elif select == "2":
                    id = input("请输入要修改老师的id: ")
                    name = input("修改为: ")
                    query = "UPDATE stu SET name ='{}' WHERE id='{}'" \
                        .format(name, id)
                    print("序号为{}的学生姓名修改为{}".format(id, name))
                    pymysql_query(query)
                elif select == "3":
                    id = int(input("请输入要查询教师的id: "))
                    pymysql_select_1(id)
                elif select == "4":
                    name = input("输入要删除教师的姓名: ")
                    delete_tea(name)
                elif select == "5":
                    pass
                break
        elif select == "3":
            while True:
                print(list_3)
                select = input("请输入你的选择: ")
                if select == "1":
                    name = input("请输入姓名: ")
                    gra(name)
                elif select == "2":
                    print("未到期末时期，不可访问！")

        elif select == "4":
            break
        else:
            print("输入格式有误，请输入阿拉伯数字！")
