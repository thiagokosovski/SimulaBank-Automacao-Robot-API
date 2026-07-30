*** Settings ***

Resource    ../../config/package.resource



*** Test Cases ***


############################################################
# DEP-001
#
# Realizar depósito com valor válido
#
############################################################

CT-DEP-001 - Realizar Depósito Com Valor Válido

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