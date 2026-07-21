*** Settings ***

Resource    ../../config/package.resource


*** Test Cases ***

CT004 - Login Negativo (Data Driven)

    ########################################################
    # Cria Sessão HTTP
    ########################################################

    Criar Sessão da API

    ########################################################
    # Executa todos os cenários negativos
    ########################################################

    Executar Cenários Negativos de Login