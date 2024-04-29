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
sql = "CREATE TABLE Prodi(kode char(5) NOT NULL PRIMARY KEY,nama_prodi varchar(100) NOT NULL,status varchar(15),jenjang varchar(15),akreditasi varchar(15));"
try:
    cursor.execute(sql)
    print("Tabel berhasil dibuat")
except mysql.connector.Error as err:
    print(f"{err}")
