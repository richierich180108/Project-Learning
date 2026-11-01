import os
import uuid
os.system('cls')

Kumpulan_catatan = []

def buat_catatan(kategori,topik,isi):
    c1 = {
    'kategori':kategori,
    'topik':topik,
    'isi':isi,
    'id': str(uuid.uuid4())
    }

    Kumpulan_catatan.append(c1)

    return Kumpulan_catatan

def cari_catatan(materi):
    materi = Kumpulan_catatan
    if materi == Kumpulan_catatan:
        print(materi)
    else:
        print('id tidak ditemukan')
    return materi

    
buat_catatan('mtk','pythagoras','relasi segitiga')
buat_catatan('fisika','energi dan gaya','memahami bagaimana gaya dan energi bekerja')
buat_catatan('coding','variabel','bagaimana sebuah variabel itu bekerja ')

print(Kumpulan_catatan)
#cari_catatan('fisika')
