Teori = input("Masukkan Nilai Ujian Teori : ")
Praktek = input("Masukkan Nilai Ujian Praktek : ")

T = float(Teori)
P = float(Praktek)

if T < 70 and P < 70 :
    print("Anda mengulang ujian teori dan ujian praktek")

elif T < 70 and P <= 70 :
    print("Anda harus mengulang ujian teori")
    
elif T >= 70 and P < 70 :
    print("Anda harus mengulang ujian praktek.")

else :
    print("Selamat, anda lulus!")
