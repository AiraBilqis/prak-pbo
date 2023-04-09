from abc import ABC
from abc import abstractmethod

class AkunBank(ABC): #kelas abstrak dan kelas parent
    def __init__(self, nama, tahun_daftar, saldo): #konstruktor
        self.nama = nama
        self.tahun_daftar = tahun_daftar
        self.saldo = saldo
        
    def lihat_saldo(self): #fungsi konkret
        print(f"{self.nama} memiliki saldo Rp {self.saldo}\n")
        
    @abstractmethod    
    def transfer_saldo(self, transfer):
        self.transfer = transfer
        return self.transfer
        #fungsi ini di implementasikan pada child class
    
    @abstractmethod
    def lihat_suku_bunga(self):
        #fungsi ini di implementasikan pada child class
        pass
    
class AkunGold(AkunBank): #child class
    def __init__(self, nama, tahun_daftar, saldo): 
        super().__init__(nama, tahun_daftar, saldo)
        
    def transfer_saldo(self, transfer):
        super().transfer_saldo(transfer)
        usia_akun = 2023 - self.tahun_daftar
        print(f"Usia Akun Bank = {usia_akun} tahun")
        
        if (usia_akun >= 3 and self.transfer > 100000):
            print("Biaya Administrasi Gratis")
            print(f"Total Transfer Pengguna : Rp {self.transfer}")
            print(f"Total Saldo Pengguna    : Rp {self.saldo - self.transfer}\n")
            self.saldo -= self.transfer
            
        elif (usia_akun < 3 and self.transfer > 100000):
            print("Biaya Administrasi Rp 2.000")
            self.transfer = self.transfer + 2000
            print(f"Total Transfer Pengguna : Rp {self.transfer}")
            print(f"Total Saldo Pengguna    : Rp {self.saldo - self.transfer}\n")
            self.saldo -= self.transfer
            
        elif (self.transfer < 100000):
            print("Bebas Biaya Administrasi")
            print(f"Total Transfer Pengguna : Rp {self.transfer}")
            print(f"Total Saldo Pengguna    : Rp {self.saldo - self.transfer}\n")
            self.saldo -= self.transfer
            
        else:
            print("Tidak Memenuhi Syarat Transfer")
            print(f"Total Saldo Pengguna    : Rp {self.saldo - self.transfer}\n")
            self.saldo -= self.transfer
            
    def lihat_suku_bunga(self):
        usia_akun = 2023 - self.tahun_daftar
        print(f"Usia Akun Bank = {usia_akun} tahun")
        
        if (usia_akun >= 3 and self.saldo >= 1000000000):
            print("Bunga Bulanan sebesar 1%")
            print(f"Saldo Rekening Pengguna : Rp {self.saldo}\n")
            
        elif (usia_akun < 3 and self.saldo >= 1000000000):
            print("Bunga Bulanan sebesar 2%")
            print(f"Saldo Rekening Pengguna : Rp {self.saldo}\n")
            
        elif (self.saldo < 1000000000):
            print("Bunga Bulanan sebesar 3%")
            print(f"Saldo Rekening Pengguna : Rp {self.saldo}\n")
            
        else:
            pass

class AkunSilver(AkunBank): #child class
    def __init__(self, nama, tahun_daftar, saldo):
        super().__init__(nama, tahun_daftar, saldo)
        
    def transfer_saldo(self, transfer):
        super().transfer_saldo(transfer)
        usia_akun = 2023 - self.tahun_daftar
        print(f"Usia Akun Bank = {usia_akun} tahun")
        
        if (usia_akun >= 3 and self.transfer > 100000):
            print("Biaya Administrasi Rp 2.000")
            self.transfer = self.transfer + 2000
            print(f"Total Transfer Pengguna : Rp {self.transfer}")
            print(f"Total Saldo Pengguna    : Rp {self.saldo - self.transfer}\n")
            self.saldo -= self.transfer
            
        elif (usia_akun < 3 and self.transfer > 100000):
            print("Biaya Administrasi Rp 5.000")
            self.transfer = self.transfer + 5000
            print(f"Total Transfer Pengguna : Rp {self.transfer}")
            print(f"Total Saldo Pengguna    : Rp {self.saldo - self.transfer}\n")
            self.saldo -= self.transfer
            
        elif (self.transfer < 100000):
            print("Bebas Biaya Administrasi")
            print(f"Total Transfer Pengguna : Rp {self.transfer}")
            print(f"Total Saldo Pengguna    : Rp {self.saldo - self.transfer}\n")
            self.saldo -= self.transfer
            
        else:
            print("Tidak Memenuhi Syarat Transfer")
            print(f"Total Saldo Pengguna    : Rp {self.saldo - self.transfer}\n")
            self.saldo -= self.transfer
            
    def lihat_suku_bunga(self):
        usia_akun = 2023 - self.tahun_daftar
        print(f"Usia Akun Bank = {usia_akun} tahun")
        
        if (usia_akun >= 3 and self.saldo >= 10000000):
            print("Bunga Bulanan sebesar 1%")
            print(f"Saldo Rekening Pengguna : Rp {self.saldo}\n")
            
        elif (usia_akun < 3 and self.saldo >= 10000000):
            print("Bunga Bulanan sebesar 2%")
            print(f"Saldo Rekening Pengguna : Rp {self.saldo}\n")
            
        elif (self.saldo < 10000000):
            print("Bunga Bulanan sebesar 3%")
            print(f"Saldo Rekening Pengguna : Rp {self.saldo}\n")
            
        else:
            pass

#Objek
Akun1 = AkunGold("Bilqis", 2019, 1300000000) 
Akun2 = AkunSilver("Zaki", 2022, 1300000) 

#Cetak Fungsi Objek 1
Akun1.lihat_saldo()
Akun1.lihat_suku_bunga()
Akun1.transfer_saldo(500000)
Akun1.lihat_saldo()

#Cetak Fungsi Objek 2
Akun2.lihat_saldo()
Akun2.lihat_suku_bunga()
Akun2.transfer_saldo(130000)
Akun2.lihat_saldo()