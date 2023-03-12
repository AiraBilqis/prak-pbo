print("============================================")
print("Nama  : KHAIRANI BILQIS")
print("NIM   : 121140091")
print("Kelas : RB")
print("============================================")
print("~~      Tugas Python Minggu Ke-3 No.2     ~~")
print("============================================")
print()

class AkunBank:
    list_pelanggan = [] #atribut kelas

    #contstructor
    def __init__(self, no_pelanggan, nama_pelanggan, jumlah_saldo):
        self.__no_pelanggan = no_pelanggan
        self.__nama_pelanggan = nama_pelanggan
        self.__jumlah_saldo = jumlah_saldo
        self.list_pelanggan.append(self)
    
    def lihat_menu(self):
        print(f"Halo {Akun1.__nama_pelanggan}, ingin melakukan apa?")
        print(" 1. Cek Saldo \n 2. Tarik Tunai \n 3. Transfer Saldo \n 4. Keluar \n")
    
    def lihat_saldo(self):
        print(f"\n{Akun1.__nama_pelanggan}, memiliki saldo Rp {Akun1.__jumlah_saldo},\n")

    def tarik_tunai(self, jmlh_tarik):
        if jmlh_tarik > Akun1.__jumlah_saldo:
            print("Nominal saldo yang Anda punya tidak cukup!\n")
        else:
            Akun1.__jumlah_saldo = Akun1.__jumlah_saldo - jmlh_tarik
            print("Saldo berhasil ditarik!")
            print(f"Sisa saldo anda Rp {Akun1.__jumlah_saldo},\n")
    
    def transfer(self, nominal_transaksi, no_pelanggan):
        if nominal_transaksi < self.__jumlah_saldo: 
            for pelanggan in self.list_pelanggan:
                if pelanggan.__no_pelanggan == no_pelanggan:
                    pelanggan.__jumlah_saldo += nominal_transaksi
                    self.__jumlah_saldo -= nominal_transaksi
                    print(f"Transfer dengan jumlah Rp. {nominal_transaksi} ke {pelanggan.__nama_pelanggan} sukses!\n")
            
            if pelanggan.__no_pelanggan != no_pelanggan:
                print("No rekening tujuan tidak dikenal! Kembali ke menu utama...\n")
        else:
            print("Saldo anda tidak mencukupi untuk melakukan transfer! Kembali Ke Menu Utama...\n")

Akun1 = AkunBank(1234, "Khairani", 5000000000)
Akun2 = AkunBank(2345, "Ukraina", 6666666666)
Akun3 = AkunBank(3456, "Elon Musk", 9999999999)

Ulang = True
while Ulang:
    print("Selamat datang di Bank Jago")
    Akun1.lihat_menu()
    akses_aktivitas_akun = (input("Masukkan nomor input : "))
    
    if akses_aktivitas_akun == '1':
        Akun1.lihat_saldo()
    elif akses_aktivitas_akun == '2':
        jmlh_tarik = int(input("\nMasukkan jumlah nominal yang akan ditarik : "))
        Akun1.tarik_tunai(jmlh_tarik)
    elif akses_aktivitas_akun == '3':
        nominal_transaksi_input = int(input("\nMasukkan jumlah nominal yang akan di transfer : "))
        no_pelanggan_input = input("Masukkan no rekening yang dituju : ")
        Akun1.transfer(nominal_transaksi_input, no_pelanggan_input)
    elif akses_aktivitas_akun == '4':
        Ulangi = False
