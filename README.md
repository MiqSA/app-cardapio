# Meu Cardápio

Meu Cardápio é uma aplicação web para comercialização de pratos de forma simples e atraente ao cliente. Contempla um sistema de cadastro de usuário e de pratos. No cadastro de pratos o usuário pode inserir o nome do prato, imagem do prato, ingredientes e mais! O usuário pode ter vários pratos cadastrados e privados, ao decidir torná-lo público um usuário administrador publica tal prato na parte principal do site.

## Tecnologias

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Docker](https://www.docker.com/products/docker-desktop)

## Como Utilizar?

Para clonar essa aplicação, você precisará ter instalado em seu computador o [Git](https://git-scm.com) e [Docker](https://www.docker.com/products/docker-desktop).Do ser terminal digite:

```bash
# Clonar esse repositório
$ git clone https://github.com/MiqSA/app-cardapio.git

# Entrar no pasta do projeto
$ cd app-cardapio

# Garantir que o docker desktop está ativo.  

# Subir aplicação pelo docker
$ docker-compose up

# A aplicação estará funcionando em http://localhost:8000/

# Para ter acesso como administrador abra outra janela do terminal e siga os seguintes passos.

# Digite o seguite comando.
 $ docker ps

# Com comando anterior será mostrado informações dos containers. Grave o CONTAINER ID do container python e digite o seguinte comando. Onde o CONTAINER_ID refere-se ao container ativo. 
$ docker exec -it CONTAINER_ID python manage.py createsuperuser

# Digite um usuário, email e senha.

# Para entrar na aba de administrador basta ir em http://localhost:8000/admin  e entrar com usuário cadastrado anteriormente.

```

## Outras Observações
Esse projeto teve como inspiração o projeto desenvolvido no curso de [Formação Django](https://cursos.alura.com.br/formacao-django)  da [Alura](https://www.alura.com.br/). Templates foram modificados do curso.

