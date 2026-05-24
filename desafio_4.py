# Lê a linha de entrada contendo nomes separados por vírgula e espaço
entrada = input()

# TODO: Para cada nome, remova espaços extras e transforme em maiúsculas
nomes_in = entrada.split(',')
nomes_cl = []

# Dica: Use split(',') para separar os nomes e depois aplique strip() e upper() em cada um
for nome in nomes_in:
  nomes_end = nome.strip().upper()
  nomes_cl.append(nomes_end)

# Exemplo de saída esperada: 'ANA; BRUNO; CARLA'
result = '; '.join(nomes_cl)

print(result)