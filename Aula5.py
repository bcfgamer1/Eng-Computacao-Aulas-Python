# Listas
carros = ["Accord", "Polo", "Civic", "Fiat Uno"]
print(carros)
# contagem de quantidade "len"
print(len(carros))
# contagem de indices e aparecer listados porem tudo começa no 0 "[0]"
print(carros[1])
print(carros[2])
print(carros[3])
carros[0] = "Jetta"
print(carros[0])

# notas = [6,7,5,8,9]
# soma = 0
# x = 0
# while x < len(notas):
#     soma += notas [x]
#     x += 1
# print(f"Média = {(soma/x):.2f}")
#
# notas = [0,0,0,0,0]
# soma = 0
# x = 0
# while x < len(notas):
#     notas[x] = float(input(f"Nota {x+1} ="))
#     soma += notas[x]
#     x += 1
# print(f"Média = {(soma/x):.2f}")

carros_back = carros
print(carros_back)
carros[3] = "Jeep"
print(carros)

carros_back = carros[:]
print(carros_back)
carros[1] = "Golf"
print(carros)
print(carros_back)