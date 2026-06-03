votos=[0, 0, 0]
for i in range(10):
    voto=int(input("Ingrese su voto (1, 2 o 3): "))
    if voto in [1, 2, 3]:
        votos[voto-1] += 1
ganador=votos.index(max(votos)) + 1
print("El ganador es el candidato", ganador)