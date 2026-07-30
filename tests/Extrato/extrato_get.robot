*** Settings ***

############################################################
# Documentação do teste
############################################################

Documentation
...    Testes automatizados do endpoint Extrato
...    Valida consulta autenticada de movimentações.


############################################################
# Recursos compartilhados do framework
############################################################

Resource
...    ../../config/package.resource



*** Test Cases ***


############################################################
# CT-EXT-001
#
# Objetivo:
#
# Validar que um usuário autenticado consegue consultar
# seu extrato bancário.
#
# Endpoint:
#
# GET /api/extrato/
#
# Validações:
#
# - Status HTTP 200
# - Contrato JSON
# - Existência de movimentações
# - Campos obrigatórios
# - Regras de negócio do extrato
#
############################################################


CT-EXT-001 - GET Extrato autenticado retorna 200


    [Tags]
    ...    extrato
    ...    get
    ...    positivo
    ...    smoke
    ...    CT-EXT-001



    

    ########################################################
    # Consulta o endpoint Extrato
    #
    # A keyword é responsável por:
    #
    # - Realizar Login
    # - Gerar JWT
    # - Criar Header Authorization
    # - Executar GET /api/extrato/
    #
    ########################################################

    ${response}=    
    ...    Consultar Extrato



    ########################################################
    # Valida retorno HTTP
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
    # Converte resposta HTTP para JSON
    #
    # Permite acessar os dados retornados
    #
    ########################################################

    ${json}=    
    ...    Converter Resposta para JSON
    ...    ${response}

 

    ########################################################
    # Valida contrato da resposta
    #
    # Verifica se o JSON segue o schema esperado:
    #
    # - Estrutura
    # - Campos existentes
    # - Tipos dos dados
    #
    ########################################################

    Validar Contrato JSON
    ...    ${json}
    ...    extrato_schema.json



    ########################################################
    # Valida regras específicas do Extrato
    #
    # Essa keyword contém:
    #
    # - Lista não vazia
    # - Quantidade de registros
    # - Campos obrigatórios
    # - Valores válidos
    # - Tipos de movimentação
    #
    # Mantém o teste limpo e reutilizável
    #
    ########################################################

    Validar Extrato Retornado
    ...    ${json}



    ########################################################
    # Exibe retorno completo no console
    #
    # Útil para análise durante desenvolvimento
    #
    ########################################################

    Log To Console
    ...    ${json}