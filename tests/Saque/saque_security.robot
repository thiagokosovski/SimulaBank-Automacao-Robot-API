*** Settings ***

############################################################
# Recursos compartilhados do framework
############################################################

Resource
...    ../../config/package.resource


*** Test Cases ***

############################################################
# CT-SAQ-006
#
# Objetivo:
#
# Validar a não realização de saque sem token
#
# Endpoint:
#
# POST /api/saque/
#
# Validações:
#
# - HTTP 401
# - success = false
# - Authentication credentials were not provided.
#
############################################################

CT-SAQ-006 - Realizar Saque sem token

    [Tags]
    ...    saque
    ...    post
    ...    negativo
    ...    smoke
    ...    CT-SAQ-006


    ########################################################
    # Executa saque sem token
    #
    # O teste escolhe qual payload deseja utilizar.
    #
    ########################################################

    ${response}=
    ...    Realizar Saque Sem Token
    ...    resources/payloads/saque/saque_valido.json


    ########################################################
    # Valida status HTTP
    #
    # Esperado:
    #
    # 401 OK
    #
    ########################################################

    Validar Status HTTP
    ...    ${response}
    ...    401


    ########################################################
    # Converte resposta HTTP para JSON
    ########################################################

    ${json}=
    ...    Converter Resposta para JSON
    ...    ${response}


    ########################################################
    # Valida regras específicas do saque
    ########################################################

    Validar Acesso Sem Autenticacao
    ...    ${json}


    ########################################################
    # Exibe retorno no console
    ########################################################

    Log To Console
    ...    ${json}


############################################################
# CT-SAQ-006
#
# Objetivo:
#
# Validar a não realização de saque sem token
#
# Endpoint:
#
# POST /api/saque/
#
# Validações:
#
# - HTTP 401
# - success = false
# - Authentication credentials were not provided.
#
############################################################

CT-SAQ-007 - Realizar Saque com token invalido

    [Tags]
    ...    saque
    ...    post
    ...    negativo
    ...    smoke
    ...    CT-SAQ-007


    ########################################################
    # Executa saque sem token
    #
    # O teste escolhe qual payload deseja utilizar.
    #
    ########################################################

    ${response}=
    ...    Realizar Saque com Token invalido
    ...    resources/payloads/saque/saque_valido.json


    ########################################################
    # Valida status HTTP
    #
    # Esperado:
    #
    # 401 OK
    #
    ########################################################

    Validar Status HTTP
    ...    ${response}
    ...    401


    ########################################################
    # Converte resposta HTTP para JSON
    ########################################################

    ${json}=
    ...    Converter Resposta para JSON
    ...    ${response}


    ########################################################
    # Valida regras específicas do saque
    ########################################################

    Validar Token Invalido
    ...    ${json}


    ########################################################
    # Exibe retorno no console
    ########################################################

    Log To Console
    ...    ${json}      


