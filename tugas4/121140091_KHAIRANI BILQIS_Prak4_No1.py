print("============================================")
print("Nama  : KHAIRANI BILQIS")
print("NIM   : 121140091")
print("Kelas : RB")
print("============================================")
print("~~      Tugas Python Minggu Ke-4 No.1     ~~")
print("============================================")
print()

class Komputer:
    def __init__(self, nama, jenis, harga, merk):
        self.nama = nama
        self.jenis = jenis
        self.harga = harga
        self.merk = merk
    
class Processor(Komputer):
    def __init__(self, nama, jenis, harga, merk, jumlah_core, kecepatan_processor):
        super().__init__(nama, jenis, harga, merk)
            self.jumlah_core = jumlah_core
            self.kecepatan_processor = kecepatan_processor
        
class RAM(Komputer):
    def __init__(self, nama, jenis, harga, merk, capacity_ram):
        super().__init__(nama, jenis, harga, merk)
            self.capacity_ram = capacity_ram

class HDD(Komputer):
    def __init__(self, nama, jenis, harga, merk, capacity_hdd, rpm_hdd):
        super().__init__(nama, jenis, harga, merk)
            self.capacity_hdd = capacity_hdd
            self.rpm_hdd = rpm_hdd

class VGA(Komputer):
    def __init__(self, nama, jenis, harga, merk, capacity_vga):
        super().__init__(nama, jenis, harga, merk)
            self.capacity_vga = capacity_vga

class PSU(Komputer):
    def __init__(self, nama, jenis, harga, merk, daya_psu):
        super().__init__(nama, jenis, harga, merk)
            self.daya_psu = daya_psu

rakit = [[p1, ram1, hdd1, vga1, psu1],[p2, ram2, hdd2, vga2, psu2]]

p1 = Processor('Intel', 'Core i7 7740X', 4350000, 4, '4.3GHz')
p2 = Processor('AMD', 'Ryzen 5 3600', 250000, 4, '4.3GHz')
ram1 = RAM('V-Gen', 'DDR4 SODimm PC19200/2400MHz', 328000, '4GB')
ram2 = RAM('G.SKILL', 'DDR4 2400MHz', 328000, '4GB')
hdd1 = HDD('Seagate', 'HDD 2.5 inch', 295000, '500GB', 7200)
hdd2 = HDD('Seagate', 'HDD 2.5 inch', 295000, '1000GB', 7200)
vga1 = VGA('Asus', 'VGA GTX 1050', 250000, '2GB')
vga2 = VGA('Asus', '1060Ti', 250000, '8GB')
psu1 = PSU('Corsair', 'Corsair V550', 250000, '500W')
psu2 = PSU('Corsair', 'Corsair V550', 250000, '500W')
