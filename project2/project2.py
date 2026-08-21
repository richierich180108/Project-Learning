class karakter:
    def __init__(self,nama,lv,gear):
        self.nama = nama 
        self.lv = lv 
        self.gear = gear 

    def showstat(self):
        print(f'[{self.nama}] - Level {self.lv} | gear: {self.gear}')


class roster:
    def __init__(self):
        self.daftarchar = []

    def tambahchar(self, karakterbaru):
        self.daftarchar.append(karakterbaru)
        print(f'Berhasil menambahkan {karakterbaru.nama} ke dalam roster!')

    def tampilkansemua(self):
        print('\n=== DAFTAR ROSTER MFF===')
        print(f'total karakter adalah {len(self.daftarchar)}')
        for kar in self.daftarchar:
            kar.showstat(   )
        print('================\n')



char1 = karakter("Doctor Strange", 80, "CTP of Rage")
char2 = karakter("Spider-Man", 70, "CTP of Authority")
char3 = karakter("Loki", 80, "CTP of Energy")
r = roster()
r.tambahchar(char1)
r.tambahchar(char2)
r.tambahchar(char3)

r.tampilkansemua()

#eval 
'''
1. pahamin ulang tentang oop 
2. lebih sering membaca secara detail
'''

