*** Settings ***

Resource    ../../config/package.resource



*** Test Cases ***


############################################################
# DEP-009
#
# Validar depósito sem autenticação
#
############################################################

CT-DEP-006 - Realizar Depósito Sem Token

    [Tags]
    ...    deposito
    ...    security
    ...    negativo
    ...    CT-DEP-009


    ${response}=    Realizar Depósito Sem Token
    ...    resources/payloads/deposito/deposito_valido.json



    Validar Status HTTP
    ...    ${response}
    ...    401


    ${json}=    Converter Resposta para JSON
    ...    ${response}


    Validar Erro Depósito Sem Autenticacao
    ...    ${json}

    Log To Console
    ...    ${json}   

############################################################
# DEP-010
#
# Validar depósito com token inválido
#
############################################################

CT-DEP-007 - Realizar Depósito Com Token Inválido

    [Tags]
    ...    deposito
    ...    security
    ...    negativo
    ...    CT-DEP-010


    ${response}=    Realizar Depósito Com Token Inválido
    ...    resources/payloads/deposito/deposito_valido.json



    Validar Status HTTP
    ...    ${response}
    ...    401
      
    ${json}=    Converter Resposta para JSON
    ...    ${response}

    Validar Erro Depósito Token Inválido
    ...    ${json}
        
    Log To Console
    ...    ${json}   
