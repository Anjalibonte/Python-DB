import pymysql


try:
  ra=int(input('Enter ram: '))
  ro=int(input('Enter rom: '))


  con=pymysql.connect(host='b49hmfubejsxfkfjygig-mysql.services.clever-cloud.com',user='u5wyeas0hrgibtv0',password='ZqMvvmWAwQif0s0b4bB3',database='b49hmfubejsxfkfjygig')
  curs=con.cursor()

  curs.execute("select modelname,price,rating from MOBILES where ram=%d and rom=%d" %(ra,ro))
  data=curs.fetchall()
  print(data)
  
  
  if(data):
    curs.execute("select * from MOBILES")
  else:
    print("not found")
        
except:
    print('invalid input')
    

con.close()

