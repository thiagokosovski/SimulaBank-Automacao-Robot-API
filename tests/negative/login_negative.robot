*** Settings ***

Resource    ../../config/package.resource



*** Test Cases ***

CT004 - Login com senha inválida


    ########################################################
    # Cria sessão HTTP
    ########################################################

    Criar Sessão da API



    ########################################################
    # Monta dados inválidos
    ########################################################

    ${body}=    Create Dictionary
    ...    username=usuario_teste
    ...    password=senha_errada



    ########################################################
    # Executa login
    ########################################################

    ${response}=    Realizar POST
    ...    ${API_PREFIX}${LOGIN_ENDPOINT}
    ...    ${body}



    ########################################################
    # Valida Status HTTP esperado
    ########################################################

    Validar Status HTTP
    ...    ${response}
    ...    401



    ########################################################
    # Converte resposta para JSON
    ########################################################

    ${json}=    Converter Resposta para JSON
    ...    ${response}



    ########################################################
    # Exibe retorno da API
    ########################################################

    Log To Console
    ...    ${json}