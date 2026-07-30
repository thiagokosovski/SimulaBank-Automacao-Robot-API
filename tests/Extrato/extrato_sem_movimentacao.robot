*** Settings ***

############################################################
# Documentação do teste
############################################################

Documentation
...    Testes automatizados do endpoint Extrato
...    Valida consulta de extrato para usuário sem movimentações.


############################################################
# Recursos compartilhados do framework
############################################################

Resource
...    ../../config/package.resource



*** Test Cases ***


############################################################
# CT-EXT-002
#
# Objetivo:
#
# Validar que um usuário autenticado,
# porém sem movimentações bancárias,
# recebe um extrato vazio.
#
#
# Endpoint
#
# GET /api/extrato/
#
#
# Usuário utilizado
#
# Cliente exclusivo sem movimentações.
#
#
# Validações
#
# ✔ HTTP 200
# ✔ Contrato JSON
# ✔ Lista vazia
#
############################################################


CT-EXT-002 - GET Extrato usuário sem movimentações


    [Tags]
    ...    extrato
    ...    get
    ...    positivo
    ...    smoke
    ...    vazio
    ...    CT-EXT-002



    ########################################################
    # Cria sessão HTTP
    ########################################################

    Criar Sessão da API



    ########################################################
    # Consulta o extrato utilizando o usuário
    # exclusivo sem movimentações.
    #
    # A keyword realiza:
    #
    # - Login
    # - Geração do JWT
    # - Header Authorization
    # - GET /api/extrato/
    #
    ########################################################

    ${response}=
    ...    Consultar Extrato Usuário Vazio



    ########################################################
    # Valida Status HTTP
    #
    # Esperado:
    #
    # HTTP 200 OK
    #
    ########################################################

    Validar Status HTTP
    ...    ${response}
    ...    200



    ########################################################
    # Converte resposta para JSON
    ########################################################

    ${json}=
    ...    Converter Resposta para JSON
    ...    ${response}



    ########################################################
    # Valida contrato JSON
    #
    # Mesmo sem registros,
    # a estrutura do retorno deve continuar válida.
    #
    ########################################################

    Validar Contrato JSON
    ...    ${json}
    ...    extrato_schema.json



    ########################################################
    # Valida que o extrato retornou vazio
    #
    # Esperado:
    #
    # []
    #
    ########################################################

    Should Be Empty
    ...    ${json}



    ########################################################
    # Exibe retorno para facilitar análise
    ########################################################

    Log To Console

    ...    Extrato retornado: ${json}