# Coder: Lee
# Time:  2022/11/3 19:12
import os.path
filename = "student.txt"

def main():
    while True:
        menu()
        choice = int(input("请选择: "))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input("你确定要退出系统吗?(y/n)")
                if answer == 'y' or answer == 'Y':
                    print("谢谢你的使用!")
                    break  # 退出系统
                else:
                    continue
            elif choice == 1:
                inputInfo()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                count()
            elif choice == 7:
                show()
        else:
            print("输入有误, 请重新输入: ")

def menu():
    print("===========学生信息管理系统===========")
    print("===============功能菜单==============")
    print("1.录入学生信息")
    print("2.查找学生信息")
    print("3.删除学生信息")
    print("4.修改学生信息")
    print("5.排序")
    print("6.统计学生总人数")
    print("7.显示所有学生信息")
    print("0.退出系统")
    print("===================================")

def inputInfo():
    student_list = []
    while True:
        id = int(input("请输入ID(如1001):"))
        if not id:
            break
        name = input("请输入姓名:")
        if not name:
            break
        try:
            english = int(input("请输入英语成绩:"))
            python = int(input("请输入Python成绩:"))
            java = int(input("请输入Java成绩:"))
        except:
            print("输入无效, 不是整数类型，请重新输入:")
            continue

        student = {'id': id, "name": name, "english": english, "python": python, "java": java}
        student_list.append(student)
        answer = input("是否继续添加?(y/n)")
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break
    save(student_list)
    print("学生信息录入完毕......")

def save(lst):
    try:
        student_file = open(filename, 'a', encoding='utf-8')
    except:
        student_file = open(filename, 'w', encoding='utf-8')

    for item in lst:
        student_file.write(str(item) + '\n')
    student_file.close()

def search():
    while True:
        option = input("查询方式: 1.按ID进行查询 2.按姓名进行查询")
        if option == '1':
            student_id = int(input("请输入要查询的学生ID: "))
        elif option == '2':
            student_name = input("请输入要查询的学生姓名: ")

        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as rfile:
                student_list = rfile.readlines()
        else:
            print("数据库不存在")
            break

        d = {}
        flag = True
        if option == '1':
            for item in student_list:
                d = dict(eval(item))
                if d['id'] == student_id:
                    print(item)
                    flag = False
        elif option == '2':
            for item in student_list:
                d = dict(eval(item))
                if d['name'] == student_name:
                    print(item)
                    flag = False
        if flag:
            print("没有找到该学生")

        answer = input("是否要继续查找?(y/n)")
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break

def delete():
    while True:
        student_id = input("请输入要删除的学生的ID:")
        if not student_id:
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as rfile:
                    student_old = rfile.readlines()
            else:
                student_old = []

            flag = False
            if student_old:
                with open(filename, 'w', encoding='utf-8') as wfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))
                        if d['id'] == student_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f"ID为{student_id}的学生信息已被删除")
                    else:
                        print(f"没有找到ID为{student_id}的学生信息")
            else:
                print("无学生信息")
        show()
        answer = input("是否继续删除?(y/n)")
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break

def modify():
    while True:
        student_id = int(input("请输入要查询的学生ID: "))
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as rfile:
                student_list = rfile.readlines()
        else:
            print("数据库不存在")
            break

        option = input("请选择要修改的项: 1.姓名, 2.英语成绩, 3.Python成绩, 4.Java成绩")
        d = {}
        flag = True
        # student_list_new = []
        with open(filename, 'w', encoding='utf8') as wfile:
            for item in student_list:
                d = dict(eval(item))
                if d['id'] == student_id:
                    print(item)
                    if option == '1':
                        student_name = input("姓名: ")
                        d['name'] = student_name
                    elif option == '2':
                        student_english = int(input("英语成绩: "))
                        d['english'] = student_english
                    elif option == '3':
                        student_python = int(input("Python成绩: "))
                        d['python'] = student_python
                    elif option == '4':
                        student_java = int(input("Java成绩: "))
                        d['java'] = student_java
                    flag = False
                    print("修改后的内容: ", d)
                    wfile.write(str(d) + '\n')
                    # student_list_new.append(d)
                else:
                    # student_list_new.append(d)
                    wfile.write(str(d) + '\n')

        if flag:
            print("没有找到该学生")

        answer = input("是否要继续查找?(y/n)")
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break

def sort():
    option = input("排序方式:1.升序, 2.降序")
    if option == '1':
        descending = False
    else:
        descending = True

    d = {}
    student_list = []
    student_list_new = []
    with open(filename, 'r', encoding='utf-8') as rfile:
        student_list = rfile.readlines()
        for item in student_list:
            d = dict(eval(item))
            student_list_new.append(d)

    option = input("排序项目:1.ID, 2.英语成绩, 3.Python成绩, 4.Java成绩")
    if option == '1':
        student_list_new.sort(key=lambda dItem : dItem['id'], reverse=descending)
    elif option == '2':
        student_list_new.sort(key=lambda dItem : dItem['english'], reverse=descending)
    elif option == '3':
        student_list_new.sort(key=lambda dItem : dItem['python'], reverse=descending)
    elif option == '4':
        student_list_new.sort(key=lambda dItem : dItem['java'], reverse=descending)

    with open(filename, 'w', encoding='utf8') as wfile:
        for item in student_list_new:
            wfile.write(str(item) + '\n')

def count():
    student_list = []
    with open(filename, 'r', encoding='utf8') as rfile:
        student_list = rfile.readlines()
    student_count = len(student_list)
    print(f"总共有{student_count}个学生")

def show():
    with open(filename, 'r', encoding='utf-8') as rfile:
        student_list = rfile.readlines()
    for item in student_list:
        print(item)

if __name__ == "__main__":
    main()
