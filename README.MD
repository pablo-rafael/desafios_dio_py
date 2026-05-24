# 🚀 Resolução de Desafios: Automação de Processos e pipelines de ETL

> **Coletânea de desafios práticos focados em lógica de negócios, padronização de dados e eficiência empresarial.**

Este repositório reúne a resolução de 4 desafios técnicos projetados para simular cenários reais do dia a dia de uma equipe de tecnologia e engenharia de dados. O objetivo principal do projeto é demonstrar o domínio de estruturas fundamentais do Python para automatizar tomadas de decisão, tratar dados de sistemas legados e construir fluxos de **ETL (Extract, Transform, Load)** de forma escalável, ágil e **sem a dependência de bibliotecas externas**.

---

## 🎯 Objetivo do Projeto
Demonstrar a aplicação prática de conceitos de programação estruturada para resolver problemas de eficiência operacional nas empresas, tais como:
* Redução de erros manuais em faturamentos;
* Automação de regras de compliance e governança de compras;
* Integração e limpeza de dados brutos provenientes de múltiplos setores ou parceiros de negócios.

---

## 💻 Visão Geral dos Módulos Desenvolvidos

### Desafio 1: Automação de Descontos (Módulo Financeiro)
* **Problema:** Calcular o valor final de um pedido aplicando um percentual de desconto variável enviado em uma única linha.
* **Foco Técnico:** Manipulação de tipos numéricos (`float` e `int`), operações matemáticas de precisão e formatação estrita de saída com duas casas decimais utilizando recursos nativos da linguagem.
* **Exemplo de Fluxo:** `150.00 10` ➡️ `135.00`

### Desafio 2: Motor de Decisão de Compras (Módulo de Compliance)
* **Problema:** Classificar automaticamente pedidos de compra entre `aprovado`, `revisao` ou `rejeitado` combinando duas variáveis: o valor financeiro do pedido e o nível de sua prioridade (*alta*, *media*, *baixa*).
* **Foco Técnico:** Construção de árvores de decisão otimizadas através de estruturas condicionais compostas (`if-elif-else`) e operadores lógicos (`and` / `or`).
* **Exemplo de Fluxo:** `1200 alta` ➡️ `revisao`

### Desafio 3: Micro-ETL de Vendas (Módulo de Integração)
* **Problema:** Extrair uma linha de venda bruta enviada por parceiros (contendo produto, quantidade e valor unitário separados por vírgula), calcular o faturamento total daquela linha e carregar em formato legível para os sistemas internos.
* **Foco Técnico:** Pipeline clássico de ETL em miniatura. Uso de `.split()` para extração e tipagem dinâmica para cálculo de regras de negócio.
* **Exemplo de Fluxo:** `caneta,10,2` ➡️ `caneta: 20`

### Desafio 4: Higienização de Dados de Clientes (Módulo de Qualidade de Dados)
* **Problema:** Tratar uma string de nomes contendo ruídos (espaços desnecessários antes e depois de cada termo causados por erros de digitação em sistemas legados), padronizá-los em caixa alta e mudar o caractere delimitador.
* **Foco Técnico:** Limpeza de strings (*Data Cleansing*). Manipulação avançada de listas e funções de texto nativas como `.strip()`, `.upper()` e `"; ".join()`.
* **Exemplo de Fluxo:** `lucas , maria ,joao` ➡️ `LUCAS; MARIA; JOAO`

---

## 🛠️ Tecnologias Utilizadas
* **Python 3**: Utilizado como linguagem exclusiva do ecossistema.
* **Recursos Nativos**: O projeto abdica intencionalmente do uso de frameworks ou pacotes externos (como Pandas ou NumPy) para evidenciar a proficiência em lógica pura, manipulação de strings, controle de fluxo e gerenciamento de memória em scripts leves de alta performance.

---

## 🚀 Como Executar e Testar os Scripts

1. Clone este repositório para a sua máquina local:
   ```bash
   git clone [https://github.com/pablo-rafael/desafios_dio_py.git](https://github.com/pablo-rafael/desafios_dio_py.git)
```

---

## Certifique-se de ter o Python 3 instalado no seu ambiente.

Para testar qualquer um dos módulos, execute o arquivo correspondente via terminal (passando a entrada esperada pelo console):
```
Bash
python nome_do_desafio.py
```
Se você gostou da abordagem limpa e da estrutura lógica utilizada para resolver estes problemas de automação, fique à vontade para deixar uma ⭐️ no repositório! feedbacks e conexões sobre arquitetura de dados são sempre bem-vindos! 🚀