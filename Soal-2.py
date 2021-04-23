#menghitung luasan dengan diberikan input nilai jari-jari
radius = float(input("Masukkan jari-jari : "))
area = float(22 / 7 * radius ** 2)

r = float(radius)
a = float(area)

print(a)
txt = "Luas lingkaran dengan jari-jari  {} cm adalah {:.2f} cm\u00b2".format(r,a)
print(txt)

# print("%.2f" % area)
#area = 22/7*r^2

#print("Luas Lingkaran adalah {}cm\u00b2".format(area))
#print("%.2f" % area) untuk mebulatkan 2 angka dibelakang desimal tipe data float

#print (area)
#print ("Luas lingkaran dengan Jari-jari " + area)
#print("\uob2") ini adalah cara menampilkan atau mencetak kuadrat 2 