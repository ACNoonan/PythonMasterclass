import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Adam', 9197457023, "
           "'an@aol.com')")
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Brian', 9197777023, "
           "'brian@aol.com')")
cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())


for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print('-' * 40)


cursor.close()
db.commit()
db.close()
