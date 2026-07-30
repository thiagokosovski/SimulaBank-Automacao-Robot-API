*** Settings ***

Resource
...    ../../config/package.resource



*** Keywords ***

############################################################
# Realizar Depósito
#
# Objetivo:
#
# Executar endpoint de depósito.
#
# Recebe:
#
# ${payload_file}
#
# Exemplo:
#
# deposito_valido.json
# deposito_zero.json
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
    # Carrega payload informado
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



    RETURN

    ...    ${response}


############################################################
# Realizar Depósito Sem Token
#
# Objetivo:
#
# Executar depósito sem autenticação JWT.
#
############################################################

Realizar Depósito Sem Token

    [Arguments]    ${payload_file}

    ${payload}=    Load JSON From File
    ...    ${payload_file}

    ${response}=    Realizar POST Sem Autenticacao
    ...    ${API_PREFIX}${DEPOSITO_ENDPOINT}
    ...    ${payload}

    RETURN    ${response}


############################################################
# Realizar Depósito Token Inválido
#
# Objetivo:
#
# Executar depósito com JWT inválido.
#
############################################################

Realizar Depósito Com Token Inválido
    
    [Arguments]    ${payload_file}

    ${payload}=    Load JSON From File
    ...    ${payload_file}

    ${response}=    Realizar POST Token Invalido
    ...    ${API_PREFIX}${DEPOSITO_ENDPOINT}
    ...    ${payload}

    RETURN    ${response}      

