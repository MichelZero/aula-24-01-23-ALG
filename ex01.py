# 1- gere tupla dinamicamente de tamanho 5, 
# de tamanho aleatório entre 1 e 20;

# gerar valores dinamicamente usando range
t1 = range(5) 
print(t1) # range(0, 5)


# importa a classe Random, e usar o randint
# import random  # importa a classe Random do módulo random
from random import randint # importa a função randint do módulo random 

# gerar tupla dinamicamente
t1 = tuple(range(5)) # gera uma tupla de tamanho 5 com valores de 0 a 4
print(t1) # (0, 1, 2, 3, 4)

t1 = tuple(range(randint(1,10))) # gera uma tupla de tamanho aleatório entre 1 e 10
print(t1) 

t2 = tuple(randint(1,10) for i in range(5)) # gera uma tupla de tamanho 5 com valores aleatórios entre 1 e 10
print(t2) 

print("fim do programa!")