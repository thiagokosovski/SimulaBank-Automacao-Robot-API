*** Settings ***

############################################################
# Recursos compartilhados do framework
############################################################

Resource
...    ../../config/package.resource


*** Test Cases ***

############################################################
# CT-SAQ-001
#
# Objetivo:
#
# Validar realização de saque com valor válido.
#
# Endpoint:
#
# POST /api/saque/
#
# Validações:
#
# - HTTP 200
# - success = true
# - mensagem de sucesso
# - saldo atual >= 0
#
############################################################

CT-SAQ-001 - Realizar Saque Com Valor Válido

    [Tags]
    ...    saque
    ...    post
    ...    positivo
    ...    smoke
    ...    CT-SAQ-001


    ########################################################
    # Executa saque
    #
    # O teste escolhe qual payload deseja utilizar.
    #
    ########################################################

    ${response}=
    ...    Realizar Saque
    ...    resources/payloads/saque/saque_valido.json


    ########################################################
    # Valida status HTTP
    #
    # Esperado:
    #
    # 200 OK
    #
    ########################################################

    Validar Status HTTP
    ...    ${response}
    ...    200


    ########################################################
    # Converte resposta HTTP para JSON
    ########################################################

    ${json}=
    ...    Converter Resposta para JSON
    ...    ${response}


    ########################################################
    # Valida regras específicas do saque
    ########################################################

    Validar Saque Realizado
    ...    ${json}


    ########################################################
    # Exibe retorno no console
    ########################################################

    Log To Console
    ...    ${json}