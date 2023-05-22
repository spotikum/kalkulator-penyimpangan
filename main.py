with open('kalkulator.txt', 'r') as f1, open('arduino.txt', 'r') as f2:
     line1 = f1.readline()
     line2 = f2.readline()
     while line1 and line2:
          hasil = (float(line1) + float(line2))
          with open('hasil.txt', 'a') as f:
               f.write(str(hasil)+"\n")

          line1 = f1.readline()
          line2 = f2.readline()



# while True:
#      kalkulator = float(input("Kalkulator : "))
#      arduino = float(input("Arduino : "))
#      persentase = 100
#      hasil = ((kalkulator - arduino) / kalkulator) * persentase
#      print(hasil)