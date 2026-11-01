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

def cari_catatan(identitas):
    kumpulan_c = Kumpulan_catatan
    for i in kumpulan_c:
        if i['id'] == identitas['id']:
            return i
        else:
            raise NameError('coba lagi')
     


    
subject1 = buat_catatan('mtk','pythagoras','relasi segitiga')
buat_catatan('fisika','energi dan gaya','memahami bagaimana gaya dan energi bekerja')
buat_catatan('coding','variabel','bagaimana sebuah variabel itu bekerja ')
print(subject1['id'])

#print(Kumpulan_catatan)
print(cari_catatan(subject1))
