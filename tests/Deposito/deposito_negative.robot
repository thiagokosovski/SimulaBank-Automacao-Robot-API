*** Settings ***

Resource    ../../config/package.resource



*** Test Cases ***


############################################################
# DEP-002
#
# Validar rejeição de depósito valor zero
#
############################################################

CT-DEP-002 - Realizar Depósito Valor Zero

    [Tags]
    ...    deposito
    ...    negativo
    ...    CT-DEP-002


    ${response}=    Realizar Depósito
    ...    resources/payloads/deposito/deposito_zero.json



    Validar Status HTTP
    ...    ${response}
    ...    400



    ${json}=    Converter Resposta para JSON
    ...    ${response}



    Validar Erro Valor Depósito
    ...    ${json}



############################################################
# DEP-003
#
# Validar rejeição de valor negativo
#
############################################################

CT-DEP-003 - Realizar Depósito Com Valor Negativo

    [Tags]
    ...    deposito
    ...    post
    ...    negativo
    ...    CT-DEP-003


    ${response}=    Realizar Depósito
    ...    resources/payloads/deposito/deposito_negativo.json



    Validar Status HTTP
    ...    ${response}
    ...    400



    ########################################################
    # Converte para JSON
    ########################################################

    ${json}=    Converter Resposta para JSON
    ...    ${response}



    ########################################################
    # Exibe retorno completo no console
    #
    ########################################################

    Log To Console
    ...    ${json}


    Validar Erro Valor Depósito
    ...    ${json}


############################################################
# DEP-004
#
# Validar rejeição de caracteres
#
############################################################

CT-DEP-004 - Realizar Depósito Com Valor Caracteres

    [Tags]
    ...    deposito
    ...    post
    ...    negativo
    ...    CT-DEP-004


    ${response}=    Realizar Depósito
    ...    resources/payloads/deposito/deposito_caracteres.json



    Validar Status HTTP
    ...    ${response}
    ...    400



    ########################################################
    # Converte para JSON
    ########################################################

    ${json}=    Converter Resposta para JSON
    ...    ${response}



    ########################################################
    # Exibe retorno completo no console
    #
    ########################################################

    Log To Console
    ...    ${json}
       

CT-DEP-005 - Validar Depósito sem tolken

    [Tags]
    ...    deposito
    ...    post
    ...    positivo
    ...    CT-DEP-001


    ${response}=    Realizar Depósito
    ...    resources/payloads/deposito/deposito_valido.json



    Validar Status HTTP
    ...    ${response}
    ...    200



    ${json}=    Converter Resposta para JSON
    ...    ${response}



    Validar Depósito Realizado
    ...    ${json}



    Log To Console
    ...    ${json}    