*** Settings ***

############################################################
# Biblioteca responsável pelas chamadas HTTP
############################################################
Library    RequestsLibrary

############################################################
# Biblioteca para trabalhar com listas e dicionários
############################################################
Library    Collections

############################################################
# Biblioteca responsável por ler as variáveis do .env
############################################################
Library    ../../libraries/env_library.py

############################################################
# Variáveis globais da API
############################################################
Resource    ../../config/package.resource

############################################################
# Keywords compartilhadas
############################################################
Resource    common_keywords.robot

############################################################
# Validações HTTP
############################################################
Resource    ../../resources/validations/http_validations.robot


*** Keywords ***

############################################################
# Realizar Login
#
# Objetivo:
# Realizar autenticação na API utilizando as credenciais
# configuradas no arquivo .env.
#
# Fluxo:
#
# 1 - Ler usuário e senha
# 2 - Criar sessão HTTP
# 3 - Montar Body
# 4 - Executar Login
# 5 - Salvar Tokens JWT
############################################################

Realizar Login

    ########################################################
    # Lê as credenciais do ambiente
    ########################################################

    ${base_url}=    Get Base Url
    ${username}=    Get Username
    ${password}=    Get Password

    ########################################################
    # Cria sessão HTTP
    ########################################################

    Create Session
    ...    simulabank
    ...    ${base_url}

    ########################################################
    # Monta Body
    ########################################################

    ${body}=    Montar Body Login
    ...    ${username}
    ...    ${password}

    ########################################################
    # Executa Login
    ########################################################

    ${response}=    Executar Login
    ...    ${body}

    ########################################################
    # Salva os Tokens
    ########################################################

    Salvar Tokens
    ...    ${response}


############################################################
# Montar Body Login
#
# Objetivo:
# Construir o JSON enviado ao endpoint de autenticação.
############################################################

Montar Body Login

    [Arguments]
    ...    ${username}
    ...    ${password}

    ${body}=    Create Dictionary
    ...    username=${username}
    ...    password=${password}

    RETURN    ${body}


############################################################
# Executar Login
#
# Objetivo:
# Enviar requisição POST para o endpoint de Login.
############################################################

Executar Login

    [Arguments]
    ...    ${body}

    ${response}=    POST On Session
    ...    simulabank
    ...    ${API_PREFIX}${TOKEN_ENDPOINT}
    ...    json=${body}

    RETURN    ${response}


############################################################
# Salvar Tokens
#
# Objetivo:
# Validar o Login e armazenar os Tokens JWT para uso
# nas próximas requisições autenticadas.
############################################################

Salvar Tokens

    [Arguments]
    ...    ${response}

    ########################################################
    # Valida Login realizado com sucesso
    ########################################################

    Validar Status HTTP
    ...    ${response}
    ...    200

    ########################################################
    # Converte resposta para JSON
    ########################################################

    ${json}=    Converter Resposta para JSON
    ...    ${response}

    ########################################################
    # Armazena Access Token
    ########################################################

    Set Global Variable
    ...    ${ACCESS_TOKEN}
    ...    ${json["access"]}

    ########################################################
    # Armazena Refresh Token
    ########################################################

    Set Global Variable
    ...    ${REFRESH_TOKEN}
    ...    ${json["refresh"]}


############################################################
# Criar Header JWT
#
# Objetivo:
# Criar o Header Authorization para chamadas protegidas.
#
# Exemplo:
#
# Authorization: Bearer eyJhbGc...
############################################################

Criar Header JWT

    ${headers}=    Create Dictionary
    ...    Authorization=Bearer ${ACCESS_TOKEN}

    RETURN    ${headers}


############################################################
# Executar Cenário Negativo de Login
#
# Objetivo:
# Executar um único cenário negativo carregado
# do arquivo YAML.
############################################################

Executar Cenário Negativo de Login

    [Arguments]
    ...    ${cenario}

    ########################################################
    # Monta Body do cenário
    ########################################################

    ${body}=    Montar Body Login
    ...    ${cenario["username"]}
    ...    ${cenario["password"]}

    ########################################################
    # Executa Login
    ########################################################

    ${response}=    Realizar POST
    ...    ${API_PREFIX}${TOKEN_ENDPOINT}
    ...    ${body}

    ########################################################
    # Valida Status HTTP
    ########################################################

    Validar Status HTTP
    ...    ${response}
    ...    ${cenario["esperado_status"]}

    ########################################################
    # Exibe retorno da API
    ########################################################

    ${json}=    Converter Resposta para JSON
    ...    ${response}

    Log
    ...    ${json}


############################################################
# Executar Cenários Negativos de Login
#
# Objetivo:
# Ler todos os cenários do arquivo login_data.yaml
# e executar cada um deles.
############################################################

Executar Cenários Negativos de Login

    ########################################################
    # Carrega os dados externos
    ########################################################

    ${dados}=    Carregar Yaml
    ...    login_data.yaml

    ${cenarios}=    Set Variable
    ...    ${dados["login_tests"]}

    ########################################################
    # Executa todos os cenários
    ########################################################

    FOR    ${cenario}    IN    @{cenarios}

        Log To Console
        ...    Executando cenário: ${cenario["nome"]}

        Executar Cenário Negativo de Login
        ...    ${cenario}

    END