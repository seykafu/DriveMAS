#Activate proxy first

import pymysql



connection = pymysql.connect(host='35.238.205.154',user='braedyn',password='harvard2018',db='driveMAS')


def sequel(command):
    """
    This command takes a sequel command and uses python to connect with our
    SQL database
    """
    cursor = connection.cursor()
    cursor.execute(command)
    return cursor.fetchone()


#print sequel('USE driveMAS;')
#print sequel(' driveMAS;')
#sequel('CREATE TABLE accountTest (id SERIAL, username varchar(50), password varchar(50), coins float, currCO2 float, currMilage float)')
#print sequel('INSERT INTO accountTest (username, password, coins, currCO2, currMilage) values (%s,%s,%s,%s,%s), ("tom2", "password123", 1.0, 2.0, 3.0);')
#print sequel('INSERT INTO account (username, password, coins, currCO2, currMilage) values  ("tom", "password123", 1.0, 2.0, 3.0);')
#print sequel('INSERT INTO account (username, password, coins, currCO2, currMilage) values  ("tom", "password123", 1.0, 2.0, 3.0);')


sqlCom = 'INSERT INTO accountTest (username, password, coins, currCO2, currMilage) values (%s,%s,%s,%s,%s)'

cursor = connection.cursor()
print cursor.execute(sqlCom, ("tom","password000",1.0,2.0,3.0))
print cursor.fetchone()
connection.commit()


print sequel('SELECT * FROM accountTest')



