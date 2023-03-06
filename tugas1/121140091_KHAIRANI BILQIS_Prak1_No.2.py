print("============================================")
print("Nama  : KHAIRANI BILQIS")
print("NIM   : 121140091")
print("Kelas : RB")
print("============================================")
print("~~               LOGIN AKUN               ~~")
print("============================================")

username ="informatika"
password ="12345678"
#fungsi login
def login (user_name,pass_word):
    if user_name != username or pass_word != password:
        print("Username atau Password salah coba lagi!")
        print()
    else:
        print()
        print("=========== ~~ LOGIN BERHASIL ~~ ===========")
        exit()

#syarat login
for i in range (0,3):
    username_=input("Username Anda : ")
    password_=input("Password Anda : ")
    login (username_, password_)

print("=========== !! AKUN TERBLOKIR !! ===========")
