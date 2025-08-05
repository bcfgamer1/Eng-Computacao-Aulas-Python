

nomes_alunos = []
print(len(nomes_alunos))

nomes_alunos.append("Heitor")
print(nomes_alunos)
nomes_alunos.append("Busa")
print(nomes_alunos)
nomes_alunos.append("Marcos")
print(nomes_alunos)
nomes_alunos.sort()
print(nomes_alunos)
nomes_alunos.sort(reverse=True)
print(nomes_alunos)


L = []
while True:
    nome_alunos = (input("Digite um nome (Heitor sai):"))
    if nome_alunos == "Heitor":
        break
    L.append(nome_alunos)
x = 0
while x < len (L):
    print(L[x])
    x += 1




