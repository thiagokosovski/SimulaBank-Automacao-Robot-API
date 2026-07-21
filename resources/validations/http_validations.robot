*** Settings ***

Library    Collections
Library    RequestsLibrary


*** Keywords ***

############################################################
# Valida Status HTTP
############################################################

Validar Status HTTP

    [Arguments]    ${response}    ${status}

    Status Should Be    ${status}    ${response}


############################################################
# Converte Response para JSON
############################################################

Converter Resposta para JSON

    [Arguments]    ${response}

    ${json}=    Set Variable    ${response.json()}

    RETURN    ${json}


############################################################
# Valida igualdade
############################################################

Validar Campo Igual

    [Arguments]    ${valor}    ${esperado}

    Should Be Equal    ${valor}    ${esperado}


############################################################
# Valida campo preenchido
############################################################

Validar Campo Não Vazio

    [Arguments]    ${valor}

    Should Not Be Empty    ${valor}