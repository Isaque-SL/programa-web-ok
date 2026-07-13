import sqlite3

db_path = 'lojaAdmin/db.sqlite3'
conn = sqlite3.connect(db_path)
rows = list(conn.execute("SELECT app, name FROM django_migrations WHERE app='loja' ORDER BY name"))
if not rows:
    print('no migrations recorded for loja')
else:
    for r in rows:
        print(r)
conn.close()
