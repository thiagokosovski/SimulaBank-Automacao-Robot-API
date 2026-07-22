*** Settings ***

Resource
...    ../../config/package.resource



*** Test Cases ***


############################################################
# CT-CLI-003
#
# Objetivo:
#
# Validar que a API rejeita JWT inválido.
#
# Endpoint:
#
# GET /api/cliente/
#
# Resultado esperado:
#
# HTTP 401 Unauthorized
############################################################


CT-CLI-003 - GET Cliente com token invalido retorna 401


    [Tags]
    ...    cliente
    ...    get
    ...    negativo
    ...    security
    ...    CT-CLI-003


    ########################################################
    # Criar sessão HTTP
    ########################################################

    Criar Sessão da API


    ########################################################
    # Criar Header JWT inválido
    ########################################################

    ${headers}=    Create Dictionary
    ...    Authorization=Bearer ${TOKEN_INVALIDO}


    ########################################################
    # Executar consulta
    ########################################################

    ${response}=    GET On Session
    ...    simulabank
    ...    ${API_PREFIX}${CLIENTE_ENDPOINT}
    ...    headers=${headers}
    ...    expected_status=anything


    ########################################################
    # Validar retorno
    ########################################################

    Validar Status HTTP
    ...    ${response}
    ...    401