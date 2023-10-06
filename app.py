import elo

import mysql.connector


db = mysql.connector.connect(

    host = "localhost",
    user = "root",

    password = "3012",

    database = "Elo",

    auth_plugin='mysql_native_password'
)


cursor = db.cursor()


query = "SELECT ID, ELO FROM player"

cursor.execute(query)

result = cursor.fetchall()

playerList = []

for i in range(len(result)):
    playerList.append(elo.Player(result[i][0], result[i][1]))

p1id = int(input("Winner ID: "))
p2id = int(input("Loser ID: "))

elo.GameDone(playerList[p1id-1], playerList[p2id-1])
    
for i in range(len(playerList)):
    sql = "UPDATE player SET elo = %s WHERE id = %s"
    value = (playerList[i].elo, playerList[i].id)
    cursor.execute (sql, value)
db.close()
