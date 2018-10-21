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


def selectCmd(command):
    """
    This command takes a sequel command and uses python to connect with our
    SQL database
    """
    cursor = connection.cursor()
    cursor.execute(command)
    res =  cursor.fetchone()
    return res

def createAccountTable():
	try:
		sequel('CREATE TABLE account (id SERIAL, username varchar(50), password varchar(50), coins float, currCO2 float, currMilage float);')
	except (RuntimeError):
		print 'Failure to create account table'



