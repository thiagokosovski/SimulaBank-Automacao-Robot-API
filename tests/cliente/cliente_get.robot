*** Settings ***

Resource    ../../config/package.resource


*** Test Cases ***

############################################################
# CT-CLI-001
#
# Objetivo:
# Validar que um usuário autenticado consegue consultar
# seus dados através do endpoint GET /api/cliente/.
############################################################

CT-CLI-001 - GET Cliente autenticado retorna 200

    [Tags]
    ...    cliente
    ...    get
    ...    positivo
    ...    smoke
    ...    CT-CLI-001

    ########################################################
    # Cria sessão HTTP
    ########################################################

    Criar Sessão da API

    ########################################################
    # Realiza Login
    ########################################################

    Realizar Login

    ########################################################
    # Consulta Cliente
    ########################################################

    ${response}=    Consultar Cliente

    ########################################################
    # Valida Status HTTP
    ########################################################

    Validar Status HTTP
    ...    ${response}
    ...    200

    ########################################################
    # Converte resposta
    ########################################################

    ${json}=    Converter Resposta para JSON
    ...    ${response}

    ########################################################
    # Valida contrato JSON
    ########################################################

    Validar Contrato JSON
    ...    ${json}
    ...    cliente_schema.json

    ########################################################
    # Valida campos retornados
    ########################################################

    Validar Número Positivo
    ...    ${json["id"]}
    
    Validar Campo Não Vazio
    ...    ${json["username"]}

    Validar Campo Não Vazio
    ...    ${json["nome"]}

    Validar Campo Não Vazio
    ...    ${json["email"]}

    Validar Campo Não Vazio
    ...    ${json["cpf"]}

    Validar Campo Não Vazio
    ...    ${json["telefone"]}

    Validar Campo Não Vazio
    ...    ${json["data_nascimento"]}

    ########################################################
    # Registra resposta no log
    ########################################################

    Log
    ...    ${json}