*** Settings ***

Library    libraries/data_library.py


*** Test Cases ***

Teste leitura YAML


    ${dados}=    Carregar Yaml
    ...    login_data.yaml


    Log To Console
    ...    ${dados}