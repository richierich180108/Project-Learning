import os
import shutil
os.system('cls')

target = 'folder_berantakan'
daftar = os.listdir(target)
print(daftar)

for file in daftar:
    nama_depan, ekstensi = os.path.splitext(file)
    if ekstensi != "":
        a = ekstensi[1:]
        b = os.path.join(target, a)
        os.makedirs(b, exist_ok=True)
        c = os.path.join(target, file)
        d = os.path.join(b, file)
        e = shutil.move(c,d)

        
