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
sql = "SELECT a.nama, b.nama_prodi,b.jenjang FROM dosen a, prodi b WHERE a.kode_prodi=b.kode AND b.jenjang='D3'"

cursor.execute(sql)
results = cursor.fetchall()
for data in results:
    print(data)
