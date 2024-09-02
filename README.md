# Tutorial de Instalação e Execução de Testes seguindo os passos do vídeo

## 1. Instalação e Preparação do Ambiente
Para começar, é necessário configurar o ambiente de desenvolvimento. Siga os passos abaixo:

### 1.1 Instale o ambiente virtual do Python

sudo apt install python3-venv


### 1.2 Navegue até o diretório do projeto

cd detect-test-pollution-main


### 1.3 Crie e ative o ambiente virtual

python3 -m venv ./venv
source ./venv/bin/activate


### 1.4 Instale as dependências do projeto

pip install -r requirements.txt


## 2. Execução dos Testes
Com o ambiente configurado, você pode começar a executar os testes:

### 2.1 Execute os testes normalmente

pytest -vv test_cal.py


### 2.2 Execute os testes com relatório de cobertura de linha (line coverage)

pytest -vv test_cal.py --cov=cal


### 2.3 Execute os testes com relatório de cobertura de ramos (branch coverage)

pytest -vv test_cal.py --cov=cal --cov-branch --cov-report html


## 3. Testes de Mutação com Mutmut
Para realizar testes de mutação, siga os passos abaixo:

### 3.1 Execute o Mutmut

mutmut run --paths-to-mutate=../detect-test-pollution-main/cal.py


### 3.2 Verifique os resultados dos testes de mutação

mutmut results


### 3.3 Exiba detalhes de um resultado específico de mutação

mutmut show [id]


### 3.4 Gere um relatório HTML dos testes de mutação

mutmut html

