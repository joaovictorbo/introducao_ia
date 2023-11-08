import pandas as pd
import numpy as np

# Criando um DataFrame com as informações dadas



renda_aleatoria = [np.random.randint(1550, 8750) for _ in range(3000)]
pontuacao_aleatoria = [np.random.randint(1, 100) for _ in range(3000)]
historico_aleatorio = [np.random.randint(100, 300) for _ in range(3000)]
limite_de_credito = [np.random.randint(400, 10000) for _ in range(3000)]
qtdfilho = [np.random.randint(0, 3) for _ in range(3000)]
renda_aleatoria.sort()
limite_de_credito.sort()
renda_aleatoria = pd.DataFrame(renda_aleatoria)
pontuacao_aleatoria = pd.DataFrame(pontuacao_aleatoria)
historico_aleatorio = pd.DataFrame(historico_aleatorio)
limite_de_credito = pd.DataFrame(limite_de_credito)
qtdfilho = pd.DataFrame(qtdfilho)

# Concatenando os valores aleatórios com o DataFrame original
df = pd.concat([renda_aleatoria, pontuacao_aleatoria, historico_aleatorio, limite_de_credito, qtdfilho], axis=1)

# Renomeando as colunas
df.columns = ['Renda', 'Pontuacao_de_Credito', 'Historico_de_Pagamento', 'Limite_de_Credito', 'qtdfilho']

# Exportando o DataFrame para um arquivo .csv
df.to_csv('dados.csv', index=False)



