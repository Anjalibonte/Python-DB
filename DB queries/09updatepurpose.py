import pymysql
try:
    mn=input("Enter Model Name: ")
    pur=input("Enter purpose: ")
    con=pymysql.connect(host='b49hmfubejsxfkfjygig-mysql.services.clever-cloud.com',user='u5wyeas0hrgibtv0',password='ZqMvvmWAwQif0s0b4bB3',database='b49hmfubejsxfkfjygig')
    curs=con.cursor()

    curs.execute("update MOBILES set modelname='%s' where purpose='%s'"%(mn,pur))
    data=curs.fetchall()
    con.commit()
    con.close()
    print("updated succesfully")
except:
    print("Enter valid input: ")