*** Settings ***

Resource    ../../config/package.resource



*** Test Cases ***

CT005 - Consultar conta sem autenticacao


    Criar Sessão da API


    ${response}=    GET On Session
    ...    simulabank
    ...    ${API_PREFIX}${CONTA_ENDPOINT}
    ...    expected_status=anything


    Validar Status HTTP
    ...    ${response}
    ...    401