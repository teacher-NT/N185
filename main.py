import os
os.system("cls")

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database= "dars_baza"
)

query1 = """SELECT * FROM users 
            WHERE joined_date > '2010-01-01';
    """

query2 = """INSERT INTO users (user_id, username, first_name, last_name, posts_count,followers, followings, joined_date)
    VALUES
    (33,'shamsiddin', 'Shamsiddin', 'Tursunov', 0, 2000, 15000, '2010-11-01')
"""
query3 = """UPDATE users
        SET joined_date = '2011-03-29'
        WHERE user_id = 33;
"""

query4 = """DELETE FROM users
    where username is NULL ;
"""

cursor = mydb.cursor()
cursor.execute(query4)
mydb.commit()
print(cursor.rowcount, "ta qatorda o'zgarish bo'ldi")

# data = cursor.fetchall()
# for qator in data:
#     print(qator)

# data = cursor.fetchone()
# print(data)

# data = cursor.fetchmany(5)
# for qator in data:
#     print(qator)