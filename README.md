# Projeto_1-Módulo_2-DEVinHouse ConectaNuvem

Projeto inteiro realizado com base na linguagem Python.

## Descrição dos projeto

Construir o sistema DEVinCar:
- Menu de opções
- Cadastro e venda de veículos
- Alteração de dados de veículos
- Prints com informações dos veículos selecionados
- Prints com informações de veículos vendidos e da empresa

## Construção do Projeto

O projeto foi construído com base em conceitos de orientação a objetos, onde cada ojeto desempenha suas funções e pode ainda executar outro objeto dentro da mesma, através do conceito de composição.
As classes MotoTriciclo, Carro e Camioneta são derivadas da classe Veiculo. A classe veiculo possui métodos e atributos que são compartilhados com as classes 'filhas', porém as classes 'filhas' também possuem seus próprios métodos e atributos juntamente com os herdados da classe superior.
A classe RetornaInfos é responsável pela maior parte dos prints de informações na tela de acordo com o que for selecionado no menu.
A classe MenuOptions foi criada para conter os templates de opções para o Menu e a classe ValidarInputs foi criada com o intuito de realizar as verificações de dados e validações de erros para que o sistema não pare de funcionar durante as interações do usuário.
A classe Menu foi construída como um display de interação, sendo executado no terminal de cada sistema operacional. Essa classe possui os templates de opções e cada opção contém os métodos das outras classes contidas no projeto. De acordo com o que o usuário selecionar das opções, o menu direciona o que vai ser retornado para a interação.

## Objetivos

- O objetivo principal foi praticar a linguagem python em cima dos conceitos de orientação a objetos, abstração, loops, operadores lógicos, condicionais e manipulação de listas e dicionários.

### Como executar

- o projeto foi construído para ser uma aplicação simples de teoria e prática, apenas cloná-lo e testar no terminal.

