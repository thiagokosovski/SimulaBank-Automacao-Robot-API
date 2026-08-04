*** Settings ***

############################################################
# Recursos compartilhados do framework
############################################################

Resource
...    ../../config/package.resource



*** Test Cases ***


############################################################
# CT-PIX-002
#
# Módulo:
#
# 19.2
#
# Objetivo:
#
# Validar login do destinatário.
#
############################################################

CT-PIX-002 - Login do Destinatário

    [Tags]
    ...    pix
    ...    auth
    ...    positivo
    ...    smoke
    ...    CT-PIX-002


    ########################################################
    # Realiza login do destinatário
    ########################################################

    Realizar Login Destinatário PIX



############################################################
# CT-PIX-003
#
# Módulo:
#
# 19.3
#
# Objetivo:
#
# Consultar os dados do destinatário.
#
############################################################

CT-PIX-003 - Consultar Destinatário

    [Tags]
    ...    pix
    ...    cliente
    ...    get
    ...    positivo
    ...    CT-PIX-003


    ########################################################
    # Consulta os dados do destinatário
    ########################################################

    ${response}=

    ...    Consultar Destinatário PIX


    ########################################################
    # Valida status HTTP
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
    # Extrai o CPF do destinatário
    #
    # O CPF será utilizado posteriormente no PIX.
    ########################################################

    ${cpf_destinatario}=

    ...    Extrair CPF do Destinatário

    ...    ${json}


    ########################################################
    # Exibe CPF capturado
    ########################################################

    Log To Console

    ...    CPF capturado: ${cpf_destinatario}