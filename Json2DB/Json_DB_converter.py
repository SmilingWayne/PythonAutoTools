

import sqlite3
import os
import json


class DbOperate(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(DbOperate, cls).__new__(cls)
        return cls._instance

    def __init__(self, db_name):
        self.db_name = db_name
        self.connect = sqlite3.connect(self.db_name)
        self.cursor = self.connect.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connect.close()

    def execute_sql(self, sql):
        try:
            self.cursor.execute(sql)
            self.connect.commit()
        except Exception as e:
            self.connect.rollback()

    def executemany_sql(self, sql, data_list):
        # example:
        # sql = 'insert into filelist (pkgKey, dirname, filenames, filetypes) values (?, ?, ?, ?);'
        # data_list = [(1, '/etc/sysconfig', 'openshift_option', 'f'), (1, '/usr/share/doc', 'adb-utils-1.6', 'd')]
        try:
            self.cursor.executemany(sql, data_list)
            self.connect.commit()
        except Exception as e:
            self.connect.rollback()
            raise Exception("executemany failed")

#     # 如果db文件不存在则创建


if __name__ == "__main__":

    DB_PATH = ""
    JSON_PATH = ""

    if not os.path.exists(DB_PATH):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('''CREATE TABLE CHATHISTORY(
                CREATETIME     Int DEFAULT 0,
                Des            Int ,
                ImgStatus      Int DEFAULT 0,
                MesLocalID     Int,
                Message        text,
                MesSvrID       Int DEFAULT 0,
                Status         Int DEFAULT 0,
                TableVer       Int DEFAULT 1,
                Type           Int);''')
        conn.commit()
        conn.close()
#     # # 连接数据库，没有会自动创建文件，数据结构还是要上面定义
#     conn = sqlite3.connect("./static/files/20230327.db")
#     c = conn.cursor()
#     # 首先删除表中所有数据

#     # t1 = time.clock()
#     sql = 'insert into CHATHISTORY (CREATETIME, Des, ImgStatus, MesLocalID, Message, MesSvrID, Status,TableVer, Type) values (?, ?, ?, ?, ?, ?, ?, ?, ?);'
#     data_list = [(1, '/etc/sysconfig', 'openshift_option', 'f'), (1, '/usr/share/doc', 'adb-utils-1.6', 'd')]
#     db.executemany_sql(sql, data_list)
#     t2 = time.clock()
#     print('insert data into filelist cost %s seconds' % (t2 - t1))
#     print('success insert data into filelist with %s' % sqlite_path)

#     # 添加数据
#     for idx, i in enumerate(contents):
#         # print(f'insert into INFO CHATHISTORY({i["CreateTime"]},{i["Des"]},{i["ImgStatus"]},{i["MesLocalID"]},{i["Message"]},{i["MesSvrID"]},{i["Status"]},{i["TableVer"]},{i["Type"]});')
#         c.execute(
#             f'insert into CHATHISTORY VALUES({i["CreateTime"]},{i["Des"]},{i["ImgStatus"]},{i["MesLocalID"]},{escape_string(i["Message"])},{i["MesSvrID"]},{i["Status"]},{i["TableVer"]},{i["Type"]});')
#         print(idx)

#     conn.commit()
#     conn.close()
#     # print(contents[:10])
#     # print((contents[0]))

#     print("Done!")

    contents = None
    ipt = []
    with open(JSON_PATH) as f:
        contents = json.load(f)

    for content in contents:
        ipt.append((content["CreateTime"], content["Des"], content["ImgStatus"], content["MesLocalID"],
                   content["Message"], content["MesSvrID"], content["Status"], content["TableVer"], content["Type"]))

    with DbOperate(DB_PATH) as db:
        # t1 = time.clock()
        # sql = 'insert into filelist (pkgKey, dirname, filenames, filetypes) values (?, ?, ?, ?);'
        sql = 'insert into CHATHISTORY (CREATETIME, Des, ImgStatus, MesLocalID, Message, MesSvrID, Status,TableVer, Type) values (?, ?, ?, ?, ?, ?, ?, ?, ?);'
        # data_list = [(1, '/etc/sysconfig', 'openshift_option', 'f'), (1, '/usr/share/doc', 'adb-utils-1.6', 'd')]
        db.executemany_sql(sql, ipt)
        # t2 = time.clock()
        # print('insert data into filelist cost %s seconds' % (t2 - t1))
        print('success insert data into filelist with %s' % DB_PATH)
