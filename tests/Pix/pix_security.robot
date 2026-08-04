*** Settings ***

############################################################
# Recursos compartilhados do framework
############################################################

Resource
...    ../../config/package.resource



*** Test Cases ***


############################################################
# CT-PIX-015
#
# Módulo:
#
# 19.15
#
# Objetivo:
#
# Validar que não é possível realizar PIX sem autenticação.
#
############################################################

CT-PIX-015 - PIX sem autenticação retorna 401

    [Tags]
    ...    pix
    ...    security
    ...    security
    ...    negativo
    ...    CT-PIX-015

    ############################################################
    # ETAPA 1
    #
    # Consulta o destinatário.
    #
    ############################################################

    ${response_destinatario}=

    ...    Consultar Destinatário PIX


    Validar Status HTTP

    ...    ${response_destinatario}

    ...    200


    ${json_destinatario}=

    ...    Converter Resposta para JSON

    ...    ${response_destinatario}


    ############################################################
    # ETAPA 2
    #
    # Captura CPF do destinatário.
    #
    ############################################################

    ${cpf_destinatario}=

    ...    Extrair CPF do Destinatário

    ...    ${json_destinatario}
   

    ########################################################
    # ETAPA 1
    #
    # Carrega payload válido.
    #
    ########################################################

    ${payload}=

    ...    Load JSON From File

    ...    resources/payloads/pix/pix_post_200.json


    ########################################################
    # ETAPA 2
    #
    # Executa PIX sem JWT.
    #
    ########################################################

    ${response}=

    ...    Realizar PIX Sem Autenticação

    ...    ${cpf_destinatario}

    ...    ${payload}[valor]

    ...    ${payload}[descricao]


############################################################
# ETAPA 3
#
# Valida status HTTP.
#
############################################################

    Validar Status HTTP

    ...    ${response}

    ...    401


    ############################################################
    # ETAPA 4
    #
    # Converte resposta para JSON.
    #
    ############################################################

    ${json}=

    ...    Converter Resposta para JSON

    ...    ${response}


    ############################################################
    # ETAPA 5
    #
    # Valida comportamento de segurança.
    #
    ############################################################

    Validar PIX Sem Autenticação

    ...    ${json}
    

    Log To Console

    ...    ${json}



############################################################
# CT-PIX-015
#
# Módulo:
#
# 19.15
#
# Objetivo:
#
# Validar que não é possível realizar PIX sem autenticação.
#
############################################################

CT-PIX-015 - PIX com token inválido 401

    [Tags]
    ...    pix
    ...    security
    ...    security
    ...    negativo
    ...    CT-PIX-015

    ############################################################
    # ETAPA 1
    #
    # Consulta o destinatário.
    #
    ############################################################

    ${response_destinatario}=

    ...    Consultar Destinatário PIX


    Validar Status HTTP

    ...    ${response_destinatario}

    ...    200


    ${json_destinatario}=

    ...    Converter Resposta para JSON

    ...    ${response_destinatario}


    ############################################################
    # ETAPA 2
    #
    # Captura CPF do destinatário.
    #
    ############################################################

    ${cpf_destinatario}=

    ...    Extrair CPF do Destinatário

    ...    ${json_destinatario}
   

    ########################################################
    # ETAPA 1
    #
    # Carrega payload válido.
    #
    ########################################################

    ${payload}=

    ...    Load JSON From File

    ...    resources/payloads/pix/pix_post_200.json


    ########################################################
    # ETAPA 2
    #
    # Executa PIX sem JWT.
    #
    ########################################################

    ${response}=

    ...    Realizar PIX com Token Inválido

    ...    ${cpf_destinatario}

    ...    ${payload}[valor]

    ...    ${payload}[descricao]


    ########################################################
    # ETAPA 3
    #
    # Valida status HTTP.
    #
    ########################################################

    Validar Status HTTP

    ...    ${response}

    ...    401


    ########################################################
    # ETAPA 4
    #
    # Converte resposta para JSON.
    #
    ########################################################

    ${json}=

    ...    Converter Resposta para JSON

    ...    ${response}


    ########################################################
    # ETAPA 5
    #
    # Valida retorno de segurança.
    #
    ########################################################

    Validar PIX com Token Inválido

    ...    ${json}


    ########################################################
    # ETAPA 6
    #
    # Exibe retorno no console.
    #
    ########################################################

    Log To Console

    ...    ${json}