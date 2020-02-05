import csv
database = 'cicil.csv'

def bayar():
    while True:
        file1 = open(database, 'r')
        read = csv.reader(file1, delimiter=";")

        pilih = input("Ingin bayar cicilan no berapa? \nInput:")
        temp = []
        error_message = "Tidak ada data"

        for i in read:
            temp.append(i)

        for i in temp:
            found = True
            if i[0] == pilih and found :
                data_change = i
                print(data_change)
                print("Anda akan membayar cicilan tersebut")
                bayar = int(input("Bayar berapa? \nInput: "))
                sisa_bayar = int(i[4]) - bayar

                if sisa_bayar == 0:
                    print("Selamat anda sudah lunas pas")
                    error_message = "Transaksi Selesai, ingin transaksi lagi ? "
                elif sisa_bayar < 0:
                    print("anda membayar kelebihan sebanyak Rp.",(sisa_bayar*(-1)))
                    error_message = "Transaksi Selesai, ingin transaksi lagi ? "
                    break
                data_change[2] = int(data_change[2]) - 1
                data_change[4] = sisa_bayar
                print(data_change)
                temp[int(i[0])-1] = data_change
                print(temp)
                file_to_change = open(database, 'w')
                file_updated = csv.writer(file_to_change,delimiter=";")
                file_updated.writerows(temp)
                # closing section
                file_to_change.close()
                file1.close()
                error_message = "Transaksi Selesai, ingin transaksi lagi ? "
                break
        print(error_message)
        proses_lagi = input("Ingin bayar lagi ? y/n")
        if proses_lagi == 'n':
            break
    # bayar()

def inputan(a,b,c,d,e):
    file = open(database, 'a')
    appen = csv.writer(file, delimiter=";")
    data = [a, b, c, d, e]
    print("Cicilan anda yang ke-",data[0],"adalah",data[1],"\nAngsuran yang diambil:",data[2],"x\nDengan harga",data[3], ",sudah dicicil sebesar",data[4])
    appen.writerow(data)


def tambahCicil():
    print("%2s \t %10s \t %10s \t %10s \t %10s" % ("No", "Barang", "Angsuran", "Harga", "Sisa Angsuran"))
    file = open(database, 'r')
    first_number = sum(1 for data in file)
    while True:
        first_number += 1
        print("No: ",first_number)
        a = first_number
        b = input("Nama barang: ")
        if b == '.':
            break
        c = int(input("Berapa kali angsur: "))
        d = int(input("Harga: "))
        e = int(input("Sisa Angsuran: "))
        inputan(a, b, c, d, e)
        print("Data telah ditambahkan")
    masuk()


def reminder():
    file11 = open(database, 'r')
    read = csv.reader(file11, delimiter=";")
    temp = []
    pembayaran = 0
    angsuran = 0
    print("Cicilan anda: ")
    for data in read:
        temp.append(data)
    for i in range(len(temp)):
        pembayaran = int(temp[i][4])
        angsuran = int(temp[i][2])
        print(
            "data ke : " + str(i+1) + "\n"+
            "Nama Barang : " + temp[i][1] + "\n"+
            "Sisa Angsuran : " + temp[i][2] + "x\n" +
            "Jumlah Yang harus dibayar : " + temp[i][4] + "\n" +
            "Rekomendasi Pembayaran setiap angsuran : " + str(pembayaran/angsuran)
        )


def masuk():
    pilih = input("Apa yang ingin Anda lakukan? \n1. Tambah cicilan \t 2.Bayar cicilan \t 3. Kembali \nInput: ")
    if pilih == "1":
        tambahCicil()
    elif pilih == "2":
        bayar()
    elif pilih == "3":
        menu()
    else:
        print("Pilihan tidak tersedia, coba kembali")
        masuk()


def menu():
    pilih = input("Met datang di program simulasi cicilan, apa yang ingin Anda lakukan? \n1. Masuk Program \t 2. Pengingat cicilan \t 3. Keluar \nInput: ")
    if pilih == "1":
        masuk()
    elif pilih == "2":
        reminder()
    elif pilih == "3":
        exit(0)
    else:
        print("Pilihan tidak tersedia, silahkan coba lagi")
        menu()

menu()