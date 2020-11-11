print ("=======================")
print ("Selamat Datang Di Dealer Sepeda Motor Kita Semua")
print ("=======================")
print ("Silahkan Masukkan Data Diri Anda Sebelum Melakukan Pembelian")

nama= input ("Silahkan Masukkan Nama Anda : ")
print (nama)

jenis_kelamin= input ("pria atau wanita? : " )
print (jenis_kelamin)

NIK= input ("Silahkan Masukkan Nomer Induk Kependudukan : ")
print (NIK)

no_kk= input ("Silahkan Masukkan No KK : ")
print (no_kk) 

alamat= input("Silahkan Masukkan Alamat : ")
print (alamat)

no_hp= input ("Silahkan Masukkan Nomer Hp Anda : ")
print (no_hp)

usia= input ("Masukkan Usia Anda : " ) 
print (usia)

print ("Jenis-Jenis Sepeda Motor Yang Ada Di Toko Kami")

sepeda_motor = ["beat","vario","crf","satria","vixion","shogun","nmax","jupiter","pcx"]
print (sepeda_motor)


beat = int (17000000)
vario = int (17600000)
crf = int (34450000)
satria = int (23300000)
vixion = int (28200000)
shogun = int (16900000)
nmax = int (33600000)
jupiter = int (18900000)
pcx = int (29800000)

harga_motor= str(input("Silahkan Pilih Jenis Sepeda Motor Apa Yang Anda Inginkan :"))
if harga_motor == "beat":
    print("Harga Sepeda Motor Beat Adalah : ",beat)

elif harga_motor == "vario":
    print ("Harga Sepeda Motor Vario Adalah :",vario)

elif harga_motor == "crf":
    print("Harga Sepeda Motor Crf Adalah:",crf)

elif harga_motor == "satria":
    print ("Harga Sepeda Motor Satria Adalah :",satria)

elif harga_motor == "vixion":
    print ("Harga Sepeda Motor Vixion Adalah :",vixion)

elif harga_motor == "shogun":
    print ("Harga Sepeda Motor Shogun Adalah :",shogun)

elif harga_motor == "nmax":
    print ("Harga Sepeda Motor Nmax Adalah :",nmax)

elif harga_motor == "jupiter":
    print ("Harga Sepeda Motor Jupiter Adalah :",jupiter)

elif harga_motor == "pcx":
    print ("Harga Sepeda Motor Pcx Adalah:",pcx)

print ("Warna-Warna Yang Tersedia : ")
warna=["Merah","Hitam","Biru","Kuning"]
print(warna)
warna_motor= str(input("Silahkan Pilih Warna Sepeda Motor Apa Yang Anda Inginkan : "))

print ("Anda Mendapatkan Diskon Sebesar 5% Untuk Pembelian Di Bulan Ini")

total = int(input('Masukan Harga Sepeda Motor Yang Anda Inginkan : '))
setelah_diskon = total
 
if total > 100000:
    diskon = total * (5/100)
else:
    diskon = total * (5/100)
 
setelah_diskon = total - diskon
print("Diskonnya Sebesar : Rp {:,}".format(float(diskon)).replace(",","."))
print("Harga Yang Harus Anda Bayar Adalah: Rp {:,}".format(float(setelah_diskon)).replace(',','.'))

print ("Terima Kasih Sudah Berbelanja Ditoko Kami")
print ("Program Ini Dikembangkan Oleh Giovani Chadavi Hidayat")
print ("Tugas PostTest 2 APD 2020")
