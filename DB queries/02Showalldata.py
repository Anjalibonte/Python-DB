import pymysql

con=pymysql.connect(host='b49hmfubejsxfkfjygig-mysql.services.clever-cloud.com',user='u5wyeas0hrgibtv0',password='ZqMvvmWAwQif0s0b4bB3',database='b49hmfubejsxfkfjygig')
curs=con.cursor()

curs.execute("select * from MOBILES")
data=curs.fetchall()

print(data)
con.close()

