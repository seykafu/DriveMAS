import pymssql

tableName = ""
server = ""
username = ""
password = ""
database = ""

conn = pymssql.connect(server=server, user=user, password=password, database=db)
cursor = conn.cursor()

query = "SELECT * FROM " + tableName
cursor.execute(query)
row = cursor.fetchone()

conn.close()

print(row)
