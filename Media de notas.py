def media(a, b, c):     # cria uma função que recebe três notas
    return (a + b + c) / 3

notas = [8, 6, 10]

# O * separa os valores da lista e envia cada um como argumento
# Equivale a: media(8, 6, 10)

print(media(*notas))  # 8.0 

dados = {         # Cria um dicionário com as notas 
    "a": 8,
    "b": 6,
    "c": 10
}

print(media(**dados))  # 8.0