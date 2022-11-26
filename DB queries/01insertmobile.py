import pymysql

try:
    id=int(input('Enter proID : '))
    mn=input('Enter modelname : ')
    cm=input('enter company : ')
    co=input('enter connectivity : ')
    ram=input('enter ram: ')
    rom=input('enter rom: ')
    col=input('enter color: ')
    scr=input('enter screen: ')
    bat=input('enter battery: ')
    pro=input('enter processor: ')
    pri=int(input('enter price: '))
    rat=float(input('enter rating: ')) 
    
    
    con=pymysql.connect(host='b49hmfubejsxfkfjygig-mysql.services.clever-cloud.com',user='u5wyeas0hrgibtv0',password='ZqMvvmWAwQif0s0b4bB3',database='b49hmfubejsxfkfjygig')
    curs=con.cursor()
    
    curs.execute("insert into MOBILES values(%d,'%s','%s','%s','%s','%s','%s','%s','%s','%s',%d,'%.2f')" %(id,mn,cm,co,ram,rom,col,scr,bat,pro,pri,rat))
    con.commit()
    print('New Mobile Added...')
    con.close()
except: #Exception as e:
    print('cant insert - ')
    

    