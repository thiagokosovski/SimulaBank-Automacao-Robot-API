*** Settings ***

############################################################
# Biblioteca responsável pelas requisições HTTP
############################################################

Library    RequestsLibrary


############################################################
# Biblioteca utilizada para manipular dicionários
############################################################

Library    Collections


############################################################
# Biblioteca para validação de JSON Schema
############################################################

Library    JSONLibrary


############################################################
# Variáveis globais da API
############################################################

Resource    ../../config/package.resource


############################################################
# Keywords compartilhadas
############################################################

Resource    common_keywords.robot


############################################################
# Keywords de autenticação
############################################################

Resource    auth_keywords.robot


*** Keywords ***

############################################################
# Consultar Conta
#
# Objetivo:
# Consultar os dados da conta bancária do usuário
# autenticado utilizando JWT.
#
# Endpoint:
#
# GET /api/conta/
#
# Retorno:
#
# Response HTTP completa
############################################################

Consultar Conta

    ########################################################
    # Garante um Token JWT válido
    ########################################################

    Realizar Login

    ########################################################
    # Executa GET autenticado
    ########################################################

    ${response}=    Realizar GET Autenticado
    ...    ${API_PREFIX}${CONTA_ENDPOINT}

    ########################################################
    # Retorna resposta da API
    ########################################################

    RETURN    ${response}



    ########################################################
    # Retorna toda a resposta
    ########################################################

    RETURN    ${response}


############################################################
# Consultar Conta sem autenticação
#
# Objetivo:
# Validar bloqueio de acesso sem JWT
############################################################

Consultar Conta Sem Token


    ${response}=    GET On Session
    ...    simulabank
    ...    ${API_PREFIX}${CONTA_ENDPOINT}
    ...    expected_status=anything


    RETURN    ${response}

