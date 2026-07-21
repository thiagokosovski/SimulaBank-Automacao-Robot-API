*** Settings ***

############################################################
# Variáveis da aplicação
############################################################

Resource    api_variables.robot

############################################################
# Keywords
############################################################

Resource    ../resources/keywords/common_keywords.robot
Resource    ../resources/keywords/auth_keywords.robot
Resource    ../resources/keywords/health_keywords.robot
Resource    ../resources/keywords/conta_keywords.robot
Resource    ../resources/keywords/cliente_keywords.robot


############################################################
# Validações
############################################################

Resource    ../resources/validations/http_validations.robot
Resource    ../resources/validations/schema_validations.robot
Resource    ../resources/validations/error_validations.robot

############################################################
# Libraries
############################################################

Library     ../libraries/data_library.py
Library     ../libraries/faker_library.py


