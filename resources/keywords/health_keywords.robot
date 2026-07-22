*** Settings ***

# Biblioteca responsável pelas requisições HTTP
Library    RequestsLibrary


# Biblioteca de validações do Robot Framework
Library    Collections


# Importa as variáveis da API
Resource    ../../config/package.resource


# Importa keywords comuns
Resource    common_keywords.robot






*** Keywords ***


############################################################
# Consultar Health
#
# Objetivo:
# Realizar uma chamada GET para o endpoint
# /api/health/ e retornar a resposta da API.
############################################################

Consultar Health

    # Executa a requisição GET

    ${response}=    GET On Session
    ...    simulabank
    ...    ${API_PREFIX}${HEALTH_ENDPOINT}


    # Retorna a resposta

    RETURN    ${response}



############################################################
# Validar Health API
#
# Objetivo:
# Validar disponibilidade da API.
#
# Fluxo:
#
# 1 - Criar sessão HTTP
# 2 - Consultar endpoint Health
# 3 - Validar HTTP 200
# 4 - Converter resposta JSON
# 5 - Validar contrato JSON
############################################################

Validar Health API


    ################################################
    # Criar sessão HTTP
    ################################################

    Criar Sessão da API



    ################################################
    # Executar consulta Health
    ################################################

    ${response}=    Consultar Health



    ################################################
    # Validar HTTP 200
    ################################################

    Validar Status HTTP
    ...    ${response}
    ...    200



    ################################################
    # Converter resposta JSON
    ################################################

    ${json}=    Converter Resposta para JSON
    ...    ${response}



    ################################################
    # Validar contrato JSON
    ################################################

    ################################################
    # Validar contrato JSON
    ################################################

    Validar Contrato JSON
    ...    ${json}
    ...    health_schema.json