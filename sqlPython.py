#Activate proxy first

import pymysql

def sequel(command):
    """
    This command takes a sequel command and uses python to connect with our
    SQL database
    """
    connection = pymysql.connect(host='35.238.205.154',
                                 user='braedyn',
                                 password='harvard2018',
                                 db='driveMAS')

    cursor = connection.cursor()
    cursor.execute(command)
    return cursor.fetchone()

#sequel('CREATE TABLE account (id SERIAL, username varchar(50), password varchar(50), coins float, currCO2 float, currMilage float)')
#sequel('INSERT INTO account (username, password, coins, currCO2, currMilage) VALUES  ("tom", "password123", 1.0, 2.0, 3.0)')
result = sequel('SELECT * FROM account')
print result



