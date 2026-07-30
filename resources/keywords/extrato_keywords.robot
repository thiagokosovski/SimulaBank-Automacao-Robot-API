*** Settings ***

Resource    ../../config/package.resource


*** Keywords ***

############################################################
# Consulta Extrato autenticado
############################################################

Consultar Extrato

    ########################################################
    # Garante um Token JWT válido
    ########################################################

    Realizar Login

    ########################################################
    # Executa GET autenticado
    ########################################################

    ${response}=    Realizar GET Autenticado
    ...    ${API_PREFIX}${EXTRATO_ENDPOINT}

    RETURN    ${response}



############################################################
# Consulta Extrato sem token
############################################################

Consultar Extrato Sem Token

    ${response}=    Realizar GET Sem Autenticacao
    ...    ${EXTRATO_ENDPOINT}

    RETURN    ${response}


############################################################
# Consulta Extrato com token inválido
############################################################

Consultar Extrato Token Invalido

    ${response}=    Realizar GET Token Invalido
    ...    ${EXTRATO_ENDPOINT}

    RETURN    ${response}

############################################################
# Login Usuário Extrato Vazio
#
# Objetivo:
#
# Realizar autenticação utilizando o usuário exclusivo
# sem movimentações bancárias.
############################################################

Login Usuário Extrato Vazio

    ########################################################
    # Carrega payload de login
    ########################################################

    ${payload}=
    ...    Load JSON From File
    ...    resources/payloads/login_extrato_vazio.json


    ########################################################
    # Executa Login
    ########################################################

    ${response}=
    ...    POST On Session
    ...    simulabank
    ...    ${API_PREFIX}${TOKEN_ENDPOINT}
    ...    json=${payload}


    ########################################################
    # Valida HTTP 200
    ########################################################

    Validar Status HTTP
    ...    ${response}
    ...    200


    ########################################################
    # Obtém Access Token
    ########################################################

    ${json}=
    ...    Converter Resposta para JSON
    ...    ${response}

    ${token}=
    ...    Get From Dictionary
    ...    ${json}
    ...    access


    RETURN
    ...    ${token}

############################################################
# Consultar Extrato Usuário Vazio
#
# Objetivo:
#
# Consultar o extrato utilizando um usuário
# sem movimentações bancárias.
############################################################

Consultar Extrato Usuário Vazio

    ########################################################
    # Realiza Login
    ########################################################

    ${token}=
    ...    Login Usuário Extrato Vazio


    ########################################################
    # Cria Header Authorization
    ########################################################

    ${headers}=
    ...    Create Dictionary
    ...    Authorization=Bearer ${token}


    ########################################################
    # Consulta Extrato
    ########################################################

    ${response}=
    ...    GET On Session
    ...    simulabank
    ...    ${API_PREFIX}${EXTRATO_ENDPOINT}
    ...    headers=${headers}


    RETURN
    ...    ${response}