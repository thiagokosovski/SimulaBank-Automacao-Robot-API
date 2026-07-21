*** Settings ***

Resource    ../config/package.resource


*** Test Cases ***

Validar Login JWT

    # Executa o login
    Realizar Login

    # Apenas verifica se o token foi gerado
    Should Not Be Empty
    ...    ${ACCESS_TOKEN}