import os

def get_file(file_dir):
for root, dirs, files in os.walk(file_dir):
    print(root) #当前目录路径
    print(dirs) #当前路径下所有子目录
    print(files) #当前路径下所有非目录子文件
    for i in files:
        f = open(root+dirs+i, "r")  # 设置文件对象
        line = f.readline()
        while line:  # 直到读取完文件
            line = f.readline()  # 读取一行文件，包括换行符
            print(line)
        f.close()  # 关闭文件

dic='G:/1/';
get_file(dic)



#读文件

f = open("G:/1/1.txt", "r")  # 设置文件对象

line = f.readline()

line = line[:-1]

while line:  # 直到读取完文件

    line = f.readline()  # 读取一行文件，包括换行符
    print(line)
line = line[:-1]  # 去掉换行符，也可以不去

f.close()  # 关闭文件