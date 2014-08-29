import sqlite3

conn = sqlite3.connect('jsondata.db')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS drawings(fname string primary key, img_data text)")
conn.commit()
conn.close()