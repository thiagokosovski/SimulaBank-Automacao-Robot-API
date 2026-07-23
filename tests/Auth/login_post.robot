*** Settings ***

Resource    ../../config/package.resource


*** Test Cases ***

CT-AUTH-001 - POST Login retorna token JWT

    [Tags]
    ...    auth
    ...    post
    ...    positivo
    ...    smoke
    ...    CT-AUTH-001

    # Executa o login
    Realizar Login

    # Apenas verifica se o token foi gerado
    Should Not Be Empty
    ...    ${ACCESS_TOKEN}