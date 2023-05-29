import os

# Hapus data di hasil.txt
with open('perkalian/hasil.txt', 'w') as f:
  f.write('')

# Buka file kalkulator.txt dan arduino.txt
with open('perkalian/bilangan.txt', 'r') as f1, open('perkalian/pengali.txt', 'r') as f2:
     kalkulator = f1.readline()
     arduino = f2.readline()

     # Mulai perhitungan
     while kalkulator and arduino:
          hasil = float(kalkulator) * float(arduino)
          with open('perkalian/hasil.txt', 'a') as f:
               f.write(str(hasil)+"\n")

          # Baca baris selanjutnya
          kalkulator = f1.readline()
          arduino = f2.readline()


filename = 'perkalian/hasil.txt'
os.system(f'start notepad.exe {filename}')