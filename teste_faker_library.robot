*** Settings ***

Resource    config/package.resource



*** Test Cases ***

Teste Faker Data Factory


    ${nome}=    Gerar Nome Aleatorio


    ${email}=    Gerar Email Aleatorio


    ${cpf}=    Gerar CPF Aleatorio


    ${telefone}=    Gerar Telefone Aleatorio



    Log To Console
    ...    Nome: ${nome}



    Log To Console
    ...    Email: ${email}



    Log To Console
    ...    CPF: ${cpf}



    Log To Console
    ...    Telefone: ${telefone}