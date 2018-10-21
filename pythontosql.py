#Activate proxy first

import pymysql

def sequel(command):
    """
    This command takes a sequel command and uses python to connect with our
    SQL database
    """
    connection = pymysql.connect(host='127.0.01',
                                 user='braedyn'
                                 password='harvard2018',
                                 db='driveMAS')

    cursor = connection.cursor()
    return cursor('command')
