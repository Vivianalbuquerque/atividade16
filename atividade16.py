# Exercício Python 16: Para ter acesso a fila de prioridade, você deve ser idoso, gestante ou cadeirante. 
# Escreva um programa que pergunta a situação do usuário 
# (se é idoso, se é gestante, se é cadeirante ou nenhum destes) 
# e diga se ele pode ter acesso a fila prioridade ou não.
pri = str(input("qual a sua situação entre cadeirante, gestante ou idoso ?"))
if pri == "cadeirante" or pri == "gestante" or pri =="idoso":
    print("você tem prioridade")
else:
    print("você não tem prioridade")