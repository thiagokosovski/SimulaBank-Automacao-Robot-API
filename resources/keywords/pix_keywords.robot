*** Settings ***

############################################################
# Recursos compartilhados do framework
############################################################

Resource
...    ../../config/package.resource



*** Keywords ***


############################################################
# Consultar Destinatário PIX
#
# Módulo:
#
# 19.3
#
# Objetivo:
#
# Consultar os dados do destinatário através da API
# de clientes.
#
# Endpoint:
#
# GET /api/cliente/
#
# Fluxo:
#
# 1. Realiza login do destinatário
# 2. Executa GET autenticado
# 3. Retorna response HTTP
#
############################################################

Consultar Destinatário PIX


    ########################################################
    # ETAPA 1
    #
    # Realiza autenticação do destinatário.
    #
    ########################################################

    Realizar Login Destinatário PIX


    ########################################################
    # ETAPA 2
    #
    # Consulta os dados do cliente.
    #
    ########################################################

    ${response}=

    ...    Realizar GET Autenticado

    ...    ${API_PREFIX}${CLIENTE_ENDPOINT}


    ########################################################
    # ETAPA 3
    #
    # Retorna a resposta HTTP.
    #
    ########################################################

    RETURN

    ...    ${response}
       

############################################################
# Realizar PIX
#
# Módulo:
#
# 19.5
#
# Objetivo:
#
# Executar um PIX utilizando o remetente autenticado.
#
# Recebe:
#
# ${cpf_destinatario}
#
# ${valor}
#
# ${descricao}
#
# Fluxo:
#
# 1. Realiza login do remetente
# 2. Monta body do PIX
# 3. Insere CPF do destinatário
# 4. Executa POST autenticado
# 5. Retorna response HTTP
#
############################################################

Realizar PIX

    [Arguments]
    ...    ${cpf_destinatario}
    ...    ${valor}
    ...    ${descricao}


    ########################################################
    # ETAPA 1
    #
    # Autentica o remetente.
    #
    # O PIX será realizado utilizando o JWT do remetente.
    #
    ########################################################

    Realizar Login


    ########################################################
    # ETAPA 2
    #
    # Monta o body da requisição.
    #
    ########################################################

    ${body}=

    ...    Create Dictionary

    ...    cpf=${cpf_destinatario}

    ...    valor=${valor}

    ...    descricao=${descricao}


    ########################################################
    # ETAPA 3
    #
    # Executa POST autenticado.
    #
    ########################################################

    ${response}=

    ...    Realizar POST Autenticado

    ...    ${API_PREFIX}${PIX_ENDPOINT}

    ...    ${body}


    ########################################################
    # ETAPA 4
    #
    # Retorna response HTTP.
    #
    ########################################################

    RETURN

    ...    ${response}  
      

############################################################
# Consultar Saldo do Destinatário PIX
#
# Módulo:
#
# 19.6
#
# Objetivo:
#
# Consultar o saldo atual da conta do destinatário.
#
# Fluxo:
#
# 1. Realiza login do destinatário
# 2. Consulta conta
# 3. Retorna response HTTP
#
############################################################

Consultar Saldo do Destinatário PIX

    ########################################################
    # ETAPA 1
    #
    # Realiza login do destinatário.
    #
    ########################################################

    Realizar Login Destinatário PIX


    ########################################################
    # ETAPA 2
    #
    # Consulta os dados da conta.
    #
    ########################################################

    ${response}=

    ...    Realizar GET Autenticado

    ...    ${API_PREFIX}${CONTA_ENDPOINT}


    ########################################################
    # ETAPA 3
    #
    # Retorna response HTTP.
    #
    ########################################################

    RETURN

    ...    ${response}
   

############################################################
# Consultar Saldo do Remetente PIX
#
# Módulo:
#
# 19.8
#
# Objetivo:
#
# Consultar o saldo atual da conta do remetente
# antes da realização do PIX.
#
# Fluxo:
#
# 1. Realiza login do remetente
# 2. Consulta conta
# 3. Retorna response HTTP
#
############################################################

Consultar Saldo do Remetente PIX


    ########################################################
    # ETAPA 1
    #
    # Realiza login do remetente.
    #
    ########################################################

    Realizar Login


    ########################################################
    # ETAPA 2
    #
    # Consulta os dados da conta.
    #
    ########################################################

    ${response}=

    ...    Realizar GET Autenticado

    ...    ${API_PREFIX}${CONTA_ENDPOINT}


    ########################################################
    # ETAPA 3
    #
    # Retorna response HTTP.
    #
    ########################################################

    RETURN

    ...    ${response}