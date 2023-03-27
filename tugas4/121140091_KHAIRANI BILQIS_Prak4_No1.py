print("============================================")
print("Nama  : KHAIRANI BILQIS")
print("NIM   : 121140091")
print("Kelas : RB")
print("============================================")
print("~~      Tugas Python Minggu Ke-4 No.1     ~~")
print("============================================")
print()

class Komputer:
    def __init__(self, merk, jenis, harga):
        self.merk = merk
        self.jenis = jenis
        self.harga = harga

    def __str__(self):
        return f"{self.nama} {self.jenis} produksi {self.merk}"

class Processor(Komputer):
    def __init__(self, merk, jenis, harga, jumlah_core, kecepatan_processor) -> None:
        Komputer.__init__(self, merk, jenis, harga)
        self.nama = "Processor"
        self.jumlah_core = jumlah_core
        self.kecepatan_processor = kecepatan_processor

class RAM(Komputer):
    def __init__(self, merk, jenis, harga, capasity_ram):
        Komputer.__init__(self, merk, jenis, harga)
        self.nama = "RAM"
        self.capasity_ram = capasity_ram

class HDD(Komputer):
    def __init__(self, merk, jenis, harga, capasity_hdd, rpm):
        Komputer.__init__(self, merk, jenis, harga)
        self.nama = "SATA"
        self.capasity_hdd = capasity_hdd
        self.rpm = rpm

class VGA(Komputer):
    def __init__(self, merk, jenis, harga, capasity_vga):
        Komputer.__init__(self, merk, jenis, harga)
        self.nama = "VGA"
        self.capasity_vga = capasity_vga

class PSU(Komputer):
    def __init__(self, merk, jenis, harga, daya_psu):
        Komputer.__init__(self, merk, jenis, harga)
        self.nama = "PSU"
        self.daya_psu = daya_psu

p1 = Processor('Intel', 'Core i7 7740X', 4350000, 4, '4.3GHz')
p2 = Processor('AMD', 'Ryzen 5 3600', 250000, 4, '4.3GHz')
ram1 = RAM('V-Gen', 'DDR4 SODimm PC19200/2400MHz', 328000, '4GB')
ram2 = RAM('G.SKILL', 'DDR4 2400MHz', 328000, '4GB')
hdd1 = HDD('Seagate', 'HDD 2.5 inch', 295000, '500GB', 7200)
hdd2 = HDD('Seagate', 'HDD 2.5 inch', 295000, '1000GB', 7200)
vga1 = VGA('Asus', 'VGA GTX 1050',250000, '2GB')
vga2 = VGA('Asus', '1060Ti', 250000, '8GB')
psu1 = PSU('Corsair', 'Corsair V550', 250000, '500W')
psu2 = PSU('Corsair', 'Corsair V550', 250000, '500W')

rakit = [[p1, ram1, hdd1, vga1, psu1], [p2, ram2, hdd2, vga2, psu2]]

for i, computer_pc in enumerate(rakit) : 
    print("Komputer ", i+1)
    for komponen in computer_pc :
        print(komponen)
    print ("")

print()
