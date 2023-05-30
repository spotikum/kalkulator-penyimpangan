import os

# Hapus data di hasil.txt
with open('hasil.txt', 'w') as f:
  f.write('')

# Buka file bilangan.txt dan pengali.txt
with open('bilangan.txt', 'r') as f1, open('pengali.txt', 'r') as f2:
     bilangan = f1.readline()
     pengali = f2.readline()

     # Mulai perhitungan
     while bilangan and pengali:
          hasil = float(bilangan) * float(pengali)
          with open('hasil.txt', 'a') as f:
               f.write(str(hasil)+"\n")

          # Baca baris selanjutnya
          bilangan = f1.readline()
          pengali = f2.readline()


filename = 'hasil.txt'
os.system(f'start notepad.exe {filename}')