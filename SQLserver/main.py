import pymssql
print ("start:")
conn = pymssql.connect(host='.',user='sa',password='sql',database='Test', charset="GBK")
# conn = pymssql.connect('127.0.0.1','sa','sql','Test')
print ("connected!")

cur=conn.cursor()
cur.execute('select top 5 * from [dbo].[S]')
#如果update/delete/insert记得要conn.commit()#否则数据库事务无法提交
print (cur.fetchall())

cur.close()
conn.close()