# 🤖 Robot Framework API Execution




        ## Workflow Information

        | Item | Value |
        |------|-------|
        | Workflow | Local Execution |
        | Repository | Local |
        | Branch | Local |
        | Commit | Local |
        | Runner | Local |
        | Python | 3.9.0 |


        ## Environment Variables

        | Variable | Status |
        |----------|--------|
        | BASE_URL | ✅ Configured |
        | API_USERNAME | ✅ Configured |
        | API_PASSWORD | ✅ Configured |


        ## 🖥 Runtime

        | Item | Value |
        |------|-------|
        | Python | Python 3.9.0 |
        | Platform | Windows |
        | Architecture | AMD64 |

        


## 📊 Test Execution Summary


| Item | Value |
|------|-------|
| Suites | 8 |
| Total Tests | 36 |
| Passed | ✅ 36 |
| Failed | ❌ 0 |
| Success Rate | 100.0% |



## ✅ Executed Test Cases


| Status | Test Case |
|--------|-----------|
| ✅ PASS | CT-AUTH-002 - POST Login inválido retorna erro |
| ✅ PASS | CT-AUTH-001 - POST Login retorna token JWT |
| ✅ PASS | CT-CLI-001 - GET Cliente autenticado retorna 200 |
| ✅ PASS | CT-CLI-002 - GET Cliente sem token retorna 401 |
| ✅ PASS | CT-CLI-003 - GET Cliente com token invalido retorna 401 |
| ✅ PASS | CT-CONTA-001 - GET Conta autenticada retorna 200 |
| ✅ PASS | CT-CONTA-002 - GET Conta sem token retorna 401 |
| ✅ PASS | CT-DEP-002 - Realizar Depósito Valor Zero |
| ✅ PASS | CT-DEP-003 - Realizar Depósito Com Valor Negativo |
| ✅ PASS | CT-DEP-004 - Realizar Depósito Com Valor Caracteres |
| ✅ PASS | CT-DEP-005 - Validar Depósito sem tolken |
| ✅ PASS | CT-DEP-001 - Realizar Depósito Com Valor Válido |
| ✅ PASS | CT-DEP-006 - Realizar Depósito Sem Token |
| ✅ PASS | CT-DEP-007 - Realizar Depósito Com Token Inválido |
| ✅ PASS | CT-EXT-001 - GET Extrato autenticado retorna 200 |
| ✅ PASS | CT-EXT-002 - GET Extrato usuário sem movimentações |
| ✅ PASS | CT-HEALTH-001 - GET Health retorna API online |
| ✅ PASS | CT-PIX-002 - Login do Destinatário |
| ✅ PASS | CT-PIX-003 - Consultar Destinatário |
| ✅ PASS | CT-PIX-008 - PIX para CPF inexistente retorna 404 |
| ✅ PASS | CT-PIX-009 - PIX com saldo insuficiente retorna 400 |
| ✅ PASS | CT-PIX-010 - PIX para própria conta não permitido |
| ✅ PASS | CT-PIX-011 - PIX com valor igual a zero |
| ✅ PASS | CT-PIX-012 - PIX com valor negativo |
| ✅ PASS | CT-PIX-007 - Validar Fluxo Completo do PIX |
| ✅ PASS | CT-PIX-005 - Consultar Saldo do Destinatário |
| ✅ PASS | CT-PIX-006 - Consultar Saldo do Remetente |
| ✅ PASS | CT-PIX-015 - PIX sem autenticação retorna 401 |
| ✅ PASS | CT-PIX-015 - PIX com token inválido 401 |
| ✅ PASS | CT-SAQ-002 - Realizar Saque Maior Que Saldo |
| ✅ PASS | CT-SAQ-003 - Realizar Saque Com Valor Zero |
| ✅ PASS | CT-SAQ-004 - Realizar Saque Com Valor Negativo |
| ✅ PASS | CT-SAQ-005 - Realizar Saque Com Método GET |
| ✅ PASS | CT-SAQ-001 - Realizar Saque Com Valor Válido |
| ✅ PASS | CT-SAQ-006 - Realizar Saque sem token |
| ✅ PASS | CT-SAQ-007 - Realizar Saque com token invalido |




## 📂 Robot Reports


✅ output.xml

✅ log.html

✅ report.html

