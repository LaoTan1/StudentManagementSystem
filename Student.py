# -*- coding:utf-8 -*-
import os


# 定义学生类
class Student(object):
    # 类似java的构造器
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    # 相当于java的toString()方法
    def __str__(self):
        # msg = "{'id':" + "'"+self.id +"'"+ ",'name':" + "'" +self.name + "'" + ",'age':" + "'" + self.age+"'}"
        msg = "学生信息：id=" + self.id + ",name=" + self.name + ",age=" + self.age
        return msg

    # 获取id
    def getId(self):
        return self.id

    # 获取name
    def getName(self):
        return self.name

    # 获取age
    def getAge(self):
        return self.age

    # 设置name
    def setName(self, name):
        self.name = name

    # 设置age
    def setAge(self, age):
        self.age = age


# 定义添加学生信息的类
class StuD(object):
    def __init__(self, array):
        self.array = array

    def addStu(self):
        "添加学生信息"
        id = input("请输入学生学号：")
        for i in range(len(self.array)):
            stu2 = self.array[i]
            if id == stu2.getId():
                print("该学号已存在，不能重复添加")
                return
        name = input("请输入学生姓名：")
        age = input("请输入学生年龄：")
        stu = Student(id, name, age)
        self.array.append(stu)  # 把单个学生添加到总列表中
        print("添加成功:", stu)

    # 删除学生信息
    def delStu(self):
        "删除学生信息"
        id = input("请输入要删除的学生学号：")
        for i in range(len(self.array)):
            stu2 = self.array[i]
            if id == stu2.getId():
                del self.array[i]
                return 0
        return 1

    # 修改学生信息
    def updateStu(self):
        "修改学生信息"
        id = input("请输入要修改的学生学号：")
        for i in range(len(self.array)):
            stu2 = self.array[i]
            if id == stu2.getId():
                name = input("请输入要修改的学生姓名：")
                age = input("请输入要修改的学生年龄：")
                stu2.setName(name)
                stu2.setAge(age)
                print("修改成功")
                return
        print("找不到该学号，没法修改")

    # 查询学生信息
    def selectStu(self):
        "查询学生信息"
        id = input("请输入要查询的学生学号：")
        for i in range(len(self.array)):
            stu2 = self.array[i]
            if id == stu2.getId():
                print("查询到的学生信息：", stu2)
                return
        print("查询失败，查不到该学生信息")
        return

    # 打印学生信息
    def printStuInfo(self):
        for i in range(len(self.array)):
            stu = self.array[i]
            print(stu)


def main():
    print("==" * 30)
    print("欢迎使用学生管理系统")
    print("1.添加学生信息")
    print("2.删除学生信息")
    print("3.修改学生信息")
    print("4.查询学生信息")
    print("5.退出系统")
    print("==" * 30)
    flag = 0
    array = []  # 定义list用于保存学生信息
    filename = 'write_data.txt'  # 文件名
    if not os.path.exists(filename):  # 判断文件是否存在
        file = open(filename, 'w')  # 不存在就创建文件
        file.close()
    f = open(filename, "r")
    content = f.readlines()
    print("文件内容：", content)
    array.extend(content)
    array_temp = []  # 临时变量
    for i in range(len(array)):  # 遍历转成学生对象
        print("第" + str(i) + "行:", array[i])
        if isinstance(array[i], str):  # 判断是否为字符串
            strArray = str(array[i]).split(",")
            id = strArray[0]
            name = strArray[1]
            age = strArray[2].replace("\n", "")
            student = Student(id, name, age)  # 创建学生对象
            array_temp.append(student)
    del array
    array = array_temp
    A = StuD(array)
    while flag != 1:
        try:
            step = input("请输入你的操作：")
            step = int(step)
            if step == 1:
                A.addStu()
                # print("学生信息打印：", array)

            elif step == 2:
                num = A.delStu()
                if num == 0:
                    print("删除成功")
                elif num == 1 or num == 2:
                    print("删除失败")
                A.printStuInfo()
            elif step == 3:
                A.updateStu()
                A.printStuInfo()
            elif step == 4:
                A.selectStu()
            elif step == 5:
                flag = 1
                with open(filename, 'w') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
                    for i in range(len(array)):
                        if i == len(array) - 1:
                            stu = array[i]
                            f.write(stu.getId() + "," + stu.getName() + "," + stu.getAge())
                        else:
                            stu = array[i]
                            f.write(stu.getId() + "," + stu.getName() + "," + stu.getAge() + "\n")
                        f.close()
            else:
                print("输入指令错误，请重新输入！！")
        except:
            print("输入指令错误，请重新输入！！")
    print("退出系统成功")


main()
