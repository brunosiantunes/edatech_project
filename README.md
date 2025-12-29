# 📊 Sistema de Análise de Vendas - TechStore

Este projeto é um script em Python desenvolvido para realizar uma Análise Exploratória de Dados (EDA) sobre um histórico de vendas. O sistema processa um arquivo CSV, realiza cálculos de negócio e exibe insights estratégicos diretamente no terminal.

## 🚀 Funcionalidades

O sistema carrega os dados brutos e responde automaticamente às seguintes questões de negócio:

* **Visão Geral:** Exibição das primeiras linhas e contagem total de registros.
* **KPIs Financeiros:** Cálculo da Receita Total da empresa.
* **Filtragem de Dados:** Identificação de vendas específicas (ex: Categoria "Eletrônicos").
* **Análise de Produto:** Identificação do produto mais vendido (em quantidade).
* **Análise Regional:** Identificação da região com maior faturamento.
* **Relatórios Cruzados:** Geração de Tabela Dinâmica (Pivot Table) de Receita por Região vs. Categoria.

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**: Linguagem principal.
* **Pandas**: Biblioteca para manipulação e análise de dados de alta performance.

## 📂 Estrutura do Projeto

```text
/
├── data_project.py    # Script principal com a lógica de análise
├── vendas.csv           # Base de dados (input)
└── README.md            # Documentação do projeto

```

## ⚙️ Pré-requisitos e Instalação

1. **Python**: Certifique-se de ter o Python instalado.
2. **Dependências**: Instale a biblioteca `pandas`:

```bash
pip install pandas

```

## ▶️ Como Executar

1. Certifique-se de que o arquivo `vendas.csv` está no mesmo diretório do script.
2. Execute o arquivo Python via terminal:

```bash
python data_project.py

```

## 🖥️ Exemplo de Saída (Terminal)

Ao executar o script, você verá um relatório semelhante a este:

```text
--- Informações Básicas ---
Primeiras 5 linhas:
(Exibição das linhas...)

Número total de registros: 100
Receita Total da TechStore: R$ 845,852.00
------------------------------

--- Consultas de Negócio ---
Total de vendas em Eletrônicos: 28
Produto mais vendido (qtd): Sofá Q (30 unidades)
Região com maior receita: Sudeste (R$ 245,605.00)

--- Tabela Dinâmica (Receita: Região x Categoria) ---
categoria     Eletrônicos   Móveis    Periféricos
regiao                                           
Centro-Oeste  R$ 39.546,00  R$ 44.884,00  R$ 25.192,00  R$ 24.106,00
Nordeste      R$ 51.890,00  R$ 22.870,00  R$ 24.383,00  R$ 52.659,00
...

```

## 📝 Autor

Desenvolvido para fins de estudo em Análise de Dados com Python.

```

