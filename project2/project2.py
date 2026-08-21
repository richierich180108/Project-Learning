class karakter:
    def __init__(self,nama,lv,gear):
        self.nama = nama 
        self.lv = lv 
        self.gear = gear 

    def showstat(self):
        print(f'[{self.nama}] - Level {self.lv} | gear: {self.gear}')


char1 = karakter('doctor strange',70, 'CTP of Energy')
char2 = karakter('storm',80, 'Mighty CTP of Rage')
char3 = karakter('ghost rider', 80, 'CTP of Rage')


char1.showstat()
char2.showstat()
char3.showstat()