*** Settings ***

############################################################
# Biblioteca utilizada para manipulação de listas
############################################################

Library    Collections



*** Keywords ***


############################################################
# Validar Extrato Retornado
#
# Objetivo:
#
# Validar regras específicas do endpoint:
#
# GET /api/extrato/
#
# Recebe:
#
# ${json}
#
# Lista contendo as movimentações bancárias.
#
############################################################


Validar Extrato Retornado

    [Arguments]
    ...    ${json}

    
    ########################################################
    # Valida se o retorno possui dados
    #
    # O extrato de um usuário deve retornar uma lista
    # contendo movimentações.
    #
    ########################################################

    Should Not Be Empty
    ...    ${json}



    ########################################################
    # Valida quantidade de movimentações
    #
    # Garante que existe pelo menos um lançamento.
    #
    ########################################################

    ${quantidade}=
    ...    Get Length
    ...    ${json}


    Should Be True
    ...    ${quantidade} > 0



    ########################################################
    # Obtém a primeira movimentação
    #
    # Usaremos como exemplo para validar o contrato
    # dos registros retornados.
    #
    ########################################################

    ${movimento}=
    ...    Get From List
    ...    ${json}
    ...    0



    ########################################################
    # Validação dos campos obrigatórios
    #
    # Nenhum campo pode estar vazio.
    #
    ########################################################

    Validar Campo Não Vazio
    ...    ${movimento["id"]}


    Validar Campo Não Vazio
    ...    ${movimento["tipo"]}


    Validar Campo Não Vazio
    ...    ${movimento["valor"]}


    Validar Campo Não Vazio
    ...    ${movimento["descricao"]}


    Validar Campo Não Vazio
    ...    ${movimento["data"]}



    ########################################################
    # Validação do identificador
    #
    # O ID da movimentação deve ser maior que zero.
    #
    ########################################################

    Validar Número Positivo
    ...    ${movimento["id"]}



    ########################################################
    # Validação do formato monetário
    #
    # Exemplos aceitos:
    #
    # 10.00
    # 150.50
    #
    ########################################################

    Should Match Regexp
    ...    ${movimento["valor"]}
    ...    ^[0-9]+\.[0-9]{2}$



    ########################################################
    # Validação do tipo de movimentação
    #
    # Valores permitidos pela aplicação:
    #
    # DEPOSITO
    # SAQUE
    # PIX
    #
    ########################################################

    Should Contain Any
    ...    ${movimento["tipo"]}
    ...    DEPOSITO
    ...    SAQUE
    ...    PIX
    
    ############################################################
    # Validar Extrato Sem Movimentações
    ############################################################

############################################################
# Validar Extrato Vazio
#
# Objetivo:
#
# Garantir que o usuário não possui movimentações
# cadastradas.
#
############################################################

############################################################
# Validar Extrato Vazio
#
# Objetivo:
#
# Garantir que uma conta recém-criada e sem operações
# retorne uma lista vazia.
#
############################################################

Validar Extrato Vazio

    [Arguments]
    ...    ${json}

    ########################################################
    # O retorno deve ser uma lista
    ########################################################

    Should Be Equal
    ...    ${json.__class__.__name__}
    ...    list

    ########################################################
    # Deve existir zero movimentações
    ########################################################

    ${quantidade}=
    ...    Get Length
    ...    ${json}

    Should Be Equal As Integers
    ...    ${quantidade}
    ...    0