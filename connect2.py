import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="1cf_akademik"
)
 
if db.is_connected():
    print("Berhasil terhubung ke Database")
    
cursor = db.cursor ()
sql = "Select nip, nama, jenis_kelamin from dosen"

cursor.execute(sql)
results = cursor.fetchall()
for data in results:
    print(data)
