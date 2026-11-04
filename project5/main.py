import os
os.system('cls')
try:
    hasil = 10 / 0
except ZeroDivisionError:
    print('tidak bisa dibagi nol')
print('program masih berjalan')