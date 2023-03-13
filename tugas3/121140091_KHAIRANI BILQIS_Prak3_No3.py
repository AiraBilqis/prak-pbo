print("============================================")
print("Nama  : KHAIRANI BILQIS")
print("NIM   : 121140091")
print("Kelas : RB")
print("============================================")
print("~~      Tugas Python Minggu Ke-3 No.3     ~~")
print("============================================")
print()

#class 
class Laptop:
    #atribut kelas
    jmlh_laptop = 0
    
    #constructor
    def __init__(self, merk, pemilik, ram, jenis_processor):
        self.merk = merk                         #atribut public
        self._pemilik = pemilik                  #atribut protected
        self._ram = ram                          #atribut protected
        self.__jenis_processor = jenis_processor #atribut private
        
        Laptop.jmlh_laptop += 1
    
    #fungsi untuk menampilkan jumlah laptop yang masuk
    def __tampilkan_jmlh_laptop(self):
        print(Laptop.jmlh_laptop)
        
    #fungsi untuk menampilkan merek laptop
    def merk_laptop(self):
        print("Merek Laptop    : ", self.merk)
    
    #fungsi untuk menampilkan nama user
    def akses_pemilik(self):
        print("Nama User       : ", self._pemilik)
    
    #fungsi untuk menampilkan ram laptop    
    def tampilkan_ram(self):
        print("RAM Laptop      : ", self._ram, " GB")
    
    #fungsi untuk menambah ram    
    def _update_ram(self, ram_baru):
        self._ram = self._ram + ram_baru
    
    #fungsi untuk menampilkan jenis processor        
    def tampilkan_processor(self):
        print("Jenis Processor : ", self.__jenis_processor)
  
#Objek 1
laptop1 = Laptop("Acer", "Khairani", 4, "Intel Core i7-4790 3.6Ghz")

laptop1.merk_laptop()         #Merek Laptop    : Acer
laptop1.akses_pemilik()       #Nama User       : Khairani
laptop1.tampilkan_ram()       #RAM Laptop      : 4 GB
laptop1.tampilkan_processor() #Jenis Processor : Intel Core i7-4790 3.6Ghz

#mengupdate ram pengguna
laptop1._update_ram(4)
laptop1.tampilkan_ram() #RAM Laptop      : 8 GB
print("\n")

#Objek 2
laptop2 = Laptop("Lenovo", "Zaki", 4, "Intel Core i5-5200U 2.20GHz")

laptop2.merk_laptop()         #Merek Laptop    : Lenovo
laptop2.akses_pemilik()       #Nama User       : Zaki
laptop2.tampilkan_ram()       #RAM Laptop      : 4 GB
laptop2.tampilkan_processor() #Jenis Processor : Intel Core i5-5200U 2.20GHz

print("\nJumlah laptop   : ", Laptop.jmlh_laptop, " buah")
