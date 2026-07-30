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
      
############################################################
# Validar Erro Depósito Sem Autenticação
#
# Objetivo:
#
# Validar retorno quando depósito é realizado
# sem token de autenticação.
#
############################################################

Validar Erro Depósito Sem Autenticacao

    [Arguments]    ${json}


    ${detail}=    Get From Dictionary
    ...    ${json}
    ...    detail


    Should Be Equal
    ...    ${detail}
    ...    Authentication credentials were not provided.

############################################################
# Validar Erro Depósito Token Inválido
#
# Objetivo:
#
# Validar retorno quando depósito é realizado
# com token JWT inválido.
#
############################################################

Validar Erro Depósito Token Inválido

    [Arguments]    ${json}


    ########################################################
    # Valida detalhe
    ########################################################

    ${detail}=    Get From Dictionary
    ...    ${json}
    ...    detail


    Should Be Equal
    ...    ${detail}
    ...    Given token not valid for any token type



    ########################################################
    # Valida código
    ########################################################

    ${code}=    Get From Dictionary
    ...    ${json}
    ...    code


    Should Be Equal
    ...    ${code}
    ...    token_not_valid



    ########################################################
    # Valida messages
    ########################################################

    ${messages}=    Get From Dictionary
    ...    ${json}
    ...    messages


    ${message}=    Get From Dictionary
    ...    ${messages[0]}
    ...    message


    Should Be Equal
    ...    ${message}
    ...    Token is invalid