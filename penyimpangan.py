import os

# Hapus data di hasil.txt
with open('penyimpangan/hasil.txt', 'w') as f:
  f.write('')

# Buka file kalkulator.txt dan arduino.txt
with open('penyimpangan/kalkulator.txt', 'r') as f1, open('penyimpangan/arduino.txt', 'r') as f2:
     kalkulator = f1.readline()
     arduino = f2.readline()

     # Mulai perhitungan
     while kalkulator and arduino:
          hasil = (((float(kalkulator) - float(arduino)) / float(kalkulator)) * 100)
          with open('penyimpangan/hasil.txt', 'a') as f:
               f.write(str(hasil)+"\n")

          # Baca baris selanjutnya
          kalkulator = f1.readline()
          arduino = f2.readline()


filename = 'penyimpangan/hasil.txt'
os.system(f'start notepad.exe {filename}')