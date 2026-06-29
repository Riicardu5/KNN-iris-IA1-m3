from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Carregando a base de dados Iris
iris = load_iris()
X = iris.data
y = iris.target

# Separando os dados em treino e teste
X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Criando o modelo KNN com K = 3
modelo = KNeighborsClassifier(n_neighbors=3)

# Treinando o modelo
modelo.fit(X_treino, y_treino)

# Fazendo previsões
previsoes = modelo.predict(X_teste)

# Calculando a acurácia
acuracia = accuracy_score(y_teste, previsoes)

print("Algoritmo utilizado: KNN - K-Nearest Neighbors")
print("Base de dados utilizada: Iris Dataset")
print("Classes existentes:", iris.target_names)
print(f"Acurácia do modelo: {acuracia:.2f}")

print("\nMatriz de Confusão:")
print(confusion_matrix(y_teste, previsoes))

print("\nRelatório de Classificação:")
print(classification_report(y_teste, previsoes, target_names=iris.target_names))

# Testando uma nova flor
nova_flor = [[5.1, 3.5, 1.4, 0.2]]
resultado = modelo.predict(nova_flor)

print("\nNovo exemplo analisado:")
print("Dados da flor:", nova_flor)
print("Classe prevista:", iris.target_names[resultado[0]])