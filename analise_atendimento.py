import pandas as pd

dados = pd.read_csv("tempo_atendimento.csv")

media = dados["tempo"].mean()
maximo = dados["tempo"].max()
minimo = dados["tempo"].min()

print("Tempo médio de atendimento:", media)
print("Tempo máximo:", maximo)
print("Tempo mínimo:", minimo)

if media > 7:
    print("O processo precisa de melhoria.")
else:
    print("Processo dentro do esperado.")
