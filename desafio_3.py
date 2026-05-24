# Leitura da linha de entrada
entrada = input().strip().split(',')

# TODO: Separe os campos da entrada e calcule o valor total da venda (quantidade * valor unitário)
# Dica: Use split(',') para separar os valores e int() para converter para inteiro

produto = entrada[0]
quantidade_in = entrada[1]
valor_un_in = entrada[2]

quantidade = int(quantidade_in)
valor_un = int(valor_un_in)

total = quantidade * valor_un

# print(f"{produto}: {total}")  # Exemplo de saída formatada
print(f"{produto}: {total}")