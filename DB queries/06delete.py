import pymysql

try: 
    pid=int(input('Enter proID to delete : '))
    
    con=pymysql.connect(host='b49hmfubejsxfkfjygig-mysql.services.clever-cloud.com',user='u5wyeas0hrgibtv0',password='ZqMvvmWAwQif0s0b4bB3',database='b49hmfubejsxfkfjygig')
    curs=con.cursor()
    
    curs.execute("select * from MOBILES where proID=%d" %pid)
    data=curs.fetchone()
    
    if data:
        print(data)
        product=input('Do you want to delete? (yes/no) : ')
        if product.lower()=='yes':
            curs.execute("delete from MOBILES where proID=%d" %pid)
            con.commit()
            print('data deleted')
        else:
            print('delete operation cancelled')
    else:
        print('proID does not exist')
    
    con.close()

except:
    print('failed')
    
    