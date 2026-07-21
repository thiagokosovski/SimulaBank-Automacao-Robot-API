*** Settings ***

Resource    ../../config/package.resource



*** Test Cases ***

Consultar Cliente

    Criar Sessão da API

    Realizar Login

    ${response}=    Consultar Cliente

    Validar Status HTTP
    ...    ${response}
    ...    200

    ${json}=    Converter Resposta para JSON
    ...    ${response}

    Validar Campo Não Vazio
    ...    ${json["username"]}

    Log
    ...    ${json}