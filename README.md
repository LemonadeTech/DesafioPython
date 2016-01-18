[![Build Status](https://travis-ci.org/lffsantos/DesafioPython.svg?branch=master)](https://travis-ci.org/lffsantos/DesafioPython)
[![Coverage Status](https://coveralls.io/repos/lffsantos/DesafioPython/badge.svg?branch=master&service=github)](https://coveralls.io/github/lffsantos/DesafioPython?branch=master)

[https://locadora-lucasfarias.herokuapp.com/](https://www.github.com)

## Como desenvolver?

1. clone o respositório.
2. crie um virtualenvo com Python 3.5.
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância .env
6. Execute os testes.

```console
git clone git@github.com:lffsantos/DesafioPython.git DesafioPython
cd DesafioPython
python -m venv .env
source .env/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

```console
API REST: 
http://host:port/api/v1/
```

=================================================================================================================

O objetivo do desafio proposto é avaliar o conhecimento do candidato e verificar se ele possui o conhecimento básico esperado para exercício das atividades esperadas. 

##Desafio
O desafio consiste na construção de um aplicativo simples para locação de automóveis. O objetivo do app é controlar a locação dos veículos, não devendo por exemplo permitir a locação de um mesmo veiculo para 2 usuários ao mesmo tempo. Deverá existir APIs REST para comunicação de cadastro de veiculo, usuários, locação e devolução.

##Requisitos
* Veículos possuem as seguintes categorias: Moto, Carro, Utilitário, Caminhão
* O cadastro do cliente deverá ter somente nome, CPF, tipo de CNH (obrigatórios)
* O REST deverá aceitar o formato JSON
* Deverá ser feita validação da CNH do usuário com a categoria do veiculo escolhido.
* Testes unitários
* A devolução do veiculo deverá registrar a quilometragem rodada.
* Configurar a página de administração da aplicação

##Plus
* Desenvolver parte de reserva de veículos
* Disparar email ao vagar o veiculo que existe reserva.

##Observações
* Não reinvente a roda. Aproveite o máximo que a plataforma pode lhe oferecer.
* Utilizar OO.
* Utilizar corretamente os padrões RESTful
* Não se preocupe em deixar o aplicativo com um uma interface profissional para publicação. Faça o necessário para deixar o app mais simples possível.
* De prioridade aos REQUISITOS e não ao plus

##O que sera avaliado
* Qualidade do código ( clareza, boas práticas )
* Desempenho do aplicativo
* Entrega no prazo
* Melhor utilização das API fornecidas pela plataforma
* Melhor utilização do espaço da tela
* Testes unitários

**Entrega: Deverá criar um PR deste repositório com a solução**

Qualquer duvida entrar em contato: **dev (at) itslemonade.com**
