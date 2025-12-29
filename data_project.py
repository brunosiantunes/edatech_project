import pandas as pd

# Carregando dados

try:
    df = pd.read_csv('vendas.csv')
    print("Arquivo carregado com sucesso!\n")
except FileNotFoundError:
    print("Arquivo não encontrado!")
    df = pd.DataFrame()


if df.empty:
    print("DataFrame está vazio, tente novamente.")
    exit()
else:
    print("DataFrame carregado com sucesso, iniciando análises...\n")
# iniciando bloco de informações básicas
    print("--- Informações Básicas ---")

    print("Primeiras 5 linhas:")
    print(df.head())

    print(f"\nNúmero total de registros: {len(df)}") # numero de linhas

    df['receita_total'] = df['quantidade'] * df['preco_unitario'] # criação de coluna para gerar a receita total com quantidade x preço unitário

    total_receita = df['receita_total'].sum()
    print(f"Receita Total da Empresa: R$ {total_receita:,.2f}")


# Bloco de consultas específicas
    print("--- Informações Específicas ---")
# Filtrando e exigindo vendas da categoria "Eletrônicos"

    vendas_eletronicos = df[df['categoria'] == 'Eletrônicos']
    print(f"\nTotal de vendas de Eletrônicos: {len(vendas_eletronicos)}")

# Identificando e exibindo o produto mais vendido em quantidade
    produto_top = df.groupby('produto')['quantidade'].sum().idxmax()
    print(f"Produto mais vendido da loja: {produto_top}")

# Descobrindo e exibindo a região com maior valor de compras.
    regiao_top = df.groupby('regiao')['receita_total'].sum().idxmax()
    print(f"Região com maior faturamento: {regiao_top}")

