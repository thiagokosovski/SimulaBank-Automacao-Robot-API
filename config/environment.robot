
*** Settings ***

Library    OperatingSystem


*** Variables ***

############################################################
# Timeout padrão das requisições
############################################################

${REQUEST_TIMEOUT}    10


*** Keywords ***

############################################################
# Keyword:
#
# Carregar variáveis de ambiente do sistema operacional.
#
# Exemplo:
# BASE_URL=http://127.0.0.1:8000
#
# Após carregada, a variável fica disponível globalmente
# para todos os testes da execução.
############################################################


Carregar Variáveis de Ambiente

    ${base_url}=    Get Environment Variable    BASE_URL

    Set Global Variable    ${BASE_URL}    ${base_url}