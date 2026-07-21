*** Settings ***

# Biblioteca para chamadas HTTP
Library    RequestsLibrary

# Biblioteca para trabalhar com coleções
Library    Collections

# importa a biblioteca com os logins
Library    ../../libraries/env_library.py

# Importa as variáveis da API
Resource    ../../config/api_variables.robot



*** Keywords ***

############################################################
# Realiza Login na API
#
# Fluxo:
# 1 - Cria uma sessão HTTP
# 2 - Envia usuário e senha
# 3 - Recebe os Tokens JWT
# 4 - Salva os Tokens em variáveis globais
############################################################

Realizar Login

    # Lê as configurações do ambiente
    ${base_url}=    Get Base Url
    ${username}=    Get Username
    ${password}=    Get Password

    # Cria a sessão HTTP
    Create Session
    ...    simulabank
    ...    ${base_url}

    # Corpo da requisição
    ${body}=    Create Dictionary
    ...    username=${username}
    ...    password=${password}

    # Chama o endpoint de autenticação
    ${response}=    POST On Session
    ...    simulabank
    ...    ${API_PREFIX}${TOKEN_ENDPOINT}
    ...    json=${body}

    Status Should Be
    ...    200
    ...    ${response}

    ${json}=    Set Variable
    ...    ${response.json()}

    ${access_token}=    Set Variable
    ...    ${json["access"]}

    ${refresh_token}=    Set Variable
    ...    ${json["refresh"]}

    Set Global Variable
    ...    ${ACCESS_TOKEN}
    ...    ${access_token}

    Set Global Variable
    ...    ${REFRESH_TOKEN}
    ...    ${refresh_token}


############################################################
# Cria o Header Authorization
#
# Exemplo:
#
# Authorization: Bearer eyJhbGc...
############################################################

Criar Header JWT

    ${headers}=    Create Dictionary
    ...    Authorization=Bearer ${ACCESS_TOKEN}

    RETURN    ${headers}