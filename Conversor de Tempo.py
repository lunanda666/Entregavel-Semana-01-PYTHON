tempo = int(input())  # recebe o tempo em segundos

horas = tempo // 3600  # calcula quantas horas cabem no tempo

tempo = tempo % 3600  # pega o que sobrou depois das horas

minutos = tempo // 60  # calcula quantos minutos cabem no restante

segundos = tempo % 60  # pega o que sobrou depois dos minutos

print(f"{horas}:{minutos}:{segundos}")  # mostra o tempo no formato horas:minutos:segundos