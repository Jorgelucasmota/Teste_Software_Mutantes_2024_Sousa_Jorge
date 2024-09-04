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

# Tutorial seguindo os passos do vídeo aplicado ao meu repositoio 

## 1. Instalação e Preparação do Ambiente
Para começar, é necessário configurar o ambiente de desenvolvimento. Siga os passos abaixo:

### 1.1 Instale o Ambiente Virtual do Python
No Windows, você pode criar um ambiente virtual com o seguinte comando:

python -m venv venv

### 1.2 Clone o Repositório
Clone o repositório do projeto escolhido:

git clone https://github.com/hernanzini/mutmut_demo.git


### 1.3 Ative o Ambiente Virtual
Ative um ambiente virtual para isolar as dependências do projeto:

.\venv\Scripts\activate

### 1.4 Instale as Dependências
Instale as dependências necessárias para o projeto, incluindo pytest, pytest-cov, e mutmut:

pip install pytest pytest-cov mutmut

## 2. Execução dos Testes
Com o ambiente configurado, você pode começar a executar os testes:

### 2.1 - Entre no projeto

cd mutmut_demo

### 2.2 Execute os Testes Unitários
Para garantir que o projeto está funcionando corretamente, execute os testes unitários:

pytest -v

### 2.3 Verifique a Cobertura de Código
Verifique a cobertura dos testes utilizando o pytest-cov:

pytest --cov=src

### 2.4 Relatório de Cobertura de Ramos
Para gerar um relatório de cobertura de ramos:

pytest --cov=src --cov-branch --cov-report html

## 3. Testes de Mutação com Mutmut
Os testes de mutação ajudam a avaliar a eficácia dos casos de teste. Para realizá-los, siga os passos abaixo:

### 3.1 Execute o Mutmut

Uso esse $env:PYTHONIOENCODING="utf-8" pois no projeto ha um código-fonte ou um dos arquivos de teste pode ter uma codificação diferente de UTF-8 (por exemplo, ISO-8859-1 ou Windows-1252), e o mutmut está tentando processá-lo como UTF-8.

$env:PYTHONIOENCODING="utf-8": Isso define a variável de ambiente PYTHONIOENCODING para "utf-8" apenas na sessão atual do PowerShell.

; mutmut run: Executa o comando mutmut run na sequência, já com a variável de ambiente configurada.

Inicie os testes de mutação:

$env:PYTHONIOENCODING="utf-8"; mutmut run


### 3.2 Verifique os Resultados dos Testes de Mutação
Para verificar os resultados dos testes de mutação:

mutmut results

### 3.3 Exiba Detalhes de um Resultado Específico de Mutação
Para ver detalhes de uma mutação específica:

mutmut show [id]

### 3.4 Gere um Relatório HTML dos Testes de Mutação
Para gerar um relatório HTML detalhado dos testes de mutação:

mutmut html

Abra o arquivo HTML gerado no seu navegador:

start html\index.html

## 4. Análise e Melhorias

### 4.1 Análise dos Resultados
Após a execução dos testes de mutação, analise quais mutações não foram detectadas pelos testes.

### 4.2 Melhorias nos Casos de Teste
Ajuste ou adicione novos casos de teste para melhorar a cobertura e identificar mais mutantes.

### 4.3 Nova Execução dos Testes de Mutação
Repita os testes de mutação após as melhorias e compare os resultados:

pytest --cov=src
mutmut run
mutmut results

# Documentação

Para mais detalhes, consulte o relatório completo [Jorge_Sousa_atividade_2.pdf]https://github.com/Jorgelucasmota/Teste_Software_Mutantes_2024_Sousa_Jorge/blob/main/Jorge_Sousa_atividade_2.pdf.

