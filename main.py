import time
import sys
import os
import sqlite3
import db.gendb as dg


testid = time.strftime("%Y%m%d%H%M%S", time.localtime())
workd = "./data/"+testid
os.mkdir(workd)
os.mkdir(workd+"/paper")
os.mkdir(workd+"/raw")
print("数据存放目录："+workd)

conn = sqlite3.connect(workd+"/data.db")
c = conn.cursor()
f_stul = input("请输入花名册csv文件路径:")
try:
    with open(f_stul, "r", encoding="gbk") as f:
        n = dg.genStuTab(c, f)
    print("共导入%d人" % n)

except FileNotFoundError:
    print("文件不存在")
else:
    import template
    for n in template.a_sub.keys():## 主观题存放文件夹
        os.mkdir(workd+"/paper/"+n)
    dg.genQuesTab(c, template)
    dg.genAnsTab(c)
    conn.commit()
    print("生成题目数据表成功")

print("请执行python runserver.py %s 来启动web服务器"%workd )