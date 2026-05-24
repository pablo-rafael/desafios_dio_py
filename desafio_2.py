# Recebe a entrada do usuário (valor e prioridade)
entrada = input().strip()
valor_str, prioridade = entrada.split()
valor = int(valor_str)

# TODO: Implemente a lógica condicional para decidir entre "aprovado", "revisao" ou "rejeitado" conforme as regras do desafio.

# REGRA 1: Valor até 1000 e prioridade alta ou media -> aprovado
if valor <= 1000 and (prioridade == 'alta' or prioridade == 'media'):
    print('aprovado')

# REGRA 2: Valor acima de 1000 e prioridade alta -> revisao
elif valor > 1000 and prioridade == 'alta':
    print('revisao')

# REGRA 3: Qualquer outra combinação -> rejeitado
else:
    print('rejeitado')