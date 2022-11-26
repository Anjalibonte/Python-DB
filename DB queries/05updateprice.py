import pymysql


pd=int(input('Enter proID : '))
np=int(input('Enter new price : '))
    
con=pymysql.connect(host='b49hmfubejsxfkfjygig-mysql.services.clever-cloud.com',user='u5wyeas0hrgibtv0',password='ZqMvvmWAwQif0s0b4bB3',database='b49hmfubejsxfkfjygig')
curs=con.cursor()
    
curs.execute("select * from MOBILES where proID=%d" %pd)
data=curs.fetchone()
    
if data:
    curs.execute("update MOBILES set price=%d where proID=%d" %(np,pd))
    con.commit()
    print('price updated...')
else:
    print('mobile does not exist')
        
con.close()
