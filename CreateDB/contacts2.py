import sqlite3

db = sqlite3.connect("contacts.sqlite")

new_email = "appropriate_response.com"
phone = input("Give us a number then, love: ")

update_sql = "UPDATE contacts SET email = ? WHERE phone = ?"
update_cursor = db.cursor()
update_cursor.executescript(update_sql)
print("{} rows updated".format(update_cursor.rowcount))


update_cursor.connection.commit()
update_cursor.close()

for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print("-" * 20)

db.close()
