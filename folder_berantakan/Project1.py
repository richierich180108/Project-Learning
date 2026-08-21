import os
os.system('cls')

target = 'folder_berantakan'
daftar = os.listdir(target)
print(daftar)

for file in daftar:
    nama_depan, ekstensi = os.path.splitext(file)
    if ekstensi == ".jpg":
        a = ekstensi[1:]
        b = os.path.join(target, "gambar")
        os.makedirs(b, exist_ok=True)
        
