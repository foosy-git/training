# import pymysql
# mysql_conn = pymysql.connect(host="localhost", user="root", password="9137652j", db="sakila")
# mysql_cursor = mysql_conn.cursor()

# #show all table in sakila
# mysql_cursor.execute("show tables")
# for table in mysql_cursor:
#   print(table[0])

# %load_ext sql
# %sql mysql+pymysql://root:9137652j@localhost/sakila
# %sql select * from actor limit 10

import sqlite3
sqlite_conn = sqlite3.connect('socioeconomic.db')
sqlite_cur = sqlite_conn.cursor()
import pymysql
mysql_conn = pymysql.connect(host="localhost", user="root", password="XXX", db="sakila")
mysql_cur = mysql_conn.cursor()

sqlite_cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = sqlite_cur.fetchall()
for t in tables:
  print(t[0])

for table_name in tables:
    table_name = table_name[0]
    sqlite_cur.execute(f"SELECT * FROM {table_name}")
    rows = sqlite_cur.fetchall()
    
    #create the table in the MySQL database
    try:
        # Replace spaces in column names with underscores
        columns = [col[0].replace(' ', '_').replace(",", "").replace("(", "").replace(")", "") + ' TEXT' if col[1] is None else col[0].replace(' ', '_') + ' ' + col[1] for col in sqlite_cur.description]
        print(f"CREATE TABLE {table_name} ({','.join(columns)})")
        mysql_cur.execute(f"DROP TABLE IF EXISTS {table_name}")
        mysql_cur.execute(f"CREATE TABLE {table_name} ({','.join(columns)})")
        print(f"Created table {table_name}")
    except Exception as e:
        print(f"Error creating table {table_name}: {e}")

    insert the data into the MySQL table
    for row in rows:
        placeholders = ','.join(['%s' for _ in row])
        mysql_cur.execute(f"INSERT INTO {table_name} VALUES ({placeholders})", row)

    print(f"{len(rows)} rows copied from {table_name} to MySQL")

mysql_conn.commit()
mysql_conn.close()
sqlite_conn.close()