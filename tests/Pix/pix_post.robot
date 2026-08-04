*** Settings ***

############################################################
# Recursos compartilhados do framework
############################################################

Resource
...    ../../config/package.resource



*** Test Cases ***




############################################################
# CT-PIX-007
#
# Módulo:
#
# 19.9
#
# Objetivo:
#
# Validar o fluxo completo de um PIX.
#
# Fluxo:
#
# 1. Consultar destinatário
# 2. Capturar CPF
# 3. Consultar saldo do remetente
# 4. Consultar saldo do destinatário
# 5. Executar PIX
# 6. Consultar saldo do remetente novamente
# 7. Consultar saldo do destinatário novamente
# 8. Validar movimentação financeira
#
############################################################

CT-PIX-007 - Validar Fluxo Completo do PIX

    [Tags]
    ...    pix
    ...    e2e
    ...    positivo
    ...    smoke
    ...    CT-PIX-007


    ########################################################
    # ETAPA 1
    #
    # Consulta o destinatário.
    #
    ########################################################

    ${response_destinatario}=

    ...    Consultar Destinatário PIX


    Validar Status HTTP

    ...    ${response_destinatario}

    ...    200


    ${json_destinatario}=

    ...    Converter Resposta para JSON

    ...    ${response_destinatario}


    ########################################################
    # ETAPA 2
    #
    # Captura CPF do destinatário.
    #
    ########################################################

    ${cpf_destinatario}=

    ...    Extrair CPF do Destinatário

    ...    ${json_destinatario}


    ########################################################
    # ETAPA 3
    #
    # Consulta saldo do remetente antes do PIX.
    #
    ########################################################

    ${response_remetente_antes}=

    ...    Consultar Saldo do Remetente PIX


    Validar Status HTTP

    ...    ${response_remetente_antes}

    ...    200


    ${json_remetente_antes}=

    ...    Converter Resposta para JSON

    ...    ${response_remetente_antes}


    ${saldo_remetente_antes}=

    ...    Extrair Saldo da Conta

    ...    ${json_remetente_antes}


    ########################################################
    # ETAPA 4
    #
    # Consulta saldo do destinatário antes do PIX.
    #
    ########################################################

    ${response_destinatario_antes}=

    ...    Consultar Saldo do Destinatário PIX


    Validar Status HTTP

    ...    ${response_destinatario_antes}

    ...    200


    ${json_destinatario_antes}=

    ...    Converter Resposta para JSON

    ...    ${response_destinatario_antes}


    ${saldo_destinatario_antes}=

    ...    Extrair Saldo da Conta

    ...    ${json_destinatario_antes}


    ########################################################
    # ETAPA 5
    #
    # Define valor do PIX.
    #
    ########################################################

    ${valor_pix}=    Set Variable    100.00


    ########################################################
    # ETAPA 6
    #
    # Executa PIX.
    #
    ########################################################

    ${response_pix}=

    ...    Realizar PIX

    ...    ${cpf_destinatario}

    ...    ${valor_pix}

    ...    Pagamento de almoço


    ########################################################
    # ETAPA 7
    #
    # Valida HTTP.
    #
    ########################################################

    Validar Status HTTP

    ...    ${response_pix}

    ...    200


    ########################################################
    # ETAPA 8
    #
    # Converte resposta do PIX.
    #
    ########################################################

    ${json_pix}=

    ...    Converter Resposta para JSON

    ...    ${response_pix}


    ########################################################
    # ETAPA 9
    #
    # Valida resultado do PIX.
    #
    ########################################################

    Validar PIX Realizado

    ...    ${json_pix}


    ########################################################
    # ETAPA 10
    #
    # Consulta novamente o saldo do remetente.
    #
    ########################################################

    ${response_remetente_depois}=

    ...    Consultar Saldo do Remetente PIX


    Validar Status HTTP

    ...    ${response_remetente_depois}

    ...    200


    ${json_remetente_depois}=

    ...    Converter Resposta para JSON

    ...    ${response_remetente_depois}


    ${saldo_remetente_depois}=

    ...    Extrair Saldo da Conta

    ...    ${json_remetente_depois}


    ########################################################
    # ETAPA 11
    #
    # Consulta novamente o saldo do destinatário.
    #
    ########################################################

    ${response_destinatario_depois}=

    ...    Consultar Saldo do Destinatário PIX


    Validar Status HTTP

    ...    ${response_destinatario_depois}

    ...    200


    ${json_destinatario_depois}=

    ...    Converter Resposta para JSON

    ...    ${response_destinatario_depois}


    ${saldo_destinatario_depois}=

    ...    Extrair Saldo da Conta

    ...    ${json_destinatario_depois}


    ########################################################
    # ETAPA 12
    #
    # Valida saldo do remetente.
    #
    ########################################################

    Validar Saldo do Remetente Após PIX

    ...    ${saldo_remetente_antes}

    ...    ${saldo_remetente_depois}

    ...    ${valor_pix}


    ########################################################
    # ETAPA 13
    #
    # Valida saldo do destinatário.
    #
    ########################################################

    Validar Saldo do Destinatário Após PIX

    ...    ${saldo_destinatario_antes}

    ...    ${saldo_destinatario_depois}

    ...    ${valor_pix}


    ########################################################
    # ETAPA 14
    #
    # Evidências.
    #
    ########################################################

    Log To Console

    ...    SALDO REMETENTE ANTES: ${saldo_remetente_antes}

    Log To Console

    ...    SALDO REMETENTE DEPOIS: ${saldo_remetente_depois}

    Log To Console

    ...    SALDO DESTINATÁRIO ANTES: ${saldo_destinatario_antes}

    Log To Console

    ...    SALDO DESTINATÁRIO DEPOIS: ${saldo_destinatario_depois}

    Log To Console

    ...    VALOR PIX: ${valor_pix}