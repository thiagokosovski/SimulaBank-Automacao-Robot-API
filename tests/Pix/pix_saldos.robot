*** Settings ***

############################################################
# Recursos compartilhados do framework
############################################################

Resource
...    ../../config/package.resource



*** Test Cases ***


############################################################
# CT-PIX-005
#
# Módulo:
#
# 19.6
#
# Objetivo:
#
# Consultar o saldo atual do destinatário antes da
# realização do PIX.
#
############################################################

############################################################
# CT-PIX-005
#
# Módulo:
#
# 19.7
#
# Objetivo:
#
# Consultar e capturar o saldo do destinatário antes
# da realização do PIX.
#
############################################################

CT-PIX-005 - Consultar Saldo do Destinatário

    [Tags]
    ...    pix
    ...    saldo
    ...    get
    ...    positivo
    ...    CT-PIX-005


    ########################################################
    # ETAPA 1
    #
    # Consulta saldo do destinatário.
    #
    ########################################################

    ${response}=

    ...    Consultar Saldo do Destinatário PIX


    ########################################################
    # ETAPA 2
    #
    # Valida status HTTP.
    #
    ########################################################

    Validar Status HTTP

    ...    ${response}

    ...    200


    ########################################################
    # ETAPA 3
    #
    # Converte resposta HTTP para JSON.
    #
    ########################################################

    ${json}=

    ...    Converter Resposta para JSON

    ...    ${response}


    ########################################################
    # ETAPA 4
    #
    # Extrai o saldo da conta.
    #
    ########################################################

    ${saldo_antes}=

    ...    Extrair Saldo da Conta

    ...    ${json}


    ########################################################
    # ETAPA 5
    #
    # Exibe saldo capturado.
    #
    ########################################################

    Log To Console

    ...    SALDO ANTES DO PIX: ${saldo_antes}
    
############################################################
# CT-PIX-006
#
# Módulo:
#
# 19.8
#
# Objetivo:
#
# Consultar e capturar o saldo do remetente antes
# da realização do PIX.
#
############################################################

CT-PIX-006 - Consultar Saldo do Remetente

    [Tags]
    ...    pix
    ...    saldo
    ...    get
    ...    positivo
    ...    CT-PIX-006


    ########################################################
    # ETAPA 1
    #
    # Consulta saldo do remetente.
    #
    ########################################################

    ${response}=

    ...    Consultar Saldo do Remetente PIX


    ########################################################
    # ETAPA 2
    #
    # Valida status HTTP.
    #
    ########################################################

    Validar Status HTTP

    ...    ${response}

    ...    200


    ########################################################
    # ETAPA 3
    #
    # Converte resposta para JSON.
    #
    ########################################################

    ${json}=

    ...    Converter Resposta para JSON

    ...    ${response}


    ########################################################
    # ETAPA 4
    #
    # Extrai saldo.
    #
    ########################################################

    ${saldo_remetente_antes}=

    ...    Extrair Saldo da Conta

    ...    ${json}


    ########################################################
    # ETAPA 5
    #
    # Exibe saldo capturado.
    #
    ########################################################

    Log To Console

    ...    SALDO DO REMETENTE ANTES DO PIX: ${saldo_remetente_antes}

