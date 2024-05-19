# Projeto Alura-Space-AL 
## Um CRUD escrito na linguagem Python utilizando o framework Django

Alura-Space-AL é uma aplicação fullstack, desenvolvida em Python com o Framework Django. Suas funcionalidades estão baseadas
numa galeria virtual, de Astrofotografias, que podem ser cadastradas pelos usuários, sendo um ponto de compartilhamento
e interações de amantes da astronomia. Para desenvolver essa aplicação, foram utilizadas as seguintes tecnologias:

* Python 3.10.6
* Django 4.1
* PostgreSQL 12.12


### :dart: Objetivos

* Desenvolver um CRUD fullstack
* Implementar  Class-Based-Views
* Aprimorar repertório técnico

Esse projeto é o resultado de atividades práticas realizadas durante a formação [Django: crie aplicações em Python](https://cursos.alura.com.br/formacao-django), 
na plataforma de cursos online [Alura](https://www.alura.com.br/). A motivação para desenvolvimento desse projeto é a preparação para o 
[Challenge Back-End 6° Edição](https://www.alura.com.br/challenges/back-end-6?host=https://cursos.alura.com.br). Que será um desafio técnico com prazo de 4 semanas, para desenvolver uma aplicação 
Back-End do zero.

### :bookmark_tabs: Etapas do projeto

| STATUS             | DESCRIÇÃO          |
|--------------------|--------------------|
| :white_check_mark: | Finalizado         |
| :hourglass:        | Em desenvolvimento |
| :x:                | Não implementado   |



* :white_check_mark: Definir modelos e relacionamentos
* :white_check_mark: criar view e rota para index
* :white_check_mark: criar view e rota para cadastro de usuário
* :white_check_mark: criar validação de formulário de cadastro de usuário
* :hourglass: criar view e rota para atualização de usuário
* :x: criar view e rota para exclusão de usuário
* :white_check_mark: criar view e rota para para Login de usuário
* :white_check_mark: criar view e rota para cadastro de astrofotografia
* :white_check_mark: criar view e rota para para visualizar astrofotografia
* :x: criar view e rota para visualizar astrofotografia cadastrada pelo usuário da sessão
* :x: criar view e rota para atualização de astrofotografia
* :x: criar view e rota para exclusão de astrofotografia
* :white_check_mark: criar view e rota para buscar astrofotografia cadastrada
* :x: criar view e rota para filtrar astrofotografia por categoria


### :hammer:Building

1. realize o clone do repositório - `git clone https://github.com/MaercioMamedes/alura-space-AL.git`
2. [crie um ambiente virtual dentro do diretório do projeto e instale todas as dependências](https://www.alura.com.br/artigos/ambientes-virtuais-em-python)
3. [configure o acesso ao banco de dados na variável DATABASES](https://docs.djangoproject.com/en/4.1/ref/settings/#databases), no arquivo `setup/settings.py`
4. realize as migrações `python manage.py migrate`
5. rode o comando `python manage.py runserver`

