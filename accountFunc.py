import sqlPython as sqlpy

# Syntax
'''
sqlpy.selectCmd("SELECT * FROM account WHERE password='hackers'")

'''

def createAccount(username, password, carbon):
	sqlCom = 'INSERT INTO account (username, password, coins, currCO2, currMilage) values (%s,%s,%s,%s,%s)'

	cursor = sqlpy.connection.cursor()
	try:
		cursor.execute(sqlCom, (username,password,0.0,0.0,0.0))
	except:
		print 'There was a problem creating an account in database'
		return -1
	cursor.fetchone()
	sqlpy.connection.commit()
	return 0

def getAccountInfoFromID(idNum):
	# We find an account based on the user id
	# If id does not exist, this returns None
	idNum = str(idNum)
	res = sqlpy.selectCmd("SELECT * FROM account WHERE id="+idNum+";")

	return res

def getCoinsById(idNum):
	# We get coins based on ID
	idNum = str(idNum)
	return sqlpy.selectCmd("SELECT coins FROM account WHERE id="+idNum+";")[0]

def updateCoinsById(idNum, coinValue):
	sqlpy.sequel("UPDATE account SET coins="+coinValue+" WHERE id="+idNum+";")

def updateMilageById(idNum, milage):
	sqlpy.sequel("UPDATE account SET currMilage="+milage+" WHERE id="+idNum+";")


def updateCO2ById(idNum, co2):
	# Theoreticly, you should not have to use this function unless you are switching from GV to EV and vice versa
	sqlpy.sequel("UPDATE account SET currCO2="+co2+" WHERE id="+idNum+";")

def updateCoinsById(idNum, coinValue):
	sqlpy.sequel("UPDATE account SET coins="+coinValue+" WHERE id="+idNum+";")

def getGasStatsByState(state):
	res = sqlpy.selectCmd("SELECT * FROM costs WHERE state='"+state+"';")

	return res

