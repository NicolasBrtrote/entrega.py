import numpy as np 


tipo_dados = [('data', 'U20'), ('regiao', 'U10'), ('produto', 'U10'),
              ('quantidade_vendida', 'i4'), ('preco_unitario', 'f4'), ('valor_total', 'f4')]


dados_vendas = np.genfromtxt('vendas.csv', delimiter=',', dtype=tipo_dados, skip_header=1)

# Calcular media mediana desvio padrao
media_total_vendas = np.mean(dados_vendas['valor_total'])
mediana_total_vendas = np.median(dados_vendas['valor_total'])
desvio_padrao_total_vendas = np.std(dados_vendas['valor_total'])

# Produto com a maior quantidade vendida e maior valor total de vendas
produto_mais_vendido = dados_vendas['produto'][np.argmax(dados_vendas['quantidade_vendida'])]
quantidade_mais_vendida = np.max(dados_vendas['quantidade_vendida'])

produto_mais_valioso = dados_vendas['produto'][np.argmax(dados_vendas['valor_total'])]
valor_total_mais_vendido = np.max(dados_vendas['valor_total'])

# Valor total de vendas por região
regioes_distintas = np.unique(dados_vendas['regiao'])
total_vendas_por_regiao = np.zeros(len(regioes_distintas))
np.add.at(total_vendas_por_regiao, np.searchsorted(regioes_distintas, dados_vendas['regiao']), dados_vendas['valor_total'])

# Venda media por dia
datas_distintas = np.unique(dados_vendas['data'])
media_vendas_diarias = [np.sum(dados_vendas['valor_total'][dados_vendas['data'] == data]) for data in datas_distintas]
media_venda_diaria = np.mean(media_vendas_diarias)

# dia da semana com maior numero de vendas
dias_semana = np.array([np.datetime64(data).astype('datetime64[D]').view('int') % 7 for data in dados_vendas['data']])
vendas_por_dia_semana = np.bincount(dias_semana, weights=dados_vendas['valor_total'], minlength=7)
dia_com_maior_venda = np.argmax(vendas_por_dia_semana)

# calcula variacao de valor por dia
dados_ordenados = np.sort(dados_vendas, order='data')
datas_ordenadas = np.unique(dados_ordenados['data'])
total_vendas_por_dia = [np.sum(dados_ordenados['valor_total'][dados_ordenados['data'] == data]) for data in datas_ordenadas]
variacao_vendas_por_dia = np.diff(total_vendas_por_dia)


nomes_dias_semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']
