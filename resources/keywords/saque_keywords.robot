*** Settings ***

############################################################
# Recursos compartilhados do framework
############################################################

Resource
...    ../../config/package.resource


*** Keywords ***

############################################################
# Realizar Saque
#
# Objetivo:
#
# Executar o endpoint de saque utilizando autenticação JWT.
#
# Recebe:
#
# ${payload_file}
#
# O payload é informado pelo teste.
#
# Exemplos:
#
# saque_valido.json
# saque_zero.json
# saque_negativo.json
#
# Fluxo:
#
# 1. Realiza login
# 2. Obtém JWT
# 3. Carrega payload
# 4. Executa POST autenticado
# 5. Retorna response HTTP
#
############################################################

Realizar Saque

    [Arguments]
    ...    ${payload_file}

    ########################################################
    # ETAPA 1
    #
    # Garante que existe uma autenticação válida.
    #
    # A keyword Realizar Login é responsável por:
    #
    # - Obter credenciais
    # - Criar sessão
    # - Executar POST /api/token/
    # - Obter JWT
    # - Salvar os tokens
    #
    ########################################################

    Realizar Login

    ########################################################
    # ETAPA 2
    #
    # Carrega o JSON informado pelo teste.
    #
    # Dessa forma a keyword não fica presa a um único
    # cenário.
    #
    ########################################################

    ${payload}=
    ...    Load JSON From File
    ...    ${payload_file}


    ########################################################
    # ETAPA 3
    #
    # Executa POST autenticado.
    #
    # A autenticação HTTP é responsabilidade do
    # common_keywords.robot.
    #
    ########################################################

    ${response}=
    ...    Realizar POST Autenticado
    ...    ${API_PREFIX}${SAQUE_ENDPOINT}
    ...    ${payload}


    ########################################################
    # ETAPA 4
    #
    # Retorna a resposta HTTP para o teste.
    #
    ########################################################

    RETURN
    ...    ${response}
    


############################################################
# Realizar Saque Com Método GET
#
# Módulo:
#
# 18.2.5
#
# Objetivo:
#
# Validar que o endpoint de saque rejeita uma requisição
# utilizando o método GET.
#
# O endpoint de saque utiliza POST.
#
# Método utilizado:
#
# GET
#
# Resposta esperada:
#
# HTTP 405 - Method Not Allowed
#
############################################################

Realizar Saque Com Método GET

    [Arguments]
    ...    ${payload_file}


    ########################################################
    # ETAPA 1
    #
    # Garante que existe uma autenticação válida.
    #
    # A keyword Realizar Login é responsável por:
    #
    # - Obter credenciais
    # - Criar sessão
    # - Executar POST /api/token/
    # - Obter JWT
    # - Salvar os tokens
    #
    ########################################################

    Realizar Login


    ########################################################
    # ETAPA 2
    #
    # Carrega o JSON informado pelo teste.
    #
    # Dessa forma a keyword não fica presa a um único
    # cenário.
    #
    ########################################################

    ${payload}=
    ...    Load JSON From File
    ...    ${payload_file}


    ########################################################
    # ETAPA 3
    #
    # Executa POST autenticado.
    #
    # A autenticação HTTP é responsabilidade do
    # common_keywords.robot.
    #
    ########################################################

    ${response}=
    ...    Realizar GET Autenticado
    ...    ${API_PREFIX}${SAQUE_ENDPOINT}


    ########################################################
    # ETAPA 4
    #
    # Retorna a resposta HTTP para o teste.
    #
    ########################################################

    RETURN
    ...    ${response}
   


Realizar Saque Sem Token

    [Arguments]
    ...    ${payload_file}


    ########################################################
    # ETAPA 1
    #
    # Garante que existe uma autenticação válida.
    #
    # A keyword Realizar Login é responsável por:
    #
    # - Obter credenciais
    # - Criar sessão
    # - Executar POST /api/token/
    # - Obter JWT
    # - Salvar os tokens
    #
    ########################################################

    Realizar Login


    ########################################################
    # ETAPA 2
    #
    # Carrega o JSON informado pelo teste.
    #
    # Dessa forma a keyword não fica presa a um único
    # cenário.
    #
    ########################################################

    ${payload}=
    ...    Load JSON From File
    ...    ${payload_file}


    ########################################################
    # ETAPA 3
    #
    # Executa POST sem autenticação.
    #
    # A autenticação HTTP é responsabilidade do
    # common_keywords.robot.
    #
    ########################################################

    ${response}=
    ...    Realizar POST Sem Autenticacao
    ...    ${API_PREFIX}${SAQUE_ENDPOINT}
    ...    ${payload}


    ########################################################
    # ETAPA 4
    #
    # Retorna a resposta HTTP para o teste.
    #
    ########################################################

    RETURN
    ...    ${response}
    


Realizar Saque com Token invalido   
   
   [Arguments]
    ...    ${payload_file}



    ########################################################
    # ETAPA 2
    #
    # Carrega o JSON informado pelo teste.
    #
    # Dessa forma a keyword não fica presa a um único
    # cenário.
    #
    ########################################################

    ${payload}=
    ...    Load JSON From File
    ...    ${payload_file}


    ########################################################
    # ETAPA 3
    #
    # Executa POST autenticado.
    #
    # A autenticação HTTP é responsabilidade do
    # common_keywords.robot.
    #
    ########################################################

    ${response}=
    ...    Realizar POST Token Invalido
    ...    ${API_PREFIX}${SAQUE_ENDPOINT}
    ...    ${payload}


    ########################################################
    # ETAPA 4
    #
    # Retorna a resposta HTTP para o teste.
    #
    ########################################################

    RETURN
    ...    ${response}
    
    