*** Settings ***

############################################################
# Configuração do Ambiente
#
# Centraliza as configurações do ambiente de execução.
#
# Exemplos:
# - BASE_URL
# - Ambiente (DEV/HML/PROD)
# - Timeout padrão
############################################################

Resource    environment.robot


############################################################
# Variáveis da API
#
# Configurações gerais da API.
#
# Exemplos:
# - Prefixo da API (/api)
# - Content-Type
# - Accept
############################################################

Resource    ../resources/variables/api_variables.robot


############################################################
# Endpoints da API
#
# Contém todos os endpoints utilizados pelo framework.
#
# Exemplos:
# - /login/
# - /cliente/
# - /conta/
# - /extrato/
############################################################

Resource    ../resources/variables/endpoint_variables.robot


############################################################
# Variáveis de Autenticação
#
# Utilizadas exclusivamente em cenários de autenticação
# e segurança.
#
# Exemplos:
# - Token inválido
# - Token malformado
# - Token expirado
############################################################

Resource    ../resources/variables/auth_variables.robot


############################################################
# Keywords
#
# Contém todas as keywords reutilizáveis do framework.
############################################################

Resource    ../resources/keywords/common_keywords.robot
Resource    ../resources/keywords/auth_keywords.robot
Resource    ../resources/keywords/health_keywords.robot
Resource    ../resources/keywords/conta_keywords.robot
Resource    ../resources/keywords/cliente_keywords.robot


############################################################
# Validações
#
# Centraliza todas as validações utilizadas pelos testes.
############################################################

Resource    ../resources/validations/http_validations.robot
Resource    ../resources/validations/schema_validations.robot
Resource    ../resources/validations/error_validations.robot


############################################################
# Libraries
#
# Bibliotecas Python utilizadas pelo Robot Framework.
############################################################

Library     ../libraries/data_library.py
Library     ../libraries/faker_library.py
