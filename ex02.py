# 2 - verifique se um determinado elemento esta contido
# na tupla ('a','b',1,2,'c',3,4,'d',5) 

# criar a tupla
t1 = ('a','b',1,2,'c',3,4,'d',5)
# criar o elemento a ser verificado
elemento = 'd'

if elemento in t1: # verifica se o elemento está contido na tupla t1 
  print(f"o {elemento} existe!") # imprime a mensagem se o elemento estiver contido na tupla t1

else: # se o elemento não estiver contido na tupla t1 
  print(f"o {elemento} não existe!") # imprime a mensagem se o elemento não estiver contido na tupla t1
  
############
# outra forma de fazer a mesma coisa é usando o método count da classe tuple
# o método count retorna a quantidade de vezes que o elemento aparece na tupla
if t1.count(elemento) > 0: # verifica se o elemento está contido na tupla t1
  print(f"o {elemento} existe!")  # imprime a mensagem se o elemento estiver contido na tupla t1
  print(f"existe {t1.count(elemento)}")  # imprime a quantidade de vezes que o elemento aparece na tupla t1

else: # se o elemento não estiver contido na tupla t1 
  print(f"o {elemento} não existe!") # imprime a mensagem se o elemento não estiver contido na tupla t1