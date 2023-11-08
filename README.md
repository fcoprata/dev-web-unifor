# Desenvolvimento WEB UNIFOR

Este é o README da aplicação Desenvolvimento WEB UNIFOR. Esta aplicação é desenvolvida em Python usando o framework FastAPI.

## Requisitos

Para instalar os requisitos da aplicação, execute o seguinte comando:
`pip install -r requirements.txt`

## Inicialização

Para iniciar a aplicação, execute o seguinte comando:
`uvicorn main:app --reload`

## Documentação

A documentação da aplicação está disponível em [endereço da documentação].

## Exemplos

Aqui estão alguns exemplos de como usar a aplicação:
```Obtenha todos os usuários
GET /users

Obtenha um usuário específico pelo id
GET /user/{id}

Obtenha um usuário específico pelo nome
GET /name/{name}

Obtenha um usuário específico pelo email
GET /email/{email}

Crie um novo usuário
POST /user/create

Atualize um usuário existente
PUT /user/update/{id}

Exclua um usuário
DELETE /user/delete/{id}

Login
POST /login
```