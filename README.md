# Classificação de Flores com KNN

## Identificação

**Integrantes:**

* Ricardo de Carvalho


**Disciplina:** IA
**Algoritmo escolhido:** KNN — K-Nearest Neighbors
**Categoria:** Aprendizado Supervisionado
**Linguagem utilizada:** Python
**Base de dados:** Iris Dataset

---

## 1. Introdução

Este projeto tem como objetivo apresentar o funcionamento teórico e prático do algoritmo **KNN**, também conhecido como **K-Nearest Neighbors** ou **K-Vizinhos Mais Próximos**.

O KNN é um algoritmo de **Aprendizado Supervisionado**, utilizado principalmente em problemas de classificação. Ele funciona comparando um novo dado com exemplos já conhecidos e definindo sua classe com base nos vizinhos mais próximos.

Neste trabalho, o algoritmo foi aplicado na classificação de flores da base de dados **Iris Dataset**, com o objetivo de identificar a espécie de uma flor a partir de suas características.

---

## 2. Problema Proposto

O problema escolhido foi a classificação de flores em três espécies:

* Setosa;
* Versicolor;
* Virginica.

A base de dados Iris possui quatro características principais para cada flor:

* Comprimento da sépala;
* Largura da sépala;
* Comprimento da pétala;
* Largura da pétala.

Com base nesses valores, o modelo deve prever corretamente a espécie da flor.

---

## 3. Funcionamento do Algoritmo KNN

O KNN classifica um novo exemplo com base nos exemplos mais próximos do conjunto de treinamento.

O funcionamento ocorre da seguinte forma:

1. O algoritmo recebe um novo dado;
2. Calcula a distância entre esse novo dado e os dados já conhecidos;
3. Seleciona os **K vizinhos mais próximos**;
4. Verifica qual classe aparece com maior frequência entre esses vizinhos;
5. Classifica o novo dado com a classe mais frequente.

Neste projeto, foi utilizado o valor **K = 3**, ou seja, o algoritmo analisa os três vizinhos mais próximos para tomar a decisão.

---

## 4. Conceito Matemático Básico

O principal conceito matemático utilizado pelo KNN é o cálculo de distância.

Uma das distâncias mais utilizadas é a **distância euclidiana**, que mede o quão distante um ponto está de outro.

De forma simples, quanto menor a distância entre dois exemplos, mais parecidos eles são. Assim, o KNN utiliza essa proximidade para decidir a classificação de um novo exemplo.

---

## 5. Implementação

A implementação foi desenvolvida em **Python**, utilizando a biblioteca **Scikit-learn**.

O projeto realiza as seguintes etapas:

1. Carrega a base de dados Iris;
2. Separa os dados em treino e teste;
3. Cria o modelo KNN com K igual a 3;
4. Treina o modelo com os dados de treinamento;
5. Realiza previsões com os dados de teste;
6. Calcula a acurácia;
7. Exibe a matriz de confusão e o relatório de classificação;
8. Testa um novo exemplo de flor.

---

## 6. Como Executar o Projeto

Primeiro, instale as dependências:

```bash
pip install -r requirements.txt
```

Depois, execute o arquivo principal:

```bash
python main.py
```

---

## 7. Resultados Obtidos

Após executar o programa, o modelo apresenta a acurácia obtida, a matriz de confusão e o relatório de classificação.

A acurácia indica a porcentagem de acertos do modelo. A matriz de confusão mostra quais classes foram classificadas corretamente e quais foram confundidas. Já o relatório de classificação apresenta métricas como precisão, revocação e f1-score.

Os resultados demonstram que o KNN conseguiu classificar corretamente a maior parte das flores da base de teste, mostrando bom desempenho para esse problema.

---

## 8. Vantagens do KNN

Algumas vantagens do algoritmo KNN são:

* É simples de entender;
* É fácil de implementar;
* Pode ser usado para classificação e regressão;
* Funciona bem em bases pequenas e organizadas;
* Não exige um treinamento complexo.

---

## 9. Desvantagens do KNN

Algumas desvantagens do algoritmo KNN são:

* Pode ser lento em bases de dados muito grandes;
* A escolha do valor de K influencia o resultado;
* Pode ser prejudicado por dados com ruídos;
* Pode ter desempenho ruim quando os atributos possuem escalas muito diferentes.

---

## 10. Aplicações Práticas

O KNN pode ser utilizado em diferentes áreas, como:

* Classificação de imagens;
* Reconhecimento de padrões;
* Sistemas de recomendação;
* Diagnóstico médico;
* Classificação de textos;
* Identificação de espécies.

---

## 11. Conclusão

Com este projeto, foi possível compreender o funcionamento do algoritmo KNN tanto na teoria quanto na prática.

O KNN se mostrou um algoritmo simples e eficiente para problemas de classificação, principalmente em bases pequenas e bem organizadas, como o Iris Dataset.

A implementação prática ajudou a entender conceitos importantes de Machine Learning, como separação entre treino e teste, classificação, distância, valor de K, acurácia e análise de resultados.

---

## 12. Referências

SCIKIT-LEARN. **KNeighborsClassifier**. Documentação oficial do Scikit-learn.

SCIKIT-LEARN. **Iris Dataset**. Documentação oficial do Scikit-learn.

IBM. **What is the k-nearest neighbors algorithm?** IBM Think.
