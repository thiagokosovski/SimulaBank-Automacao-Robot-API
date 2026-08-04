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
      

############################################################
# Validar PIX para CPF Inexistente
#
# Módulo:
#
# 19.10
#
# Objetivo:
#
# Validar resposta de tentativa de PIX para CPF inexistente.
#
############################################################

Validar PIX CPF Inexistente

    [Arguments]
    ...    ${json}


    ########################################################
    # Valida campo success
    ########################################################

    ${success}=

    ...    Get From Dictionary

    ...    ${json}

    ...    success


    ${success}=

    ...    Convert To String

    ...    ${success}


    Should Be Equal

    ...    ${success}

    ...    False


    ########################################################
    # Valida mensagem
    ########################################################

    ${message}=

    ...    Get From Dictionary

    ...    ${json}

    ...    message


    Should Be Equal

    ...    ${message}

    ...    Cliente destinatário não encontrado.




############################################################
# Validar PIX com Saldo Insuficiente
#
# Módulo:
#
# 19.10.2
#
# Objetivo:
#
# Validar tentativa de PIX com valor superior ao
# saldo disponível do remetente.
#
############################################################

Validar PIX Saldo Insuficiente

    [Arguments]
    ...    ${json}


    ########################################################
    # Valida success
    ########################################################

    ${success}=

    ...    Get From Dictionary

    ...    ${json}

    ...    success


    ${success}=

    ...    Convert To String

    ...    ${success}


    Should Be Equal

    ...    ${success}

    ...    False


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
# Validar PIX para Própria Conta
#
# Objetivo:
#
# Validar que a API não permite realizar PIX
# para a própria conta do remetente.
#
# Retorno esperado:
#
# success = false
#
# message = "Não é permitido realizar PIX para a própria conta."
#
############################################################

Validar PIX para Própria Conta

    [Arguments]
    ...    ${json}


    ########################################################
    # Valida sucesso
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

    ...    Não é permitido realizar PIX para a própria conta.
    
############################################################
# Validar PIX com Valor Zero
#
# Módulo:
#
# 19.13
#
# Objetivo:
#
# Validar tentativa de PIX com valor igual a zero.
#
# Retorno esperado:
#
# {
#     "valor": [
#         "O valor do PIX deve ser maior que zero."
#     ]
# }
#
############################################################

Validar PIX Valor Zero

    [Arguments]
    ...    ${json}


    ########################################################
    # ETAPA 1
    #
    # Obtém a mensagem de validação do campo valor.
    #
    ########################################################

    ${valor}=

    ...    Get From Dictionary

    ...    ${json}

    ...    valor


    ########################################################
    # ETAPA 2
    #
    # Valida se a mensagem foi retornada.
    #
    ########################################################

    Should Not Be Empty

    ...    ${valor}


    ########################################################
    # ETAPA 3
    #
    # Valida mensagem da API.
    #
    ########################################################

    ${mensagem}=

    ...    Get From List

    ...    ${valor}

    ...    0


    Should Be Equal

    ...    ${mensagem}

    ...    O valor do PIX deve ser maior que zero.

############################################################
# Validar PIX com Valor Negativo
#
# Módulo:
#
# 19.14
#
# Objetivo:
#
# Validar tentativa de PIX com valor negativo.
#
# Retorno esperado:
#
# {
#     "valor": [
#         "O valor do PIX deve ser maior que zero."
#     ]
# }
#
############################################################

Validar PIX Valor Negativo

    [Arguments]
    ...    ${json}


    ########################################################
    # ETAPA 1
    #
    # Obtém o campo de validação "valor".
    #
    ########################################################

    ${valor}=

    ...    Get From Dictionary

    ...    ${json}

    ...    valor


    ########################################################
    # ETAPA 2
    #
    # Valida se a mensagem foi retornada.
    #
    ########################################################

    Should Not Be Empty

    ...    ${valor}


    ########################################################
    # ETAPA 3
    #
    # Obtém a primeira mensagem da lista.
    #
    ########################################################

    ${mensagem}=

    ...    Get From List

    ...    ${valor}

    ...    0


    ########################################################
    # ETAPA 4
    #
    # Valida mensagem retornada pela API.
    #
    ########################################################

    Should Be Equal

    ...    ${mensagem}

    ...    O valor do PIX deve ser maior que zero.
      

############################################################
# Validar PIX Sem Autenticação
#
# Módulo:
#
# 19.15
#
# Objetivo:
#
# Validar que a API bloqueia a realização de PIX
# sem autenticação.
#
# Retorno esperado:
#
# {
#     "detail": "Authentication credentials were not provided."
# }
#
############################################################

Validar PIX Sem Autenticação

    [Arguments]
    ...    ${json}


    ########################################################
    # ETAPA 1
    #
    # Obtém o campo "detail".
    #
    ########################################################

    ${detail}=

    ...    Get From Dictionary

    ...    ${json}

    ...    detail


    ########################################################
    # ETAPA 2
    #
    # Valida se a mensagem de segurança foi retornada.
    #
    ########################################################

    Should Not Be Empty

    ...    ${detail}


    ########################################################
    # ETAPA 3
    #
    # Valida mensagem retornada pela API.
    #
    ########################################################

    Should Be Equal

    ...    ${detail}

    ...    Authentication credentials were not provided.    
       

############################################################
# Validar PIX com Token Inválido
#
# Módulo:
#
# 19.16
#
# Objetivo:
#
# Validar que a API rejeita uma tentativa de PIX
# utilizando um token JWT inválido.
#
############################################################

Validar PIX com Token Inválido

    [Arguments]
    ...    ${json}


    ########################################################
    # ETAPA 1
    #
    # Obtém a mensagem retornada pela API.
    #
    ########################################################

    ${message}=

    ...    Get From Dictionary

    ...    ${json}

    ...    detail


    ########################################################
    # ETAPA 2
    #
    # Valida se a mensagem foi retornada.
    #
    ########################################################

    Should Not Be Empty

    ...    ${message}


    ########################################################
    # ETAPA 3
    #
    # Valida mensagem de autenticação.
    #
    ########################################################

    Should Be Equal

    ...    ${message}

    ...    Given token not valid for any token type    