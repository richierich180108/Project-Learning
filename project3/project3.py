import os 
os.system('cls')


with open('data.txt','r') as file:
    baris = file.readlines()
    b = []
    for bbaris in baris:
        a = bbaris.strip()
        dat = int(a)
        b.append(dat)

total = sum(b)
banyak = len(b)
avg = total/banyak
terbesar = max(b)


with open('laporan.txt','w') as fil:
    fil.write('\n===Hasil Analisis Data===\n')
    fil.write(f'total data yang diolah: {banyak} baris\n')
    fil.write(f'total keseluruhan {total}\n')
    fil.write(f'Rata-Rata {avg}\n')
    fil.write(f'nilai tertinggi {terbesar}\n')
    fil.write('===\n')

print("\n[INFO] Laporan berhasil diekspor ke 'laporan.txt'!")

