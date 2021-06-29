import pymysql


def function_list():
    print(
        """
+-----------------+     
      首页
欢迎来到学生管理系统
1.学生管理
2.教师管理
3.学生分数管理
4.考试分数统计
5.退出系统
+-----------------+
"""
    )


def function_list1():
    print(
        '''

欢迎来到学生管理系统
+-----------------+
1.学生注册
2.开除学生
3.修改学生信息
4.查询学生个人信息
5.返回到首页
+-----------------+
'''
    )


def function_list1_1():
    print(
        """
           注册
+----------------------------+
序号   姓名   年龄   性别    老师
+----------------------------+
        """
    )


def function_list1_2():
    print(
        """
       开除
+---------------+
    姓名  序号  
+---------------+  
        """
    )


def function_list1_3():
    print(
        """
        修改
+--------------------+
原姓名  序号  要修改的姓名
+--------------------+
        """
    )


def function_list1_4():
    print(
        """
  查询
+-----+
  学号
+-----+
        """
    )


def function_list2():
    print(
        '''
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
    )


def function_list2_1():
    print(
        '''
            教师注册
        +------------------------+
        姓名   所教科目   年龄   性别 
        +------------------------+ 
        '''
    )


def function_list_2_2():
    print(
        """
           教师信息修改
        +--------------+
        姓名   修改后的姓名
        +--------------+
        """
    )


def function_list2_34():
    print(
        """
              查询教师信息
        +---------------------+
         姓名  所教学科  年龄 性别
        +---------------------+
        """
    )


def function_list3():
    pass


def pymysql_conn():
    try:
        conn = pymysql.Connect(
            host="192.168.121.145",
            user="root",
            password="682535",
            db="student"
        )
        print("数据库连接成功！")
        cur = conn.cursor()

        return conn
    except pymysql.Error as a:
        print("数据库连接失败！", a)
        return None


def add_stu():


if __name__ == "__main__":
    while True:
        function_list()
        select_1 = input("请输入你的选择： ")
