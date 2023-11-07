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

Obtenha um usuário específico
GET /users/<id>

Crie um novo usuário
POST /users

Atualize um usuário existente
PUT /users/<id>

Exclua um usuário
DELETE /users/<id>
```