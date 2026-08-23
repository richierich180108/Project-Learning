import os 
os.system('cls')
while True:

    print("=== 💰 FINANCE TRACKER ===")
    print("1. Catat Transaksi")
    print("2. Cek Sisa Saldo")
    print("3. Keluar")
    print("==========================")
    
    pilihan = input("Pilih menu (1/2/3): ")
    if pilihan == '1':
        a = int(input('masukkan nominal: '))
        b = input('keterangan transaksi: ')
        with open('keuangan.txt','a') as k:
            k.write(f'{a},{b}\n')
        input('tekan enter untuk kembali ke menu')
    elif pilihan == '2':
        saldo = 0  
        with open('keuangan.txt','r') as l:
            baca = l.readlines()
            for data in baca:
                c = data.strip()
                f = c.split(',')
                nominal = f[0]
                saldo += int(nominal)
        print(f'saldo saat ini adalah: Rp.{saldo}')
        input('tekan enter untuk kembali ke menu')
    else:
        break
