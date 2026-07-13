import sqlite3

db_path = 'lojaAdmin/db.sqlite3'
conn = sqlite3.connect(db_path)
rows = list(conn.execute("PRAGMA table_info('loja_produto')"))
if not rows:
    print('table not found or empty')
else:
    for r in rows:
        print(r)
conn.close()
