import os

# Hapus data di hasil.txt
with open('hasil.txt', 'w') as f:
  f.write('')

# Buka file out.txt dan inn.txt
with open('out.txt', 'r') as f1, open('inn.txt', 'r') as f2:
     out = f1.readline()
     inn = f2.readline()

     # Mulai perhitungan
     while out and inn:
          hasil = (float(out) / float(inn)) * 100
          with open('hasil.txt', 'a') as f:
               f.write(str(hasil)+"\n")

          # Baca baris selanjutnya
          out = f1.readline()
          inn = f2.readline()


filename = 'hasil.txt'
os.system(f'start notepad.exe {filename}')