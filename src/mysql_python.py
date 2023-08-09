import mysql.connector

sql_conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "test",
    database = "test"
)

object = sql_conn.cursor()

query = "SELECT * FROM barcode"
object.execute(query)


rows = object.fetchall()

for row in rows:
    print(row)
