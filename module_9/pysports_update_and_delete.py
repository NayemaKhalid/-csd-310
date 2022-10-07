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

	# defining inert cursor 
	ins_cursor = db.cursor()
	ins_cursor.execute("INSERT INTO `pysports`.`player` (`player_id`, `first_name`, `last_name`, `team_id`) VALUES ('21', 'Smeagol', 'Shire Folk', '1')")
	db.commit()
	ins_cursor.execute("select player_id, first_name, last_name, team_name from player inner join team on player.team_id = team.team_id")
	ins_data = ins_cursor.fetchall()
	print("-- Displaying Players After Insert --")
	# printing data after inserting record
	for i in ins_data:
		 print(f"Player ID: {i[0]}"),
         print(f"First Name: {i[1]}"),
         print(f"Last Name: {i[2]}"),
         print(f"Team Name: {i[3]}"),
         print("\n") 
	
	# defining updation cursor
	upd_cursor = db.cursor()
	upd_cursor.execute("Update player SET team_id = 2, first_name = 'Gollum', last_name = 'RIng Stealer' where first_name = 'Smeagol'")
	db.commit()
	upd_cursor.execute("select player_id, first_name, last_name, team_name from player inner join team on player.team_id = team.team_id")
	upd_data = upd_cursor.fetchall()
	print("-- Displaying Players After Update --")
	# printing data after update 
	for i in upd_data:
		 print(f"Player ID: {i[0]}"),
         print(f"First Name: {i[1]}"),
         print(f"Last Name: {i[2]}"),
         print(f"Team Name: {i[3]}"),
         print("\n")

	# defining deletion cursor
	del_cursor = db.cursor()
	del_cursor.execute("delete from player where first_name = 'Gollum'")
	db.commit()
	del_cursor.execute("select player_id, first_name, last_name, team_name from player inner join team on player.team_id = team.team_id")
	del_data = del_cursor.fetchall()
	print("-- Displaying Players After Delete --")
	# printing data after update 
	for i in del_data:
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

