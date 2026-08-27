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


############################################################
# MÓDULO 8.2.2
#
# CT-SAQ-003
#
# Saque com valor negativo
#
############################################################

CT-SAQ-004 - Realizar Saque Com Valor Negativo

    [Tags]
    ...    saque
    ...    post
    ...    negativo
    ...    CT-SAQ-003


    ########################################################
    # Executa o saque
    #
    # O payload utilizado contém:
    #
    # "valor": -50
    #
    ########################################################

    ${response}=

    ...    Realizar Saque

    ...    resources/payloads/saque/saque_negativo.json


    ########################################################
    # Valida status HTTP
    #
    # A API deve rejeitar o valor negativo.
    #
    # Esperado:
    #
    # HTTP 400
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
    # Valida mensagem de erro
    ########################################################

    Validar Saque Valor Deve Ser Maior Que Zero

    ...    ${json}


    ########################################################
    # Exibe retorno no console
    ########################################################

    Log To Console

    ...    ${json}
     

############################################################
# 18.2.5
#
# CT-SAQ-006
#
# Objetivo:
#
# Validar que o endpoint de saque não permite utilização
# do método GET.
#
############################################################

CT-SAQ-005 - Realizar Saque Com Método GET

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
    ...    Realizar Saque Com Método GET
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
    ...    405


    ########################################################
    # Converte resposta HTTP para JSON
    ########################################################

    ${json}=
    ...    Converter Resposta para JSON
    ...    ${response}

 

    ########################################################
    # Valida regras específicas do saque
    ########################################################

    Validar Método GET Não Permitido
    ...    ${json}


    ########################################################
    # Exibe retorno no console
    ########################################################

    Log To Console
    ...    ${json}    


############################################################
# 18.2.5
#
# CT-SAQ-006
#
# Objetivo:
#
# Validar erro
#
############################################################

CT-SAQ-005 - Validar Saque Com erro

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
    ...    Realizar Saque Com Método GET
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
    ...    400


    ########################################################
    # Converte resposta HTTP para JSON
    ########################################################

    ${json}=
    ...    Converter Resposta para JSON
    ...    ${response}

 

    ########################################################
    # Valida regras específicas do saque
    ########################################################

    Validar Método GET Não Permitido
    ...    ${json}


    ########################################################
    # Exibe retorno no console
    ########################################################

    Log To Console
    ...    ${json}    

