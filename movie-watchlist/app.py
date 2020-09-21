import psycopg2

url = "postgres://mvvkwtps:j5rKWNdxSyxJ9bzmK5r6v2de9mdFspy1@lallah.db.elephantsql.com:5432/mvvkwtps"
connection = psycopg2.connect(url)

cursor = connection.cursor()
cursor.execute("SELECT * FROM users;")
first_user = cursor.fetchone()

print(first_user)

connection.close()