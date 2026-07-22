*** Settings ***

Resource    ../../config/package.resource


*** Test Cases ***

CT-AUTH-002 - POST Login inválido retorna erro

    [Tags]
    ...    auth
    ...    post
    ...    negativo
    ...    CT-AUTH-002

    ########################################################
    # Cria Sessão HTTP
    ########################################################

    Criar Sessão da API

    ########################################################
    # Executa todos os cenários negativos
    ########################################################

    Executar Cenários Negativos de Login