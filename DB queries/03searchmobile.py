import pymysql


con=pymysql.connect(host='b49hmfubejsxfkfjygig-mysql.services.clever-cloud.com',user='u5wyeas0hrgibtv0',password='ZqMvvmWAwQif0s0b4bB3',database='b49hmfubejsxfkfjygig')
curs=con.cursor()

mn=input(' enter modelname: ')




curs.execute("select proID,company,connectivity,ram,rom,color,screen,battery,processor,price,rating from MOBILES where modelname='%s'" %mn)
data=curs.fetchone()
print(data)

if(data):
    curs.execute("select * from MOBILES")
else:
    print("not found")


con.close()
