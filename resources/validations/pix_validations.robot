*** Settings ***

Library    Collections


*** Keywords ***

############################################################
# Extrair CPF do Destinatário
#
# Módulo:
#
# 19.4
#
# Objetivo:
#
# Extrair o CPF do destinatário a partir da resposta
# retornada pelo endpoint /api/cliente/.
#
# Recebe:
#
# ${json}
#
# Retorna:
#
# ${cpf}
#
############################################################

Extrair CPF do Destinatário

    [Arguments]
    ...    ${json}


    ########################################################
    # Obtém o CPF através da chave "cpf"
    ########################################################

    ${cpf}=

    ...    Get From Dictionary

    ...    ${json}

    ...    cpf


    ########################################################
    # Valida se o CPF foi encontrado
    ########################################################

    Should Not Be Empty

    ...    ${cpf}


    ########################################################
    # Exibe o CPF encontrado
    ########################################################

    Log To Console

    ...    CPF do destinatário: ${cpf}


    ########################################################
    # Retorna CPF
    ########################################################

    RETURN

    ...    ${cpf}
  

############################################################
# Extrair Saldo
#
# Módulo:
#
# 19.7
#
# Objetivo:
#
# Extrair o saldo da conta retornado pela API.
#
# Recebe:
#
# ${json}
#
# Retorna:
#
# ${saldo}
#
############################################################

Extrair Saldo da Conta

    [Arguments]
    ...    ${json}


    ########################################################
    # Obtém o saldo através da chave "saldo"
    ########################################################

    ${saldo}=

    ...    Get From Dictionary

    ...    ${json}

    ...    saldo


    ########################################################
    # Valida se o saldo foi retornado
    ########################################################

    Should Not Be Empty

    ...    ${saldo}


    ########################################################
    # Converte o saldo de string para número
    #
    # A API retorna:
    #
    # "1101.00"
    #
    # O teste precisa trabalhar com:
    #
    # 1101.00
    #
    ########################################################

    ${saldo}=

    ...    Convert To Number

    ...    ${saldo}


    ########################################################
    # Exibe saldo capturado
    ########################################################

    Log To Console

    ...    Saldo capturado: ${saldo}


    ########################################################
    # Retorna saldo
    ########################################################

    RETURN

    ...    ${saldo}


############################################################
# Validar Saldo do Remetente Após PIX
#
# Módulo:
#
# 19.9
#
# Objetivo:
#
# Garantir que o saldo do remetente foi reduzido
# exatamente pelo valor do PIX.
#
############################################################

Validar Saldo do Remetente Após PIX

    [Arguments]
    ...    ${saldo_antes}
    ...    ${saldo_depois}
    ...    ${valor_pix}


    ########################################################
    # Calcula saldo esperado
    ########################################################

    ${saldo_esperado}=

    ...    Evaluate

    ...    ${saldo_antes} - ${valor_pix}


    ########################################################
    # Compara saldo esperado com saldo real
    ########################################################

    Should Be Equal As Numbers

    ...    ${saldo_depois}

    ...    ${saldo_esperado}
  

############################################################
# Validar Saldo do Destinatário Após PIX
#
# Módulo:
#
# 19.9
#
# Objetivo:
#
# Garantir que o saldo do destinatário foi aumentado
# exatamente pelo valor do PIX.
#
############################################################

Validar Saldo do Destinatário Após PIX

    [Arguments]
    ...    ${saldo_antes}
    ...    ${saldo_depois}
    ...    ${valor_pix}


    ########################################################
    # Calcula saldo esperado
    ########################################################

    ${saldo_esperado}=

    ...    Evaluate

    ...    ${saldo_antes} + ${valor_pix}


    ########################################################
    # Compara saldo esperado com saldo real
    ########################################################

    Should Be Equal As Numbers

    ...    ${saldo_depois}

    ...    ${saldo_esperado}


############################################################
# Validar PIX Realizado
#
# Módulo:
#
# 19.9
#
# Objetivo:
#
# Validar o retorno positivo da realização de um PIX.
#
# Resposta esperada:
#
# {
#     "success": true,
#     "message": "PIX realizado com sucesso.",
#     "saldo_atual": 25826.0
# }
#
# Validações:
#
# - success deve ser True
# - message deve informar sucesso
# - saldo_atual deve existir
# - saldo_atual deve ser maior ou igual a zero
#
############################################################

Validar PIX Realizado

    [Arguments]
    ...    ${json}


    ########################################################
    # ETAPA 1
    #
    # Valida se o PIX foi realizado com sucesso.
    #
    ########################################################

    ${success}=

    ...    Get From Dictionary

    ...    ${json}

    ...    success


    Should Be True

    ...    ${success}


    ########################################################
    # ETAPA 2
    #
    # Valida mensagem de sucesso.
    #
    ########################################################

    ${message}=

    ...    Get From Dictionary

    ...    ${json}

    ...    message


    Should Be Equal

    ...    ${message}

    ...    PIX realizado com sucesso.


    ########################################################
    # ETAPA 3
    #
    # Obtém saldo retornado pela API.
    #
    ########################################################

    ${saldo}=

    ...    Get From Dictionary

    ...    ${json}

    ...    saldo_atual


    ########################################################
    # ETAPA 4
    #
    # Garante que o saldo é válido.
    #
    ########################################################

    Should Be True

    ...    ${saldo} >= 0


    ########################################################
    # Evidência
    ########################################################

    Log

    ...    PIX realizado com sucesso. Saldo atual: ${saldo}    