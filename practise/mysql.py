#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql;
#初始化参数
dbip = '192.168.114.130'
dbname = 'pydb'
dbuser = 'root'
dbpasswd = 'root'
dbport = 3306
dbcharset = 'utf8'

#创建游标
def createDB():
    conn = pymysql.Connect(host=dbip,user=dbuser,passwd=dbpasswd,port=dbport,charset=dbcharset)
    cursor = conn.cursor()
    #sql = 'create table userinfo(id int not null auto_increment primary key,username varchar(10),passwd varchar(10))engine=innodb default charset=utf8;'
    sql = 'create database pydb default charset=utf8'
    cursor.execute(sql)
    conn.close()
#createDB()

def createTable():
    conn = pymysql.Connect(host=dbip,user=dbuser,passwd=dbpasswd,db=dbname,port=dbport,charset=dbcharset)
    cursor = conn.cursor()
    sql = 'create table userinfo(id int not null auto_increment primary key,username varchar(10),passwd varchar(10))engine=innodb default charset=utf8;'
    #sql = 'create database pydb default charset=utf8'
    cursor.execute(sql)
    conn.close()
#createTable()

def insertTable():
    conn = pymysql.Connect(host=dbip,user=dbuser,passwd=dbpasswd,db=dbname,port=dbport,charset=dbcharset)
    cursor = conn.cursor()
    sql = "insert into userinfo(username,passwd) values('frank','123'),('rose','321'),('jeff',666);"
    cursor.execute(sql)
    conn.close()
insertTable()




#连接数据库
# db = pymysql.connect("localhost","root","LBLB1212@@","dbforpymysql")
#
# #使用cursor()方法创建一个游标对象
# cursor = db.cursor()
#
# #使用execute()方法执行SQL语句
# cursor.execute("SELECT * FROM userinfo")
#
# #使用fetall()获取全部数据
# data = cursor.fetchall()
#
# #打印获取到的数据
# print(data)
#
# #关闭游标和数据库的连接
# cursor.close()
# db.close()
