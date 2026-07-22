*** Variables ***

############################################################
# Ambiente de execução
#
# Define a URL base utilizada pelo framework.
#
# Futuramente poderá ser carregada automaticamente
# através do arquivo .env.
############################################################

${BASE_URL}
...    http://127.0.0.1:8000


############################################################
# Timeout padrão das requisições
############################################################

${REQUEST_TIMEOUT}
...    10