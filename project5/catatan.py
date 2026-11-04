import os
import uuid
os.system('cls')

Kumpulan_catatan = []

def buat_catatan(kategori:str,topik:str,isi:str):
    c1 = {
    'kategori':kategori,
    'topik':topik,
    'isi':isi,
    'id': str(uuid.uuid4())
    }

    Kumpulan_catatan.append(c1)

    return c1

def cari_catatan(identitas:str):
    kumpulan_c = Kumpulan_catatan
    for i in kumpulan_c:
        if i['id'] == identitas:
            return i
    raise NameError('coba lagi') 


    
subject1 = buat_catatan('mtk','pythagoras','relasi segitiga')
subject2 = buat_catatan('fisika','energi dan gaya','memahami bagaimana gaya dan energi bekerja')
subject3 = buat_catatan('coding','variabel','bagaimana sebuah variabel itu bekerja ')
print(Kumpulan_catatan)

try:
    teks = input('masukkan id: ')
    print(cari_catatan(teks))
except NameError:
    print('salah id, coba lagi')
print('program masih berjalan')