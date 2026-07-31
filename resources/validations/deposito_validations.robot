*** Settings ***

Library    Collections


*** Keywords ***

############################################################
# Validar Depósito Realizado
#
# Objetivo:
#
# Validar retorno positivo do depósito.
#
############################################################

Validar Depósito Realizado

    [Arguments]
    ...    ${json}


    ########################################################
    # Valida sucesso
    ########################################################

    ${success}=
    ...    Get From Dictionary
    ...    ${json}
    ...    success


    Should Be True
    ...    ${success}



    ########################################################
    # Valida mensagem
    ########################################################

    ${message}=
    ...    Get From Dictionary
    ...    ${json}
    ...    message


    Should Be Equal
    ...    ${message}
    ...    Depósito realizado com sucesso.



    ############################################################
    # Valida saldo atual
    ############################################################

    ${saldo}=
    ...    Get From Dictionary
    ...    ${json}
    ...    saldo_atual


    Should Be True
    ...    ${saldo} >= 0
      
############################################################
# Validar Erro Valor Depósito
#
# Objetivo:
#
# Validar mensagem de erro para depósito com valor zero.
#
############################################################

Validar Erro Valor Depósito

    [Arguments]    ${json}


    ${valor}=    Get From Dictionary
    ...    ${json}
    ...    valor


    Should Contain
    ...    ${valor[0]}
    ...    maior que zero
 