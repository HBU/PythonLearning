#测试连接SQLserver数据库

import pymssql

print ("start:")
conn = pymssql.connect(host='.',user='sa',password='sql',database='Test', charset="GBK")
print ("connected!")

cur=conn.cursor()
cur.execute('select * from C')

#如果update/delete/insert记得要conn.commit()，否则数据库事务无法提交

print (cur.fetchall())

cur.close()
conn.close()