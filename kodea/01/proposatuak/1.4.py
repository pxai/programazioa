pisua = input("Sartu zure pisua: ")
altuera = input("Sartu zure altuera: ")
pisua = int(pisua)
altuera = int(altuera)

emaitza = pisua / (altuera * altuera)

imc = (emaitza * 10000)
print("Zure IMC: ", imcRedondeado)

if imc < 16 :
  print("Beharrezkoa da gehiago jan")
elif imc >= 16 and imc < 25:
  print("Ongi zaude")
elif imc >= 25 and imc < 30:
  print("Gorputz gordinagoa duzu")
else:
  print("Obesitate arazoa daukazu")