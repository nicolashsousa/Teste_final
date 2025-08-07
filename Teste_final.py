#Problema1
#Parte1
notas_fulano = [9, 8, 7]
#Parte2
media = sum(notas_fulano) / len(notas_fulano)
print("Média:", media)
#Parte3
def calcular_media(notas):
    return sum(notas) / len(notas)
#Parte4
notas1 = [9.0, 8.0, 7.0]
notas2 = [6.0, 7.0, 8.0]
notas3 = [10.0, 9.0, 8.0]
notas4 = [5.0, 6.0, 7.0]
notas5 = [8.0, 9.0, 7.0]
print("Média 1º aluno:", calcular_media(notas1))
print("Média 2º aluno:", calcular_media(notas2))
print("Média 3º aluno:", calcular_media(notas3))
print("Média 4º aluno:", calcular_media(notas4))
print("Média 5º aluno:", calcular_media(notas5))
#Parte5
notas_1 = []
notas_2 = []
for i in range(3):
    nota = float(input(f"Digite a nota: "))
    notas_1.append(nota)
for i in range(3):
    nota = float(input(f"Digite a nota: "))
    notas_2.append(nota)
print("Média 1º aluno::", calcular_media(notas_1))
print("Média 2º aluno::", calcular_media(notas_2))
#Parte6
notas = []
entradas = input("Digite as notas(separadas por espaço):").split(" ")
notas = [float(i) for i in entradas]
print(notas)
#Problema2
#Parte1
temperaturas_semana = [22.0, 24.0, 19.0, 21.0, 23.0, 20.0, 18.0] 
#Parte2
media_semanal = sum(temperaturas_semana) / len(temperaturas_semana)
print("Média semanal:", media_semanal)
#Parte3
def calcular_media_temperaturas(temperaturas):
    return sum(temperaturas) / len(temperaturas)
#Parte4
cidade1 = [22.0, 24.0, 19.0, 21.0, 23.0, 20.0, 18.0]
cidade2 = [25.0, 26.0, 24.0, 23.0, 22.0, 21.0, 20.0]
cidade3 = [15.0, 16.0, 14.0, 13.0, 12.0, 11.0, 10.0]
print("Média Cidade 1:", calcular_media_temperaturas(cidade1))
print("Média Cidade 2:", calcular_media_temperaturas(cidade2))
print("Média Cidade 3:", calcular_media_temperaturas(cidade3))  
#Parte5
cidade = []
temperaturas = list(map(float, input("Digite as temperaturas(separadas por espaço): ").split()))
cidade = [float(i) for i in temperaturas] 
print(cidade)
#Problema3
#Parte1
tempos_piloto_joão = [14, 13, 12]
#Parte2 sem min()
def menor_tempo(tempos):
    if tempos[0] < tempos[1] and tempos[0] < tempos[2]:
        return tempos[0]
    elif tempos[1] < tempos[0] and tempos[1] < tempos[2]:
        return tempos[1]
    else:
        return tempos[2]
print("Menor tempo:", menor_tempo(tempos_piloto_joão))
#Parte3
def melhor_volta(tempos):
    return min(tempos)
print("Melhor volta:", melhor_volta(tempos_piloto_joão), "segundos")
#Parte4
tempos_piloto1 = [14, 13, 12]
tempos_piloto2 = [15, 14, 13]
tempos_piloto3 = [16, 15, 14]
tempos_piloto4 = [17, 16, 15]
tempos_piloto5 = [18, 17, 16]
print("Piloto 1:", melhor_volta(tempos_piloto1), "segundos")
print("Piloto 2:", melhor_volta(tempos_piloto2), "segundos")
print("Piloto 3:", melhor_volta(tempos_piloto3), "segundos")
print("Piloto 4:", melhor_volta(tempos_piloto4), "segundos")    
print("Piloto 5:", melhor_volta(tempos_piloto5), "segundos")
#Parte5
tempos = []
voltas = list(map(float, input("Digite as voltas(separadas por espaço): ").split()))
tempos = [float(i) for i in voltas]
print("Melhor volta:", melhor_volta(tempos))
#Parte6
tempos_piloto1 = [14, 13, 12]
tempos_piloto2 = [15, 14, 13]
tempos_piloto3 = [16, 15, 14]
tempos_piloto4 = [17, 16, 15]
tempos_piloto5 = [18, 17, 16]
def tempo_total(tempos):
    return sum(tempos)
print(f'Piloto 1: {melhor_volta(tempos_piloto1)} segundos, Tempo total: {tempo_total(tempos_piloto1)} segundos')
print(f'Piloto 2: {melhor_volta(tempos_piloto2)} segundos, Tempo total: {tempo_total(tempos_piloto2)} segundos')
print(f'Piloto 3: {melhor_volta(tempos_piloto3)} segundos, Tempo total: {tempo_total(tempos_piloto3)} segundos')
print(f'Piloto 4: {melhor_volta(tempos_piloto4)} segundos, Tempo total: {tempo_total(tempos_piloto4)} segundos')
print(f'Piloto 5: {melhor_volta(tempos_piloto5)} segundos, Tempo total: {tempo_total(tempos_piloto5)} segundos')
#Problema4
#Parte1
posicao = []
#Parte2
posicao.append(0)
posicao.append(0)
#Parte3
def mover_para_cima():
    posicao[1] += 1
#Parte4
def mover_para_baixo():
    posicao[1] -= 1
def mover_para_esquerda():
    posicao[0] -= 1
def mover_para_direita():
    posicao[0] += 1
#Parte5
def mostrar_posicao():
    print(f"Posição atual: ({posicao[0]},{posicao[1]})")
mover_para_cima()
mover_para_cima()
mover_para_direita()
mostrar_posicao()
#Problema5
#Parte1
amostras = [8.0, 5.5, 7.5, 12.0, 11.5, 13.0] 
#Parte2
amostra_irregular = 0
for i in range(len(amostras)):
    if amostras[i] <8 or amostras[i]> 12.0:
        amostra_irregular += 1
print(f'Amostras irregulares:", {amostra_irregular} irregulares')
#Parte3
def contar_irregulares(amostras):
    amostra_irregular = 0
    for amostra in amostras:
        if amostra < 8 or amostra > 12.0:
            amostra_irregular += 1
    return amostra_irregular
print("Amostras irregulares:", contar_irregulares(amostras))
#Parte4
amostras1 = [8.0, 5.5, 7.5, 12.0, 11.5, 13.0]
amostras2 = [9.0, 10.0, 11.0, 12.0, 13.0, 14.0]
amostras3 = [6.0, 7.0, 8.0, 9.0, 10.0, 11.0]
print(f'Amostras irregulares 1:", {contar_irregulares(amostras1)} irregulares')
print(f'Amostras irregulares 2:", {contar_irregulares(amostras2)} irregulares')
print(f'Amostras irregulares 3:", {contar_irregulares(amostras3)} irregulares')
amostras4 = []
teste = list(map(float, input("Digite os valores(separadas por espaço): ").split()))
amostras4 = [float(i) for i in teste]
print("Amostras irregulares 4:", contar_irregulares(amostras4))