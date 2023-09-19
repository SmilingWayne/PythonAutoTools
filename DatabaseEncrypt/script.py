import sqleet
import os
import sqlite3


if __name__ == "__main__":
    db_name = "./Contents/YOURDATABSENAME.db"

    # key = b"Key"
    # # Try to open db with the wrong key, this fails
    # try:
    #     con = sqleet.connect(db_name, key="123456")
    # except sqleet.AuthenticationError:
    #     print("Failed to open database")

    # ===================


    CONN = sqlite3.connect('./Contents/YOURSRCDB.db')
    cursor = CONN.cursor()
    execute_sentence = "select * from tablex"
    temp = cursor.execute(execute_sentence).fetchall()
    cursor.close()
    CONN.close()

    # print(temp)

    # Remove the encryption on the created database
    # con = sqleet.connect(db_name, key=key)
    # con.change_key(None)
    # con.close()
    # # Create a new encrypted db
    con = sqleet.connect(db_name, key="YOURKEY")


    # # con.execute("create table test(col char);")
    # # cursor = conn.cursor()
    con.execute('''
        create table tablex(
            createTime integer,
            Des integer,
            ImgStatus integer,
            MesLocalID integer,
            Message text,
            MesSvrID integer,
            Status integer,
            TableVar integer,
            Type integer
        )
    ''')
    # con.commit()
    # con.close()

    # con = sqleet.connect(db_name, key="123456")
    # data = [
    #     (2, 'lily', 19),
    #     (3, 'mike', 20)
    # ]
    sql = 'insert into tablex values (?, ?, ?, ?, ? ,?, ?, ?, ?)'
    con.executemany(sql, temp)
    con.commit()
    # cursor.close()

    con.close()

    # ==============
    # con = sqleet.connect(db_name, key="XXgqdl41h5900490")

    # t = con.execute("select createTime from chathistory")
    # # print(t)
    # for i in t:
    #     print(i)

    # con.close()
