*** Settings ***

# Biblioteca responsável pelas requisições HTTP
Library    RequestsLibrary

# Biblioteca Python responsável por ler o arquivo .env
Library    ../../libraries/env_library.py

# Importa as variáveis da API
Resource    ../../config/api_variables.robot

# Importa as keywords de autenticação
Resource    auth_keywords.robot


*** Keywords ***

############################################################
# Cria uma sessão HTTP com a API.
#
# Responsável por:
# - Ler a URL da API através do arquivo .env
# - Criar uma sessão HTTP reutilizável
############################################################

Criar Sessão da API

    ${base_url}=    Get Base Url

    Create Session
    ...    simulabank
    ...    ${base_url}


############################################################
# Executa uma requisição GET.
############################################################

Realizar GET

    [Arguments]    ${endpoint}

    ${response}=    GET On Session
    ...    simulabank
    ...    ${endpoint}

    RETURN    ${response}





############################################################
# Executa uma requisição POST.
#
# expected_status=anything permite receber respostas
# de erro como:
#
# 400
# 401
# 403
# 404
#
# para que o teste possa validar o comportamento da API.
############################################################

Realizar POST

    [Arguments]
    ...    ${endpoint}
    ...    ${body}


    ${response}=    POST On Session
    ...    simulabank
    ...    ${endpoint}
    ...    json=${body}
    ...    expected_status=anything


    RETURN    ${response}    


############################################################
# Executa uma requisição PUT.
############################################################

Realizar PUT

    [Arguments]    ${endpoint}    ${body}

    ${response}=    PUT On Session
    ...    simulabank
    ...    ${endpoint}
    ...    json=${body}

    RETURN    ${response}


############################################################
# Executa uma requisição PATCH.
############################################################

Realizar PATCH

    [Arguments]    ${endpoint}    ${body}

    ${response}=    PATCH On Session
    ...    simulabank
    ...    ${endpoint}
    ...    json=${body}

    RETURN    ${response}


############################################################
# Executa uma requisição DELETE.
############################################################

Realizar DELETE

    [Arguments]    ${endpoint}

    ${response}=    DELETE On Session
    ...    simulabank
    ...    ${endpoint}

    RETURN    ${response}


############################################################
# GET autenticado
############################################################

Realizar GET Autenticado

    [Arguments]    ${endpoint}

    ${headers}=    Criar Header JWT

    ${response}=    GET On Session
    ...    simulabank
    ...    ${endpoint}
    ...    headers=${headers}

    RETURN    ${response}


############################################################
# POST autenticado
############################################################

Realizar POST Autenticado

    [Arguments]
    ...    ${endpoint}
    ...    ${body}

    ${headers}=    Criar Header JWT

    ${response}=    POST On Session
    ...    simulabank
    ...    ${endpoint}
    ...    json=${body}
    ...    headers=${headers}

    RETURN    ${response}


############################################################
# PUT autenticado
############################################################

Realizar PUT Autenticado

    [Arguments]
    ...    ${endpoint}
    ...    ${body}

    ${headers}=    Criar Header JWT

    ${response}=    PUT On Session
    ...    simulabank
    ...    ${endpoint}
    ...    json=${body}
    ...    headers=${headers}

    RETURN    ${response}


############################################################
# PATCH autenticado
############################################################

Realizar PATCH Autenticado

    [Arguments]
    ...    ${endpoint}
    ...    ${body}

    ${headers}=    Criar Header JWT

    ${response}=    PATCH On Session
    ...    simulabank
    ...    ${endpoint}
    ...    json=${body}
    ...    headers=${headers}

    RETURN    ${response}


############################################################
# DELETE autenticado
############################################################

Realizar DELETE Autenticado

    [Arguments]    ${endpoint}

    ${headers}=    Criar Header JWT

    ${response}=    DELETE On Session
    ...    simulabank
    ...    ${endpoint}
    ...    headers=${headers}

    RETURN    ${response}