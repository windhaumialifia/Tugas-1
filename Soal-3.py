Teori = input("Masukkan Nilai Ujian Teori : ")
Praktek = input("Masukkan Nilai Ujian Praktek : ")

T = float(Teori)
P = float(Praktek)

if T > 70 and P > 70 :
    print("Selamat, anda lulus")
elif T >= 70 and P < 70 :
    print(str("Anda harus mengulang ujian praktek."))
elif T < 70 and P <= 70 :
    print(str("Anda harus mengulang ujian teori"))
else :
    print(str("Anda harus mengulang ujian teori dan praktek"))