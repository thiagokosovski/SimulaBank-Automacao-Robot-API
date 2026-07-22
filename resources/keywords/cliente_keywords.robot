*** Settings ***

############################################################
# Biblioteca HTTP
############################################################

Library    RequestsLibrary


############################################################
# Variáveis da API
############################################################

Resource    ../../config/package.resource


############################################################
# Keywords comuns
############################################################

Resource    common_keywords.robot



*** Keywords ***


############################################################
# Consultar Cliente
#
# Objetivo:
# Buscar os dados do cliente autenticado.
#
# Endpoint:
#
# GET /api/cliente/
#
# Necessita JWT
############################################################

Consultar Cliente

    ########################################################
    # Executa GET autenticado
    ########################################################

    ${response}=    Realizar GET Autenticado
    ...    ${API_PREFIX}${CLIENTE_ENDPOINT}


    RETURN    ${response}