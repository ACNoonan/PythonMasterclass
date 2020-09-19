import sqlite3

db = sqlite3.connect("contacts.sqlite")


search_name = input("Who're we 'ookin for then? ")

check_sql = "SELECT * FROM contacts WHERE name = ?"

for row in db.execute(check_sql, (search_name,)):
    print(row)

db.close()
