import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression  # Pode ser outro algoritmo de regressão
from sklearn.metrics import mean_squared_error

# Carregar seu conjunto de dados
data = pd.read_csv('dados.csv')


# Dividir os dados em recursos (X) e variável alvo (y)
X = data.drop('Limite_de_Credito', axis=1)
y = data['Limite_de_Credito']


# Dividir os dados em conjunto de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42123)

# Inicializar e treinar o modelo (usando regressão linear neste exemplo)
model = LinearRegression()
model.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
y_pred = model.predict(X_test)

# Avaliar o desempenho do modelo (por exemplo, usando o erro quadrático médio)
mse = mean_squared_error(y_test, y_pred)
print(f"Erro Quadrático Médio: {mse}")

# Agora você pode usar o modelo treinado para prever limites de crédito para novos solicitantes
novo_solicitante = pd.DataFrame({'Renda': [10000], 'Pontuacao_de_Credito': [300], 'Historico_de_Pagamento': [20]})
limite_previsto = model.predict(novo_solicitante)
print(f"Limite de Crédito Previsto para o Novo Solicitante: {limite_previsto[0]}")
#faça um grafico 
