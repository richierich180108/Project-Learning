import os
os.system('cls')

target = 'folder_berantakan'
daftar = os.listdir(target)
print(daftar)

for file in daftar:
    nama_depan, ekstensi = os.path.splitext(file)
    if file == ".jpg":
        ekstensi[1:]
        #os.path.join(target, "gambar")
        print(ekstensi)
print(file)
