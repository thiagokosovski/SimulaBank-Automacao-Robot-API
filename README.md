# SimulaBank - Automação de APIs com Robot Framework

![Robot Framework Tests](https://github.com/thiagokosovski/SimulaBank-Automacao-Robot-API/actions/workflows/robot-tests.yml/badge.svg)

Projeto de automação de testes de APIs REST utilizando **Robot Framework**,
desenvolvido com foco em uma arquitetura organizada e reutilizável 

O projeto tem como objetivo demonstrar a construção de um framework de
automação de APIs desde a execução dos testes até a integração contínua
com GitHub Actions.

---

# Objetivo do Projeto

O objetivo principal é automatizar e validar diferentes comportamentos
de uma API bancária, contemplando não apenas cenários positivos, mas
também cenários negativos, validações de contrato e testes relacionados
à segurança e autenticação.

O framework foi estruturado buscando separar claramente as responsabilidades
entre:

- Testes
- Keywords de negócio
- Keywords HTTP
- Validações
- Schemas JSON
- Payloads
- Variáveis
- Dados de teste
- Bibliotecas Python
- Configuração de ambiente
- Relatórios
- Pipeline CI/CD

Essa separação permite que os testes sejam mais simples de ler, enquanto
a complexidade da automação permanece concentrada nas camadas responsáveis.

---

# Objetivos Técnicos

O projeto busca demonstrar conhecimentos em:

- Automação de APIs REST
- Robot Framework
- Testes funcionais de API
- Testes positivos
- Testes negativos
- Testes de segurança
- Autenticação JWT
- Validação de status HTTP
- Validação de respostas JSON
- Validação de JSON Schema
- Reutilização de keywords
- Separação de responsabilidades
- Dados de teste externos
- Variáveis de ambiente
- Bibliotecas Python auxiliares
- Git e GitHub
- GitHub Actions
- Integração contínua
- Geração de relatórios
- Organização de framework de automação

---

# Escopo da Automação

Atualmente o projeto possui automações organizadas por domínio da API.

Os módulos implementados incluem:

- Health
- Auth
- Cliente
- Conta
- Extrato
- Depósito
- Saque

Cada módulo pode possuir diferentes categorias de testes:

```text
Testes positivos
        ↓
Testes negativos
        ↓
Testes de segurança
        ↓
Validações de contrato
        ↓
Validações de regras de negócio


---

# Tecnologias utilizadas

O framework utiliza as seguintes tecnologias e ferramentas:

- Python 3.9
- Robot Framework
- RequestsLibrary
- JSONLibrary
- JSON Schema
- Django REST Framework
- Postman
- Git
- GitHub
- GitHub Actions
- REST API
- JWT Authentication

---

# Arquitetura do Projeto

O projeto utiliza uma arquitetura baseada na **separação de responsabilidades**.

Cada camada possui uma função específica dentro do framework, evitando
que regras de negócio, chamadas HTTP, validações e dados de teste fiquem
misturados nos arquivos de teste.

```text
SimulaBank-Automacao-Robot-API

│
├── .github
│   │
│   └── workflows
│       │
│       └── robot-tests.yml
│
│
├── config
│   │
│   ├── environment.robot
│   └── package.resource
│
│
├── libraries
│   │
│   ├── data_library.py
│   ├── env_library.py
│   ├── faker_library.py
│   └── schema_library.py
│
│
├── resources
│   │
│   ├── keywords
│   │
│   │   ├── auth_keywords.robot
│   │   ├── cliente_keywords.robot
│   │   ├── common_keywords.robot
│   │   ├── conta_keywords.robot
│   │   ├── deposito_keywords.robot
│   │   ├── extrato_keywords.robot
│   │   ├── health_keywords.robot
│   │   └── saque_keywords.robot
│   │
│   │
│   ├── payloads
│   │
│   │   ├── deposito
│   │   │   ├── deposito_caracteres.json
│   │   │   ├── deposito_negativo.json
│   │   │   ├── deposito_valido.json
│   │   │   └── deposito_zero.json
│   │   │
│   │   ├── saque
│   │   │   ├── saque_maior_saldo.json
│   │   │   ├── saque_negativo.json
│   │   │   ├── saque_valido.json
│   │   │   └── saque_zero.json
│   │   │
│   │   ├── login.json
│   │   └── login_extrato_vazio.json
│   │
│   │
│   ├── schemas
│   │
│   │   ├── cliente_schema.json
│   │   ├── conta_schema.json
│   │   ├── error_schema.json
│   │   ├── extrato_schema.json
│   │   ├── health_schema.json
│   │   └── login_schema.json
│   │
│   │
│   ├── validations
│   │
│   │   ├── deposito_validations.robot
│   │   ├── error_validations.robot
│   │   ├── extrato_validations.robot
│   │   ├── http_validations.robot
│   │   ├── saque_validations.robot
│   │   ├── schema_validations.robot
│   │   └── security_validations.robot
│   │
│   │
│   └── variables
│       │
│       ├── api_variables.robot
│       ├── auth_variables.robot
│       └── endpoint_variables.robot
│
│
├── scripts
│   │
│   └── robot_summary.py
│
│
├── test_data
│   │
│   └── login_data.yaml
│
│
├── tests
│   │
│   ├── Auth
│   ├── Cliente
│   ├── Conta
│   ├── Deposito
│   ├── Extrato
│   ├── Health
│   └── Saque
│
│
├── results
│
│
├── requirements.txt
├── run_tests.bat
├── run_tests.ps1
├── .env.example
└── README.md




# Organização dos Testes

Os testes são organizados por **domínio funcional da API**.

Cada módulo pode possuir diferentes arquivos de teste, separados de
acordo com o tipo de comportamento que está sendo validado.

```text
tests/
│
├── Auth
│
├── Cliente
│
├── Conta
│
├── Deposito
│
├── Extrato
│
├── Health
│
└── Saque


---

# Instalação

## Pré-requisitos

Antes de executar o projeto, é necessário possuir:

- Python 3.9
- Git
- Ambiente virtual Python
- Acesso à API SimulaBank
- Credenciais válidas para execução dos testes

---

# Clonando o Projeto

Clonar o repositório:

```bash
git clone https://github.com/thiagokosovski/SimulaBank-Automacao-Robot-API.git



# Roadmap

## Concluído

- [x] API Health
- [x] API Auth
- [x] API Cliente
- [x] API Conta
- [x] API Extrato
- [x] API Depósito
- [x] API Saque
- [x] Testes positivos
- [x] Testes negativos
- [x] Testes de segurança
- [x] Autenticação JWT
- [x] Validações centralizadas
- [x] Validação de JSON Schema
- [x] GitHub Actions
- [x] Relatórios automatizados

## Próximas evoluções

- [ ] API PIX
- [ ] API Documentos
- [ ] Paginação e filtros
- [ ] Validação de contratos OpenAPI
- [ ] Execução em múltiplos ambientes
- [ ] Integração com ferramentas de gestão de testes
- [ ] Testes Data Driven avançados
- [ ] Geração de massa dinâmica com Faker