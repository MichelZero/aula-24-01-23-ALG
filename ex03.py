#3- Dada uma tupla de nomes de alunos e suas 
# respectivas notas, escreva um programa que 
# imprima o nome do aluno com a maior nota e 
# o nome do aluno com a menor nota.
# alunos = (("João", 8.5), ("Maria", 9.2), ("José", 7.1), ("Ana", 8.7), ("Carlos", 6.5))

maior_nota = 0
menor_nota = 10
maior_nome = ""
menor_nome = ""

for nome, nota in alunos:
    if nota > maior_nota:
        maior_nota = nota
        maior_nome = nome
    if nota < menor_nota:
        menor_nota = nota
        menor_nome = nome

print("O aluno com a maior nota é", maior_nome, "com nota", maior_nota)
print("O aluno com a menor nota é", menor_nome, "com nota", menor_nota)