#3- Dada uma tupla de nomes de alunos e suas 
# respectivas notas, escreva um programa que 
# imprima o nome do aluno com a maior nota e 
# o nome do aluno com a menor nota.
# alunos = (("João", 8.5), ("Maria", 9.2), ("José", 7.1), ("Ana", 8.7), ("Carlos", 6.5))

# criar a tupla
alunos = (("João", 8.5), ("Maria", 9.2), ("José", 7.1), ("Ana", 8.7), ("Carlos", 6.5))

maior_nota = 0 # maior nota é 0 para que a primeira nota seja sempre maior que 0
menor_nota = 10 # menor nota é 10 para que a primeira nota seja sempre menor que 10
maior_nome = "" # inicializa a variável maior_nome com uma string vazia
menor_nome = ""

for nome, nota in alunos: # percorre a tupla alunos e atribui o nome e a nota a variáveis nome e nota   
    if nota > maior_nota: # verifica se a nota é maior que a maior nota
        maior_nota = nota # se for maior, atribui a nota a maior nota
        maior_nome = nome # pega o nome do aluno com a maior nota
    if nota < menor_nota:
        menor_nota = nota
        menor_nome = nome

print(f"O aluno com a maior nota é, {maior_nome}, com nota, {maior_nota}")
print(f"O aluno com a menor nota é, {menor_nome}, com nota, {menor_nota}")
print("fim do programa!")