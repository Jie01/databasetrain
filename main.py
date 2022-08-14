import sqlite3

conn = sqlite3.connect('test.db')

print ("数据库打开成功")
c = conn.cursor()
tablename = "ETHUSDT1h_EMACROSS"
keys = ["ID",
"SIDE",
"BUYINTIME",
"BUYINPRICE",
"TAKEPROFIT",
"STOPLOSS",
"SELLTIME",
"SELLPRICE",
]
# c.execute(f'''CREATE TABLE {tablename}
#        ({keys[0]} INT PRIMARY KEY     NOT NULL,
#        {keys[1]}     TEXT    NOT NULL,
#        {keys[2]}     TEXT    NOT NULL,
#        {keys[3]}     REAL    NOT NULL,
#        {keys[4]}     REAL    NOT NULL,
#        {keys[5]}     REAL    NOT NULL,
#        {keys[6]}     TEXT    NOT NULL,
#        {keys[7]}     REAL    NOT NULL);''')
# print ("数据表创建成功")
# conn.commit()
# conn.close()

# 訂單id, 訂單方向(買入/沽出), 買入時間, 買入價格, 止賺價格, 止蝕價格, 賣出時間(default 0), 賣出價格(default 0)

# c.execute(f"INSERT INTO {tablename} {tuple(keys)} \
#       VALUES (1, 'BUY', '2020-06-03 17:58:58', 20000.00 , {20000*1.2} , {20000 * 0.8}, '0', 0)")

# c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")

# c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")

# c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")

conn.commit()
# print ("数据插入成功")
# conn.close()

# c.execute(f"UPDATE {tablename} set {keys[6]}='2022-06-03 18:23:44',{keys[7]}=16000 where {keys[6]}='0'")
# conn.commit()
# print("Total number of rows updated :", conn.total_changes)



# cursor = c.execute(f"SELECT {keys[0]}, {keys[1]}, {keys[2]}, {keys[3]}, {keys[4]}, {keys[5]}, {keys[6]}, {keys[7]}  from {tablename}")
cursor = c.execute(f"SELECT *  from {tablename} WHERE {keys[6]}='0'").fetchall()
print(cursor)
for row in cursor:
#    print("ID = ", row[0])
#    print("NAME = ", row[1])
#    print("ADDRESS = ", row[2])
#    print("SALARY = ", row[3], "\n")
    print(row , "\n")


print ("数据操作成功")
conn.close()


