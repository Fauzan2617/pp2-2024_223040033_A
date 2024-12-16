import pandas as pd

# Data for the table
data = {
    "No": [
        1, 1, 1, 1, 1,
        2, 2, 2, 2, 2,
        3, 3, 3, 3, 3,
        4, 4, 4, 4, 4
    ],
    "Kelas": [
        "Akun", "Akun", "Akun", "Akun", "Akun",
        "Sampah", "Sampah", "Sampah", "Sampah", "Sampah",
        "Transaksi Penjemputan", "Transaksi Penjemputan", "Transaksi Penjemputan", "Transaksi Penjemputan", "Transaksi Penjemputan",
        "Kurir", "Kurir", "Kurir", "Kurir", "Kurir"
    ],
    "Operasi": [
        "getAkun", "getAllAkun", "setAkun", "updateAkun", "deleteAkun",
        "getSampah", "getAllSampah", "setSampah", "updateSampah", "deleteSampah",
        "getTransaksi", "getAllTransaksi", "setTransaksi", "updateTransaksi", "deleteTransaksi",
        "getKurir", "getAllKurir", "setKurir", "updateKurir", "deleteKurir"
    ],
    "Algoritma": [
        "function getAkun(idAkun: Integer): Record\nreturn akun",
        "function getAllAkun(): List\nreturn daftarAkun",
        "procedure setAkun(data: Record)\nakun = data",
        "procedure updateAkun(data: Record)\nakun = data",
        "procedure deleteAkun(idAkun: Integer)\nDELETE akun",
        "function getSampah(idSampah: Integer): Record\nreturn sampah",
        "function getAllSampah(): List\nreturn daftarSampah",
        "procedure setSampah(data: Record)\nsampah = data",
        "procedure updateSampah(data: Record)\nsampah = data",
        "procedure deleteSampah(idSampah: Integer)\nDELETE sampah",
        "function getTransaksi(idTransaksi: Integer): Record\nreturn transaksi",
        "function getAllTransaksi(): List\nreturn daftarTransaksi",
        "procedure setTransaksi(data: Record)\ntransaksi = data",
        "procedure updateTransaksi(data: Record)\ntransaksi = data",
        "procedure deleteTransaksi(idTransaksi: Integer)\nDELETE transaksi",
        "function getKurir(idKurir: Integer): Record\nreturn kurir",
        "function getAllKurir(): List\nreturn daftarKurir",
        "procedure setKurir(data: Record)\nkurir = data",
        "procedure updateKurir(data: Record)\nkurir = data",
        "procedure deleteKurir(idKurir: Integer)\nDELETE kurir"
    ],
    "Query": [
        "SELECT * FROM Akun WHERE ID_Akun = ?",
        "SELECT * FROM Akun",
        "INSERT INTO Akun (ID_Akun, Nama, Email, Password, Alamat, No_Handphone) VALUES (?, ?, ?, ?, ?, ?)",
        "UPDATE Akun SET Nama = ?, Email = ?, Password = ?, Alamat = ?, No_Handphone = ? WHERE ID_Akun = ?",
        "DELETE FROM Akun WHERE ID_Akun = ?",
        "SELECT * FROM Sampah WHERE ID_Sampah = ?",
        "SELECT * FROM Sampah",
        "INSERT INTO Sampah (ID_Sampah, Nama_Sampah, Lokasi_DropBox, Kategori_Sampah, Deskripsi_Sampah, Point) VALUES (?, ?, ?, ?, ?, ?)",
        "UPDATE Sampah SET Nama_Sampah = ?, Lokasi_DropBox = ?, Kategori_Sampah = ?, Deskripsi_Sampah = ?, Point = ? WHERE ID_Sampah = ?",
        "DELETE FROM Sampah WHERE ID_Sampah = ?",
        "SELECT * FROM Transaksi_Penjemputan WHERE ID_Transaksi = ?",
        "SELECT * FROM Transaksi_Penjemputan",
        "INSERT INTO Transaksi_Penjemputan (ID_Transaksi, Tanggal, ID_Sampah, Status_Transaksi, ID_Kurir, ID_Akun) VALUES (?, ?, ?, ?, ?, ?)",
        "UPDATE Transaksi_Penjemputan SET Tanggal = ?, ID_Sampah = ?, Status_Transaksi = ?, ID_Kurir = ?, ID_Akun = ? WHERE ID_Transaksi = ?",
        "DELETE FROM Transaksi_Penjemputan WHERE ID_Transaksi = ?",
        "SELECT * FROM Kurir WHERE ID_Kurir = ?",
        "SELECT * FROM Kurir",
        "INSERT INTO Kurir (ID_Kurir, Nama_Kurir, Kontak, Alamat, No_Polisi, Merk_Motor) VALUES (?, ?, ?, ?, ?, ?)",
        "UPDATE Kurir SET Nama_Kurir = ?, Kontak = ?, Alamat = ?, No_Polisi = ?, Merk_Motor = ? WHERE ID_Kurir = ?",
        "DELETE FROM Kurir WHERE ID_Kurir = ?"
    ]
}

# Convert to a pandas DataFrame
df = pd.DataFrame(data)

# Save as an Excel file
file_name = "CRUD_Operations_Table.xlsx"
df.to_excel(file_name, index=False)

print(f"File saved as {file_name}")
import pandas as pd

# Data for the table
data = {
    "No": [
        1, 1, 1, 1, 1,
        2, 2, 2, 2, 2,
        3, 3, 3, 3, 3,
        4, 4, 4, 4, 4
    ],
    "Kelas": [
        "Akun", "Akun", "Akun", "Akun", "Akun",
        "Sampah", "Sampah", "Sampah", "Sampah", "Sampah",
        "Transaksi Penjemputan", "Transaksi Penjemputan", "Transaksi Penjemputan", "Transaksi Penjemputan", "Transaksi Penjemputan",
        "Kurir", "Kurir", "Kurir", "Kurir", "Kurir"
    ],
    "Operasi": [
        "getAkun", "getAllAkun", "setAkun", "updateAkun", "deleteAkun",
        "getSampah", "getAllSampah", "setSampah", "updateSampah", "deleteSampah",
        "getTransaksi", "getAllTransaksi", "setTransaksi", "updateTransaksi", "deleteTransaksi",
        "getKurir", "getAllKurir", "setKurir", "updateKurir", "deleteKurir"
    ],
    "Algoritma": [
        "function getAkun(idAkun: Integer): Record\nreturn akun",
        "function getAllAkun(): List\nreturn daftarAkun",
        "procedure setAkun(data: Record)\nakun = data",
        "procedure updateAkun(data: Record)\nakun = data",
        "procedure deleteAkun(idAkun: Integer)\nDELETE akun",
        "function getSampah(idSampah: Integer): Record\nreturn sampah",
        "function getAllSampah(): List\nreturn daftarSampah",
        "procedure setSampah(data: Record)\nsampah = data",
        "procedure updateSampah(data: Record)\nsampah = data",
        "procedure deleteSampah(idSampah: Integer)\nDELETE sampah",
        "function getTransaksi(idTransaksi: Integer): Record\nreturn transaksi",
        "function getAllTransaksi(): List\nreturn daftarTransaksi",
        "procedure setTransaksi(data: Record)\ntransaksi = data",
        "procedure updateTransaksi(data: Record)\ntransaksi = data",
        "procedure deleteTransaksi(idTransaksi: Integer)\nDELETE transaksi",
        "function getKurir(idKurir: Integer): Record\nreturn kurir",
        "function getAllKurir(): List\nreturn daftarKurir",
        "procedure setKurir(data: Record)\nkurir = data",
        "procedure updateKurir(data: Record)\nkurir = data",
        "procedure deleteKurir(idKurir: Integer)\nDELETE kurir"
    ],
    "Query": [
        "SELECT * FROM Akun WHERE ID_Akun = ?",
        "SELECT * FROM Akun",
        "INSERT INTO Akun (ID_Akun, Nama, Email, Password, Alamat, No_Handphone) VALUES (?, ?, ?, ?, ?, ?)",
        "UPDATE Akun SET Nama = ?, Email = ?, Password = ?, Alamat = ?, No_Handphone = ? WHERE ID_Akun = ?",
        "DELETE FROM Akun WHERE ID_Akun = ?",
        "SELECT * FROM Sampah WHERE ID_Sampah = ?",
        "SELECT * FROM Sampah",
        "INSERT INTO Sampah (ID_Sampah, Nama_Sampah, Lokasi_DropBox, Kategori_Sampah, Deskripsi_Sampah, Point) VALUES (?, ?, ?, ?, ?, ?)",
        "UPDATE Sampah SET Nama_Sampah = ?, Lokasi_DropBox = ?, Kategori_Sampah = ?, Deskripsi_Sampah = ?, Point = ? WHERE ID_Sampah = ?",
        "DELETE FROM Sampah WHERE ID_Sampah = ?",
        "SELECT * FROM Transaksi_Penjemputan WHERE ID_Transaksi = ?",
        "SELECT * FROM Transaksi_Penjemputan",
        "INSERT INTO Transaksi_Penjemputan (ID_Transaksi, Tanggal, ID_Sampah, Status_Transaksi, ID_Kurir, ID_Akun) VALUES (?, ?, ?, ?, ?, ?)",
        "UPDATE Transaksi_Penjemputan SET Tanggal = ?, ID_Sampah = ?, Status_Transaksi = ?, ID_Kurir = ?, ID_Akun = ? WHERE ID_Transaksi = ?",
        "DELETE FROM Transaksi_Penjemputan WHERE ID_Transaksi = ?",
        "SELECT * FROM Kurir WHERE ID_Kurir = ?",
        "SELECT * FROM Kurir",
        "INSERT INTO Kurir (ID_Kurir, Nama_Kurir, Kontak, Alamat, No_Polisi, Merk_Motor) VALUES (?, ?, ?, ?, ?, ?)",
        "UPDATE Kurir SET Nama_Kurir = ?, Kontak = ?, Alamat = ?, No_Polisi = ?, Merk_Motor = ? WHERE ID_Kurir = ?",
        "DELETE FROM Kurir WHERE ID_Kurir = ?"
    ]
}

# Convert to a pandas DataFrame
df = pd.DataFrame(data)

# Save as an Excel file
file_name = "CRUD_Operations_Table.xlsx"
df.to_excel(file_name, index=False)

print(f"File saved as {file_name}")
