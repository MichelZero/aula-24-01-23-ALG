# 2 - verifique se um determinado elemento esta contido
# na tupla ('a','b',1,2,'c',3,4,'d',5) 

t1 = ('a','b',1,2,'c',3,4,'d',5)
elemento = 'd'
if elemento in t1:
  print(f"o {elemento} existe!")

else:
  print(f"o {elemento} não existe!")
  
############

if t1.count(elemento) > 0:
  print(f"o {elemento} existe!")
  print(f"existe {t1.count(elemento)}")

else:
  print(f"o {elemento} não existe!")