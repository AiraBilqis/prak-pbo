print("============================================")
print("Nama  : KHAIRANI BILQIS")
print("NIM   : 121140091")
print("Kelas : RB")
print("============================================")
print("~~      Tugas Python Minggu Ke-4 No.2     ~~")
print("~~      Inheritance dan Polymorphism      ~~")
print("============================================")
print()

class Robot: 
    jumlah_turn = 0
    alive = True
    
    def __init__(self, nama, health, damage) -> None:
        self.nama = nama
        self.health = health
        self.damage = damage
        
    def lakukan_aksi(self, other):
        if self.nama == "Antares":
            if (Robot.jumlah_turn % 3) == 0:
                self.damage = self.damage * 1.5
                Robot.terima_aksi(other, self.damage)
                self.damage = 5 #to be changed
            else:
                Robot.terima_aksi(other, self.damage)
        elif self.nama == "Alphasetia":
            if (Robot.jumlah_turn % 2) == 0:
                self.health += 4000 #to be changed 
                Robot.terima_aksi(other, self.damage)
                return f"Alphasetia mendapatkan health tambahan sebesar 4000\n" #to be changed 
            else:
                Robot.terima_aksi(other, self.damage)
                return f"Alphasetia mendapatkan health tambahan sebesar 4000\n"
        elif self.nama == "Lecalicus":
            if (Robot.jumlah_turn % 4) == 0:
                self.damage = self.damage * 2 
                self.health += 7000
                Robot.terima_aksi(other, self.damage)
                self.damage = 5500
                return f"Lecalicus mendapatkan health tambahan sebesar 7000\n"
            else:
                Robot.terima_aksi(other, self.damage)
                return f"Lecalicus mendapatkan health tambahan sebesar 7000\n"
                
    def terima_aksi(self, damage):
        if damage > self.health:
            self.health=0
            print(f"{self.nama} telah menerima damage sebesar {damage} DMG, sisa health : {self.health} HP")
            print(f"{self.nama} telah mati secara terhormat!")
            Robot.alive = False 
        else:
            self.health += damage
            print(f"{self.nama} telah menerima damage sebesar {damage} DMG dengan sisa health sebesar {self.health} HP")
    
class Antares(Robot):
    def __init__(self):
        super().__init__("Antares", 50000, 5000)

class Alphasetia(Robot):
    def __init__(self):
        super().__init__("Alphasetia", 40000, 6000)

class Lecalicus(Robot):
    def __init__(self):
        super().__init__("Lecalicus", 45000, 5500)

print("Selamat datang di pertandingan robot Yamako")
robot_choice = int(input("Pilih robotmu (1 = Antares, 2 = Alphasetia, 3 = Lecalicus) :  "))
while robot_choice <= 3 and robot_choice > 0:
    if robot_choice == 1:
        robot_saya = Antares()
        robot_choice = 0
    elif robot_choice == 2:
        robot_saya = Alphasetia()
        robot_choice = 0
    elif robot_choice == 3:
        robot_saya = Lecalicus()
        robot_choice = 0
    else : 
        print("Pilihan antara 1, 2, dan 3 saja!")
        robot_choice = int(input("Pilih robotmu (1 = Antares, 2 = Alphasetia, 3 = Lecalicus) :  "))

enemyrobot_choice = int(input("Pilih robot lawan (1 = Antares, 2 = Alphasetia, 3 = Lecalicus) :  "))
while enemyrobot_choice <= 3 and enemyrobot_choice > 0:
    if enemyrobot_choice == 1:
        robot_lawan = Antares()
        enemyrobot_choice = 0
    elif enemyrobot_choice == 2:
        robot_lawan = Alphasetia()
        enemyrobot_choice = 0
    elif enemyrobot_choice == 3:
        robot_lawan = Lecalicus()
        enemyrobot_choice = 0
    else:
        print("Pilihan antara 1, 2, dan 3 saja!")
        enemyrobot_choice = int(input("Pilih robot lawan (1 = Antares, 2 = Alphasetia, 3 = Lecalicus) :  "))
        
print("Selanjutnya, pilih 1 untuk batu, 2 untuk kertas, dan 3 untuk gunting")
while Robot.alive:
    Robot.jumlah_turn += 1 
    print(f"\nTurn saat ini: {Robot.jumlah_turn}")
    print(f"Robotmu ({robot_saya.nama} - {robot_saya.health} HP), robot lawan ({robot_lawan.nama} - {robot_lawan.health} HP)")
    turn_saya = int(input(f"Pilih tangan robotmu ({robot_saya.nama}) : "))
    turn_musuh = int(input(f"Pilih tangan robot lawan ({robot_lawan.nama}) : ")) #random.randint(1,3) 
    print(f"Robot lawan {robot_lawan.nama} memilih : {turn_musuh}")

    if turn_saya == 1:
        if turn_musuh == 1:
            print("Tidak ada yang menang suit!")
        elif turn_musuh == 2:
            print(Robot.lakukan_aksi(robot_lawan, robot_saya))
        elif turn_musuh == 3:
            print(Robot.lakukan_aksi(robot_saya, robot_lawan))
    elif turn_saya == 2:
        if turn_musuh == 1:
            print(Robot.lakukan_aksi(robot_saya, robot_lawan))
        elif turn_musuh == 2:
            print("Tidak ada yang menang suit!")
        elif turn_musuh == 3:
            print(Robot.lakukan_aksi(robot_lawan, robot_saya))
    elif turn_saya == 3:
        if turn_musuh == 1:
            print(Robot.lakukan_aksi(robot_lawan, robot_saya))
        elif turn_musuh == 2:
            print(Robot.lakukan_aksi(robot_saya, robot_lawan))
        elif turn_musuh == 3:
            print("Tidak ada yang menang suit!\n")

print("Pertandingan berakhir!")
