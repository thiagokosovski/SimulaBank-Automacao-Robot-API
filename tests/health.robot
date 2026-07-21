*** Settings ***

Resource    ../config/package.resource



*** Test Cases ***

############################################################
# Teste:
# Validar se a API está online.
############################################################

Validar Health Check


    ################################################
    # Executa validação completa do Health
    ################################################

    Validar Health API