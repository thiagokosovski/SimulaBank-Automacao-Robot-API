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