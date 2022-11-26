import pymysql


con=pymysql.connect(host='b49hmfubejsxfkfjygig-mysql.services.clever-cloud.com',user='u5wyeas0hrgibtv0',password='ZqMvvmWAwQif0s0b4bB3',database='b49hmfubejsxfkfjygig')
curs=con.cursor()

cm=input('enter company: ')


curs.execute("select proID,modelname,price,rating from MOBILES where company='%s'" %cm)
data=curs.fetchall()
print(data)

if(data):
    curs.execute("select * from MOBILES order by price")
else:
    print("not found")


con.close()