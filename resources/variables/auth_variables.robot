*** Variables ***

############################################################
# Tokens utilizados nos testes negativos
#
# Estes valores são utilizados apenas para validar
# cenários de autenticação e segurança.
############################################################


############################################################
# Token completamente inválido
############################################################

${TOKEN_INVALIDO}
...    token_invalido


############################################################
# JWT malformado
#
# Estrutura:
# header.payload.signature
############################################################

${TOKEN_MALFORMADO}
...    abc123.def456.xyz999


############################################################
# Token expirado
#
# Futuramente poderá ser substituído por um JWT
# realmente expirado gerado automaticamente.
############################################################

${TOKEN_EXPIRADO}
...    eyJhbGciOiJIUzI1NiJ9.expirado.assinatura