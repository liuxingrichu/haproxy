#!/urs/bin/env python
# -*- coding:utf-8 -*-

head = []
body = []


#数据备份
def save_data():
    with open("haproxy.txt", "r", encoding="utf-8") as f1,\
        open("haproxy.txt.bak", "w", encoding="utf-8") as f2:
        for line in f1:
            f2.write(line)

 #数据处理
def data_handle(request):
    request = eval(request)
    for k, v in request.items():
        if isinstance(v, str):
            head.append(k)
            head.append(v)
        else:
            for key, value in request[k].items():
                body.append(key)
                body.append(str(value))


#删除
def delete(request):
    data_handle(request)
    save_data()
    find_strings = " ".join(head)
    count = 0
    with open("haproxy.txt.bak", "r", encoding="utf-8") as f1,\
            open("haproxy.txt", "w", encoding="utf-8") as f2:
        for line in f1:
            if find_strings in line:
                count = 3

            if not count:
                f2.write(line)
            else:
                count -= 1


#添加
def add(request):
    data_handle(request)
    save_data()
    with open("haproxy.txt", "a+", encoding="utf-8") as f1:
        f1.write("\n")
        f1.write(" ".join(head))
        f1.write("\n")
        f1.write("\t\t")
        f1.write(" ".join(body))


#修改
def update(request):
    data_handle(request)
    save_data()
    find_strings = " ".join(head)
    count = 0
    with open("haproxy.txt.bak", "r", encoding="utf-8") as f1,\
            open("haproxy.txt", "w+", encoding="utf-8") as f2:
        for line in f1:
            if find_strings in line:
                f2.write(" ".join(head))
                f2.write("\n")
                f2.write("\t\t")
                f2.write(" ".join(body))
                count = 2

            if not count:
                f2.write(line)
            else:
                count -= 1


#数据查询
def query(request):
    show_flag = False

    with open("haproxy.txt", "r", encoding="utf-8") as f:
        for line in f:
            if request in line:
                show_flag = True
                continue
            if show_flag:
                print(line.strip("\n"))
            if not line.strip():
                show_flag = False


info = """
------ 操作模式 --------
    1   查询记录
    2   添加记录
    3   删除记录
    4   更新记录
-----------------------
"""

def main():
    while True:
        print(info)
        choose = input(">>")
        if choose.isdigit():
            choose = int(choose)
            if choose > 4 and choose < 1:
                print("\033[0;31m请输入正确选项！\033[0m")
                continue
            else:
                if choose == 1:
                    text = input("请输入查询内容：")
                    query(text)
                elif choose == 2:
                    text = input("请输入添加内容：")
                    add(text)
                    for i in range(len(head)):
                        head.pop()
                    for i in range(len(body)):
                        body.pop()
                    print("\t你好，已完成添加操作。")
                elif choose == 3:
                    text = input("请输入删除内容：")
                    delete(text)
                    for i in range(len(head)):
                        head.pop()
                    for i in range(len(body)):
                        body.pop()
                    print("\t你好，已完成删除操作。")
                else:
                    text = input("请输入更新内容：")
                    update(text)
                    for i in range(len(head)):
                        head.pop()
                    for i in range(len(body)):
                        body.pop()
                    print("\t你好，已完成更新操作。")
        else:
            if choose == 'q':
                break
            else:
                print("\033[0;31m请输入正确选项！\033[0m")
                continue


if __name__ == '__main__':
    main()