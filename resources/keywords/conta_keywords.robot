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

Resource    ../../config/api_variables.robot


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
    # Garante que existe um token válido
    ########################################################

    Realizar Login

    ########################################################
    # Cria o Header Authorization
    ########################################################

    ${headers}=    Criar Header JWT

    ########################################################
    # Executa a chamada da API
    ########################################################

    ${response}=    GET On Session
    ...    simulabank
    ...    ${API_PREFIX}${CONTA_ENDPOINT}
    ...    headers=${headers}

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

