*** Settings ***

Resource
...    ../../config/package.resource


*** Keywords ***

############################################################
# Realizar Depósito
#
# Objetivo:
#
# Executar endpoint de depósito autenticado.
#
# Recebe:
#
# ${payload_file}
#
# Exemplos:
#
# deposito_valido.json
# deposito_zero.json
# deposito_negativo.json
# deposito_caracteres.json
#
# Fluxo:
#
# 1. Realiza autenticação
# 2. Carrega payload
# 3. Executa POST autenticado
# 4. Retorna response HTTP
#
############################################################

Realizar Depósito

    [Arguments]
    ...    ${payload_file}


    ########################################################
    # Garante autenticação
    ########################################################

    Realizar Login


    ########################################################
    # Carrega payload informado pelo teste
    ########################################################

    ${payload}=
    ...    Load JSON From File
    ...    ${payload_file}


    ########################################################
    # Executa POST autenticado
    ########################################################

    ${response}=
    ...    Realizar POST Autenticado
    ...    ${API_PREFIX}${DEPOSITO_ENDPOINT}
    ...    ${payload}


    ########################################################
    # Retorna response HTTP
    ########################################################

    RETURN
    ...    ${response}


############################################################
# Realizar Depósito Sem Token
#
# Objetivo:
#
# Executar depósito sem autenticação JWT.
#
# Recebe:
#
# ${payload_file}
#
# Fluxo:
#
# 1. Carrega payload
# 2. Executa POST sem autenticação
# 3. Retorna response HTTP
#
############################################################

Realizar Depósito Sem Token

    [Arguments]
    ...    ${payload_file}


    ########################################################
    # Carrega payload
    ########################################################

    ${payload}=
    ...    Load JSON From File
    ...    ${payload_file}


    ########################################################
    # Executa POST sem autenticação
    ########################################################

    ${response}=
    ...    Realizar POST Sem Autenticacao
    ...    ${API_PREFIX}${DEPOSITO_ENDPOINT}
    ...    ${payload}


    RETURN
    ...    ${response}


############################################################
# Realizar Depósito Com Token Inválido
#
# Objetivo:
#
# Executar depósito utilizando um JWT inválido.
#
# Recebe:
#
# ${payload_file}
#
# Fluxo:
#
# 1. Carrega payload
# 2. Executa POST com token inválido
# 3. Retorna response HTTP
#
############################################################

Realizar Depósito Com Token Inválido

    [Arguments]
    ...    ${payload_file}


    ########################################################
    # Carrega payload
    ########################################################

    ${payload}=
    ...    Load JSON From File
    ...    ${payload_file}


    ########################################################
    # Executa POST com token inválido
    ########################################################

    ${response}=
    ...    Realizar POST Token Invalido
    ...    ${API_PREFIX}${DEPOSITO_ENDPOINT}
    ...    ${payload}


    RETURN
    ...    ${response}