*** Settings ***

############################################################
# Recursos compartilhados do framework
############################################################

Resource
...    ../../config/package.resource


*** Test Cases ***


############################################################
# CT-SAQ-005
#
# Objetivo:
#
# Validar que a API rejeita um saque cujo valor seja
# superior ao saldo disponível na conta.
#
# Endpoint:
#
# POST /api/saque/
#
# Cenário:
#
# valor = 200000.00
#
# Resultado esperado:
#
# success = false
# message = "Saldo insuficiente."
#
############################################################

CT-SAQ-002 - Realizar Saque Maior Que Saldo

    [Tags]
    ...    saque
    ...    post
    ...    negativo
    ...    regra-negocio
    ...    CT-SAQ-005


    ########################################################
    # Executa saque
    #
    # A keyword:
    #
    # - Realiza login
    # - Obtém JWT
    # - Carrega payload
    # - Executa POST autenticado
    ########################################################

    ${response}=
    ...    Realizar Saque
    ...    resources/payloads/saque/saque_maior_saldo.json


    ########################################################
    # Valida status HTTP
    #
    # IMPORTANTE:
    #
    # Utilizar o status retornado pela API.
    # Se o Postman retornar 400, manter 400.
    ########################################################

    Validar Status HTTP
    ...    ${response}
    ...    400


    ########################################################
    # Converte resposta HTTP para JSON
    ########################################################

    ${json}=
    ...    Converter Resposta para JSON
    ...    ${response}


    ########################################################
    # Valida regra de negócio
    #
    # Esperado:
    #
    # success = false
    # message = "Saldo insuficiente."
    ########################################################

    Validar Saldo Insuficiente
    ...    ${json}


    ########################################################
    # Exibe retorno da API
    ########################################################

    Log To Console
    ...    ${json}


############################################################
# CT-SAQ-002
#
# Objetivo:
#
# Validar que a API rejeita saque com valor igual a zero.
#
# Endpoint:
#
# POST /api/saque/
#
# Payload:
#
# saque_zero.json
#
# Resposta esperada:
#
# HTTP 400
#
# {
#     "valor": [
#         "O valor do saque deve ser maior que zero."
#     ]
# }
#
############################################################

CT-SAQ-003 - Realizar Saque Com Valor Zero

    [Tags]
    ...    saque
    ...    post
    ...    negativo
    ...    CT-SAQ-002


    ########################################################
    # Executa saque
    #
    # A keyword:
    #
    # - Realiza autenticação
    # - Carrega o payload
    # - Executa POST
    # - Retorna response
    ########################################################

    ${response}=

    ...    Realizar Saque

    ...    resources/payloads/saque/saque_zero.json


    ########################################################
    # Valida HTTP 400
    #
    # O valor zero é uma entrada inválida.
    ########################################################

    Validar Status HTTP

    ...    ${response}

    ...    400


    ########################################################
    # Converte resposta para JSON
    ########################################################

    ${json}=

    ...    Converter Resposta para JSON

    ...    ${response}


    ########################################################
    # Valida mensagem de negócio
    ########################################################

    Validar Saque Valor Deve Ser Maior Que Zero

    ...    ${json}


    ########################################################
    # Exibe retorno
    ########################################################

    Log To Console

    ...    ${json}    

