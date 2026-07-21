*** Settings ***

Library    Collections


*** Keywords ***


Validar Mensagem de Erro

    [Arguments]
    ...    ${json}
    ...    ${campo}
    ...    ${mensagem}


    Should Be Equal
    ...    ${json["${campo}"]}
    ...    ${mensagem}