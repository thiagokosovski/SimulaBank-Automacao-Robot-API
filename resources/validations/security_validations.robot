*** Settings ***

Library    Collections


*** Keywords ***

############################################################
# Validar acesso sem autenticação
#
# Objetivo:
#
# Validar que a API bloqueia uma requisição realizada
# sem o header Authorization.
#
# Esperado:
#
# HTTP 401
#
############################################################

Validar Acesso Sem Autenticacao

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




############################################################
# Validar acesso com token inválido
#
# Objetivo:
#
# Validar que a API rejeita uma requisição contendo
# um JWT inválido.
#
# Esperado:
#
# HTTP 401
#
############################################################

Validar Token Invalido

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