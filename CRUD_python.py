#variabel global  
buku=[]

#fungsi untuk menampilkan/read data di buku
def showData():
    if (len(buku)) <= 0:
        print (" Belum ada data")
    else:
        for i in range(len(buku)):
            print ("{} {}".format(i , buku[i]))

#fungsi menambahkan/insert data di buku
def insertData():
    bukuBaru = input("Judul Buku: ")
    buku.append(bukuBaru)

#fungsi mengedit data di buku
def editData():
    showData()
    i = int(input("masukan ID Buku: "))
    if (i > len(buku)):
        print ("ID salah")
    else:
        judulBaru = input("Judul baru")
        buku[i] = judulBaru
# fungsi untuk menghapus data di buku
def hapusData():
    showData()
    i= int(input("Masukan ID: "))
    if (i > len(buku)):
        print("ID salah")
    else:
        buku.remove(buku[i])

#fungsi untuk menampilkan menu
def showMenu():
    print ("""
    ========Menu==========
    [1] Show data
    [2] Insert data
    [3] Edit data
    [4] Delete data
    [5] exit
    """)
    menu = int(input("Masukan menu : "))

    if menu == 1:
        showData()
    if menu == 2:
        insertData()
    if menu == 3:
        editData()
    if menu == 4:
        hapusData()
    if menu == 5:
        exit()
    if menu > 6 :
        print ("salah input") 

if __name__ == "__main__":
    while (True):
        showMenu()
