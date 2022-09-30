import mysql.connector
from mysql.connector import errorcode
config ={
	"user":"pysports_user",
	"password":"MYSQL8ISGREAT!",
	"host":"127.0.0.1",
	"database": "pysports",
	"raise_on_warnings": FALSE
}

try:
	db = mysql.connector.connect(**config)
	print("\n Database user {} connected to mysql on host {} with datatbase {}".
		format(config["user"], config["host"], config["database"]))
	input("\n \n Press any key to continue.... ")
except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("  The supplied user name or password are invalid")
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("  The specified database does not exist")
	else: 
		print(err)
	finally:
		db.close()


