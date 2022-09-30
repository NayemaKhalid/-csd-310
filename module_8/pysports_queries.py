# importing libraries
import errno
import mysql.connector
from mysql.connector import errorcode

# defining config of the database
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database":"pysports",
    "raise_on_warnings":True
}

try: 
    # assigning db connector
    db = mysql.connector.connect(**config)
    print(f"\nDatabase user {config['user']} connected to MySQL on host {config['host']} with database {config['database']} \n \n")

    #defining team cursor
    cursor = db.cursor()

    #querying team table
    cursor.execute("SELECT team_id, team_name, mascot FROM team")
    teams = cursor.fetchall()

    print("-- DISPLAYING TEAM RECORDS --")

    #printing team table
    for team in teams: 
        print(f"Team ID: {team[0]}")
        print(f"Team Name: {team[1]}")
        print(f"Mascot: {team[2]}")
        print("\n")


    #defining player cursor
    player_cursor = db.cursor()

    #querying team table
    player_cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
    players = player_cursor.fetchall()

    print("-- DISPLAYING PLAYER RECORDS --")

    #printing team table
    for player in players: 
        print(f"Player ID: {player[0]}")
        print(f"First Name: {player[1]}")
        print(f"Last Name: {player[2]}")
        print(f"Team ID: {player[3]}")
        print("\n")

    input("\n\nPress any key to continue..")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist.")
    else:
        print(err)

finally:
    db.close()