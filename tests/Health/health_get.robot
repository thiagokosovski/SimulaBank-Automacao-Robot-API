*** Settings ***

Resource    ../../config/package.resource



*** Test Cases ***

############################################################
# Teste:
# Validar se a API está online.
############################################################

CT-HEALTH-001 - GET Health retorna API online

    [Tags]
    ...    health
    ...    get
    ...    positivo
    ...    smoke
    ...    CT-HEALTH-001


    ################################################
    # Executa validação completa do Health
    ################################################

    Validar Health API