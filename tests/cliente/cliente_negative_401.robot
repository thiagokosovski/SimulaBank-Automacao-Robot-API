** Settings ***

Resource    ../../config/package.resource


*** Test Cases ***

############################################################
# CT-CLI-002
#
# Objetivo:
# Garantir que o endpoint exija autenticação.
############################################################

CT-CLI-002 - GET Cliente sem token retorna 401

    [Tags]
    ...    cliente
    ...    get
    ...    negativo
    ...    CT-CLI-002

    ########################################################
    # Cria sessão
    ########################################################

    Criar Sessão da API

    ########################################################
    # Consulta sem autenticação
    ########################################################

    ${response}=    Realizar GET
    ...    ${API_PREFIX}${CLIENTE_ENDPOINT}

    ########################################################
    # Valida retorno
    ########################################################

    Validar Status HTTP
    ...    ${response}
    ...    401