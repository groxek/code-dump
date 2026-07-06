import psycopg2
from psycopg2.extras import DictCursor
conn = psycopg2.connect(
    host = "127.0.0.1",
    user = "postgres",
    password = "",
    port = 5432,
    dbname = "postgres"
)

if conn:
    print('asd')


cursor = conn.cursor(cursor_factory=DictCursor)
title = input('Введите заголовок ')
preview = input('Введите анонс ')
sql = f"INSERT INTO news(title, preview) VALUES(%s, %s)"
cursor.execute(sql, (title, preview))
conn.commit()

cursor.execute("SELECT * FROM news")
result = cursor.fetchall()
print(type(result))

for news in result:
    print(news['title'])

cursor.close()
conn.close()