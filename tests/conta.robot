*** Settings ***

Resource    ../config/package.resource


*** Test Cases ***

Consultar Conta

    ########################################################
    # Cria sessão HTTP
    ########################################################

    Criar Sessão da API

    ########################################################
    # Consulta a API
    ########################################################

    ${response}=    Consultar Conta

    ########################################################
    # Valida o Status HTTP
    ########################################################

    Validar Status HTTP    ${response}    200

    ########################################################
    # Converte para JSON
    ########################################################

    ${json}=    Converter Resposta para JSON    ${response}

    ########################################################
    # Valida campos
    ########################################################

    Validar Campo Igual    ${json["agencia"]}    0001

    Validar Campo Não Vazio    ${json["numero"]}

    ################################################
    # Validar contrato da conta
    ################################################

    Validar Contrato JSON
    ...    ${json}
    ...    conta_schema.json
       
    ########################################################
    # Exibe o retorno
    ########################################################

    Log To Console    ${json}




