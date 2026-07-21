*** Settings ***

Library    ../../libraries/schema_library.py


*** Keywords ***

Validar Contrato JSON

    [Arguments]
    ...    ${json_response}
    ...    ${schema_file}


    Validar Schema
    ...    ${json_response}
    ...    ${schema_file}