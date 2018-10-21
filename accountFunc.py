import sqlPython as sqlpy

def createAccount(username, password):
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


createAccount('Dr. Evil', 'hackers')
sqlpy.selectCmd("SELECT * FROM account WHERE password='hackers'")
