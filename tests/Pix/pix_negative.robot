*** Settings ***

############################################################
# Recursos compartilhados do framework
############################################################

Resource
...    ../../config/package.resource



*** Test Cases ***


############################################################
# CT-PIX-008
#
# Módulo:
#
# 19.10
#
# Objetivo:
#
# Validar tentativa de PIX para CPF inexistente.
#
############################################################

CT-PIX-008 - PIX para CPF inexistente retorna 404

    [Tags]
    ...    pix
    ...    negative
    ...    negativo
    ...    CT-PIX-008


    ########################################################
    # ETAPA 1
    #
    # Carrega o payload externo.
    #
    ########################################################

    ${payload}=

    ...    Load JSON From File

    ...    resources/payloads/pix/pix_cpf_inexistente.json


    ########################################################
    # ETAPA 2
    #
    # Executa PIX com CPF inexistente.
    #
    ########################################################

    ${response}=
       
    ...    Realizar PIX

    ...    ${payload}[cpf]

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

    ...    404


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
    # Valida contrato do erro.
    #
    ########################################################

    Validar PIX CPF Inexistente

    ...    ${json}
        
    ########################################################
    # Exibe retorno no console
    ########################################################

    Log To Console
    ...    ${json}   
       

CT-PIX-009 - PIX com saldo insuficiente retorna 400

    [Tags]
    ...    pix
    ...    negative
    ...    negativo
    ...    CT-PIX-009
    
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

    ${payload}=

    ...    Load JSON From File

    ...    resources/payloads/pix/pix_saldo_insuficiente.json


    ${response}=

    ...    Realizar PIX

    ...    ${cpf_destinatario}

    ...    ${payload}[valor]

    ...    ${payload}[descricao]


    Validar Status HTTP

    ...    ${response}

    ...    400


    ${json}=

    ...    Converter Resposta para JSON

    ...    ${response}


    Validar PIX Saldo Insuficiente

    ...    ${json}

   ########################################################
    # Exibe retorno no console
    ########################################################

    Log To Console
    ...    ${json}   
   



############################################################
# CT-PIX-010
#
# Módulo:
#
# 19.12
#
# Objetivo:
#
# Validar tentativa de PIX para a própria conta.
#
############################################################

CT-PIX-010 - PIX para própria conta não permitido

    [Tags]
    ...    pix
    ...    negative
    ...    negativo
    ...    CT-PIX-010

    ########################################################
    # ETAPA 1
    #
    # Realiza login do remetente e consulta seus dados.
    #
    ########################################################

    Realizar Login


    ${response_cliente}=

    ...    Realizar GET Autenticado

    ...    ${API_PREFIX}${CLIENTE_ENDPOINT}


    ########################################################
    # ETAPA 2
    #
    # Valida consulta do cliente.
    #
    ########################################################

    Validar Status HTTP

    ...    ${response_cliente}

    ...    200


    ########################################################
    # ETAPA 3
    #
    # Converte resposta para JSON.
    #
    ########################################################

    ${json_cliente}=

    ...    Converter Resposta para JSON

    ...    ${response_cliente}


    ########################################################
    # ETAPA 4
    #
    # Captura CPF do próprio remetente.
    #
    ########################################################

    ${cpf_remetente}=

    ...    Extrair CPF do Destinatário

    ...    ${json_cliente}
       
    ########################################################
    # ETAPA 1
    #
    # Carrega payload do cenário.
    #
    ########################################################

    ${payload}=

    ...    Load JSON From File

    ...    resources/payloads/pix/pix_propria_conta.json


    ########################################################
    # ETAPA 2
    #
    # Executa PIX utilizando a própria conta.
    #
    ########################################################

    ${response}=

    ...    Realizar PIX

    ...    ${cpf_remetente}

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

    ...    400


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
    # Valida regra de negócio.
    #
    ########################################################

    Validar PIX para Própria Conta

    ...    ${json}    
        
    ########################################################
    # Exibe retorno no console
    ########################################################

    Log To Console
    ...    ${json}   
   
############################################################
# CT-PIX-011
#
# Módulo:
#
# 19.13
#
# Objetivo:
#
# Validar tentativa de PIX com valor igual a zero.
#
############################################################

CT-PIX-011 - PIX com valor igual a zero

    [Tags]
    ...    pix
    ...    negative
    ...    negativo
    ...    CT-PIX-011

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
    # Carrega payload do cenário.
    #
    ########################################################

    ${payload}=

    ...    Load JSON From File

    ...    resources/payloads/pix/pix_valor_zero.json


    ########################################################
    # ETAPA 2
    #
    # Executa PIX utilizando valor zero.
    #
    ########################################################

    ${response}=

    ...    Realizar PIX

    ...    ${json_destinatario}

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

    ...    400


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
    # Valida regra de negócio.
    #
    ########################################################

    Validar PIX Valor Zero

    ...    ${json}


    ########################################################
    # ETAPA 6
    #
    # Evidência.
    #
    ########################################################

    Log To Console

    ...    ${json}


############################################################
# CT-PIX-012
#
# Módulo:
#
# 19.14
#
# Objetivo:
#
# Validar tentativa de PIX com valor negativo.
#
############################################################

CT-PIX-012 - PIX com valor negativo

    [Tags]
    ...    pix
    ...    negative
    ...    negativo
    ...    CT-PIX-012


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
    # Carrega payload do cenário.
    #
    ########################################################

    ${payload}=

    ...    Load JSON From File

    ...    resources/payloads/pix/pix_valor_negativo.json


    ########################################################
    # ETAPA 2
    #
    # Executa PIX utilizando valor negativo.
    #
    ########################################################

    ${response}=

    ...    Realizar PIX

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

    ...    400


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
    # Valida regra de negócio.
    #
    ########################################################

    Validar PIX Valor Negativo

    ...    ${json}


    ########################################################
    # ETAPA 6
    #
    # Evidência.
    #
    ########################################################

    Log To Console

    ...    ${json}
