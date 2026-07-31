*** Settings ***

############################################################
# Biblioteca para manipulação de dicionários JSON
############################################################

Library
...    Collections


*** Keywords ***

############################################################
# Validar Saque Realizado
#
# Objetivo:
#
# Validar o retorno positivo do endpoint de saque.
#
# JSON esperado:
#
# {
#     "success": true,
#     "message": "Saque realizado com sucesso.",
#     "saldo_atual": 16226.0
# }
#
############################################################

Validar Saque Realizado

    [Arguments]
    ...    ${json}


    ########################################################
    # Validação 1
    #
    # Obtém o campo success.
    #
    ########################################################

    ${success}=
    ...    Get From Dictionary
    ...    ${json}
    ...    success


    ########################################################
    # O saque deve ter sido realizado com sucesso.
    ########################################################

    Should Be True
    ...    ${success}


    ########################################################
    # Validação 2
    #
    # Obtém a mensagem retornada pela API.
    #
    ########################################################

    ${message}=
    ...    Get From Dictionary
    ...    ${json}
    ...    message


    ########################################################
    # Valida mensagem de sucesso.
    ########################################################

    Should Be Equal
    ...    ${message}
    ...    Saque realizado com sucesso.


    ########################################################
    # Validação 3
    #
    # Obtém saldo atual.
    #
    ########################################################

    ${saldo}=
    ...    Get From Dictionary
    ...    ${json}
    ...    saldo_atual


    ########################################################
    # O saldo não pode ser negativo.
    ########################################################

    Should Be True
    ...    ${saldo} >= 0


############################################################
# Validar Saldo Insuficiente
#
# Objetivo:
#
# Validar que a API rejeitou o saque devido à
# insuficiência de saldo.
#
# Resposta esperada:
#
# {
#     "success": false,
#     "message": "Saldo insuficiente."
# }
#
############################################################

Validar Saldo Insuficiente

    [Arguments]
    ...    ${json}


    ########################################################
    # Valida campo success
    ########################################################

    ${success}=
    ...    Get From Dictionary
    ...    ${json}
    ...    success


    Should Be Equal
...    ${success}
...    ${False}


    ########################################################
    # Valida mensagem
    ########################################################

    ${message}=
    ...    Get From Dictionary
    ...    ${json}
    ...    message


    Should Be Equal
    ...    ${message}
    ...    Saldo insuficiente.    
  

############################################################
# Validar Saque Com Valor Maior Que Zero
#
# Objetivo:
#
# Validar erro de negócio quando o valor do saque
# é igual ou inferior a zero.
#
# Resposta esperada:
#
# {
#     "valor": [
#         "O valor do saque deve ser maior que zero."
#     ]
# }
#
############################################################

Validar Saque Valor Deve Ser Maior Que Zero

    [Arguments]
    ...    ${json}


    ########################################################
    # Obtém o campo "valor"
    ########################################################

    ${valor}=

    ...    Get From Dictionary

    ...    ${json}

    ...    valor


    ########################################################
    # Valida mensagem retornada pela API
    ########################################################

    ${mensagem}=

    ...    Get From List

    ...    ${valor}

    ...    0


    Should Be Equal

    ...    ${mensagem}

    ...    O valor do saque deve ser maior que zero.

############################################################
# Validar Método GET Não Permitido
#
# Módulo:
#
# 18.2.5
#
############################################################

Validar Método GET Não Permitido

    [Arguments]
    ...    ${json}


    ########################################################
    # Obtém campo "detail"
    ########################################################

    ${detail}=
    ...    Get From Dictionary
    ...    ${json}
    ...    detail


    ########################################################
    # Valida mensagem retornada pela API
    ########################################################

    Should Be Equal
    ...    ${detail}
    ...    Method "GET" not allowed.


############################################################
# Validar Saque Sem Autenticação
#
# Objetivo:
#
# Validar a mensagem retornada pela API quando uma tentativa
# de saque é realizada sem credenciais de autenticação.
#
# Resposta esperada:
#
# {
#     "detail": "Authentication credentials were not provided."
# }
#
############################################################

Validar Saque Sem Token

    [Arguments]
    ...    ${json}


    ########################################################
    # Obtém campo "detail"
    ########################################################

    ${detail}=
    ...    Get From Dictionary
    ...    ${json}
    ...    detail


    ########################################################
    # Valida mensagem retornada pela API
    ########################################################

    Should Be Equal
    ...    ${detail}
    ...    Authentication credentials were not provided.



Validar Saque com Token Invalido

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