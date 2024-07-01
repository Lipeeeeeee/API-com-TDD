# API com método TDD

## Projeto

&emsp;&emsp;O projeto proposto foi construir uma API assíncrona simples, com apenas um modelo de classe, que escolhi, como tema livre, uma API para registro de Jogadores de Futebol, tendo como atributos, nome, idade, valor de mercado, e um booleano para aposentado ou não, contendo um desafio final ao final da construção.<br>
&emsp;&emsp;Foi feita de forma simples, pois o foco não seria a construção da API em si, o foco deste projeto foi a aplicação do método TDD no desenvolvimento da mesma, na qual expliquarei abaixo:

## O que é TDD?

&emsp;&emsp;TDD é a sigla para <b>Test Driven Development</b>, ou seja, <b>Desenvolvimento Orientado a Testes</b>, que consiste em três passos:<br>
1. Criar testes reais da aplicação, que primeiramente falharão pois as implementações não estarão completas.

2. A partir destes testes, desenvolver o que é necessário para o teste funcionar.

3. Após o teste estar funcional, realizar a refatoração do código, para que não fique ambiguidades ou linhas de código desnecessárias.

&emsp;&emsp;Com esse método de desenvolvimento, seu projeto tende a finalizar com mais qualidade, pois seus testes estarão feitos, falhas já terão sido encontradas e corrigidas, e seu código estará limpo!

## Desafio final

&emsp;&emsp;Após criar meu venv, e terminar a API, parti para os desafios finais para testar meu conhecimento e praticar mais, desafios esses que foram:

1. Mapear exceções e capturá-las na controller, caso encontre erros na criação, inserção ou atualização de um Jogador, com sua devida mensagem de <i>feedback</i>.

2. Atualizar o <i>updated_at</i> do Jogador ao atualizá-lo com sucesso.

3. Atribuir filtros ao campo VALOR do Jogador, e garantir que não haja mais de um Jogador com o mesmo valor, optei por filtrar da seguinte forma, (15 < valor < 180)

## Considerações finais

&emsp;&emsp;Após um árduo e longo caminho para a conclusão do projeto, aprendi muito sobre o método TDD, aprefeiçoei minhas habilidades de programação, correção de erros e também a utilização do FastAPI, aprendi novas tecnologias que foram utilizadas, e me sinto orgulhoso do trabalho que fiz, me sinto melhor e mais preparado do que quando terminei meu último projeto e vejo minha evolução cada dia mais.

## Principais ferramentas utilizadas

1. [FastAPI](https://fastapi.tiangolo.com/)
2. [Uvicorn](https://www.uvicorn.org/)
3. [Pydantic](https://docs.pydantic.dev/latest/)
2. [docker-compose](https://docs.docker.com/compose/)
3. [pre-commit](https://pre-commit.com/)
3. [MongoDB](https://www.mongodb.com/docs/)
4. [Pytest](https://docs.pytest.org/en/stable/contents.html)
5. [Makefile](https://embarcados.com.br/introducao-ao-makefile/)
