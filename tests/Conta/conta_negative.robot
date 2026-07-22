*** Settings ***

Resource    ../../config/package.resource



*** Test Cases ***

CT-CONTA-002 - GET Conta sem token retorna 401

    [Tags]
    ...    conta
    ...    get
    ...    negativo
    ...    CT-CONTA-002


    Criar Sessão da API


    ${response}=    GET On Session
    ...    simulabank
    ...    ${API_PREFIX}${CONTA_ENDPOINT}
    ...    expected_status=anything


    Validar Status HTTP
    ...    ${response}
    ...    401