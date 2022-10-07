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
	# defining cursor 
	cursor = db.cursor()
	#  execute query 
	cursor.execute("select player_id, first_name, last_name, team_name from player inner join team on player.team_id = team.team_id")
	# fetching all data
	teams = cursor.fetchall()
	print("-- Displaying Players Records --")
	# displaying all records
	for i in teams:
		 print(f"Player ID: {i[0]}"),
         print(f"First Name: {i[1]}"),
         print(f"Last Name: {i[2]}"),
         print(f"Team Name: {i[3]}"),
         print("\n")

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


