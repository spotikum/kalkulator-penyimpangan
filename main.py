while True:
     kalkulator = float(input("Kalkulator : "))
     arduino = float(input("Arduino : "))
     persentase = 100
     hasil = ((kalkulator - arduino) / kalkulator) * persentase
     print(hasil)