print("============================================")
print("Nama  : KHAIRANI BILQIS")
print("NIM   : 121140091")
print("Kelas : RB")
print("============================================")
print("~~    Tugas Program Python Minggu Ke-2    ~~")
print("============================================")
print()
 
class Mahasiswa:
    def __init__(self, nama, nim, semester, kelas_pbo, sks, total_sks_saat_ini):
        self.nama = nama
        self.nim = nim
        self.semester = semester
        self.kelas_pbo = kelas_pbo
        self.sks = sks
        self.total_sks_saat_ini = total_sks_saat_ini

    def data_mahasiswa(self):
        print("Nama Mahasiswa          : ", self.nama)
        print("NIM Mahasiswa           : ", self.nim)
        print("Semester Mahasiswa      : ", self.semester)
        print("Kelas PBO Siakad        : ", self.kelas_pbo)
        print("Jumlah SKS Mahasiswa    : ", self.sks)
        print("SKS Transkip Mahasiswa  : ", self.total_sks_saat_ini)

data = Mahasiswa("Khairani Bilqis", "121140091", "4", "RB", "22", "61")
data.data_mahasiswa()
