#ASCII ART FOR DICE---
#print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
#● ┌ ─ ┐ │ └ ┘

diceart={1:("┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘"),

         2:("┌─────────┐",
            "│         │",
            "│   ● ●   │",
            "│         │",
            "└─────────┘"),

         3:("┌─────────┐",
            "│  ●   ●   │",
            "│         │",
            "│    ●    │",
            "└─────────┘"),

         4:("┌─────────┐",
            "│  ●  ●   │",
            "│         │",
            "│  ●  ●   │",
            "└─────────┘"),

         5:("┌─────────┐",
            "│ ●  ●  ● │",
            "│         │",
            "│  ●   ●  │",
            "└─────────┘"),

         6:("┌─────────┐",
            "│ ●  ●  ● │",
            "│         │",
            "│ ●  ●  ● │",
            "└─────────┘")   }

#FN FOR ROLLING DICE---
def roll():
    import random
    global rand_num
    rand_num=random.randint(1,6)
    for i in diceart[rand_num]:
        print(i,end="\n")

#FN FOR CREATING SCORE TRACKER---
def addname(x):
    import mysql.connector
    db=mysql.connector.connect(host="localhost",
                               user="root",
                               passwd="mysql",
                               database="pig")
    mycursor=db.cursor()
    mycursor.execute("CREATE TABLE IF NOT EXISTS score_track(name varchar(20), score int(2), id int(1) PRIMARY KEY AUTO_INCREMENT)")
    sql="INSERT INTO score_track (name, score) VALUES (%s, %s)"
    t=(x, 0)
    mycursor.execute(sql,t)
    db.commit()

#FOR FETCHING SCORE---
def fetch_score():
    import mysql.connector

    db = mysql.connector.connect(host="localhost",
                                 user="root",
                                 passwd="mysql",
                                 database="pig")
    mycursor = db.cursor()
    mycursor.execute("SELECT score FROM score_track")
    result = mycursor.fetchall()
    mycursor.close()
    db.close()

    result_list = [list(row) for row in result]

    return result_list

#FOR FETCHING A NAME---
def fetch_name():
    import mysql.connector

    db = mysql.connector.connect(host="localhost",
                                 user="root",
                                 passwd="mysql",
                                 database="pig")
    mycursor = db.cursor()
    mycursor.execute("SELECT name FROM score_track")
    result = mycursor.fetchall()
    mycursor.close()
    db.close()

    result_list = [list(row) for row in result]

    return result_list

#FOR UPDATING SCORE THROUGH ONE GAME---
def update_score(name, new_score):
    import mysql.connector

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mysql",
        database="pig")

    mycursor = db.cursor()
    sql= "UPDATE score_track SET score = %s WHERE name = %s"
    values = (new_score, name)
    mycursor.execute(sql, values)
    db.commit()

#FOR CLEARING TABLE---
def clear():
    import mysql.connector

    db = mysql.connector.connect(host="localhost",
                                 user="root",
                                 passwd="mysql",
                                 database="pig")
    mycursor = db.cursor()
    mycursor.execute("DROP TABLE IF EXISTS score_track")
    mycursor.close()
    db.close()

#FOR FINDING WINNER---
def find_winner():
    import mysql.connector

    db = mysql.connector.connect(host="localhost",
                                 user="root",
                                 passwd="mysql",
                                 database="pig")
    mycursor = db.cursor()
    mycursor.execute("SELECT MAX(score) FROM score_track")
    max_score=mycursor.fetchone()[0]
    query="SELECT name FROM score_track WHERE score = %s"
    mycursor.execute(query, (max_score,))
    winner=mycursor.fetchone()[0]
    print(f"\n\nThe winner is {winner}- Congratulations!")
    mycursor.close()
    db.close()
