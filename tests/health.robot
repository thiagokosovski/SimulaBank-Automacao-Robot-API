*** Settings ***
Library    RequestsLibrary

*** Variables ***
${BASE_URL}    http://127.0.0.1:8000

*** Test Cases ***
Validar Health Check da API

    Create Session    simulabank    ${BASE_URL}

    ${response}=    GET On Session
    ...    simulabank
    ...    /api/health/

    Status Should Be    200    ${response}

    Should Be Equal As Strings
    ...    ${response.json()["status"]}
    ...    online