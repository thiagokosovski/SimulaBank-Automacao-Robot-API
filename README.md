# SimulaBank - Automação de APIs com Robot Framework


![Robot Framework Tests](https://github.com/thiagokosovski/SimulaBank-Automacao-Robot-API/actions/workflows/robot-tests.yml/badge.svg)


Projeto de automação de testes de APIs REST utilizando **Robot Framework**, desenvolvido para simular uma estrutura profissional de QA Automation.

O projeto tem como objetivo aplicar boas práticas utilizadas em ambientes corporativos:

- Automação de APIs REST
- Organização por camadas
- Reutilização de keywords
- Validações centralizadas
- Controle de variáveis de ambiente
- Execução contínua utilizando GitHub Actions


---

# Tecnologias utilizadas


- Python 3.9
- Robot Framework
- RequestsLibrary
- Django REST Framework
- Postman
- Git
- GitHub Actions
- REST API
- JWT Authentication


---

# Arquitetura do Projeto


```
SimulaBank-Automacao-Robot-API

│
├── config
│   │
│   ├── api_variables.robot
│   ├── environment.robot
│   └── package.resource
│
│
├── libraries
│   │
│   └── custom Python libraries
│
│
├── resources
│   │
│   ├── keywords
│   │   ├── auth_keywords.robot
│   │   ├── cliente_keywords.robot
│   │   ├── conta_keywords.robot
│   │   └── health_keywords.robot
│   │
│   └── validations
│       └── http_validations.robot
│
│
├── tests
│   │
│   ├── Auth
│   │
│   ├── Cliente
│   │
│   ├── Conta
│   │
│   └── Health
│
│
├── results
│
│
├── requirements.txt
│
│
└── .github
    │
    └── workflows
        └── robot-tests.yml

```


---

# Organização dos Testes


Os testes são separados por domínio da API.


## Health API

Validação da disponibilidade da API.


Exemplo:

```
CT-HEALTH-001
GET Health retorna API online
```



## Auth API

Testes relacionados à autenticação JWT.


Exemplos:

```
CT-AUTH-001
POST Login retorna token JWT


CT-AUTH-002
POST Login inválido retorna erro
```



## Cliente API

Testes dos endpoints de clientes.


Exemplos:

```
CT-CLI-001
GET Cliente autenticado retorna 200


CT-CLI-002
GET Cliente sem token retorna 401


CT-CLI-003
GET Cliente com token inválido retorna 401
```



## Conta API

Testes relacionados às contas bancárias.


Exemplos:

```
CT-CONTA-001
GET Conta autenticada retorna 200


CT-CONTA-002
GET Conta sem token retorna 401
```



---

# Instalação


Clonar o projeto:


```bash
git clone https://github.com/thiagokosovski/SimulaBank-Automacao-Robot-API.git
```


Criar ambiente virtual:


```bash
python -m venv venv
```


Ativar ambiente virtual:


Windows:

```bash
venv\Scripts\activate
```


Instalar dependências:


```bash
pip install -r requirements.txt
```


---

# Configuração de Ambiente


O projeto utiliza variáveis de ambiente para informações sensíveis.


Exemplo:


```
BASE_URL

API_USERNAME

API_PASSWORD
```


Localmente essas informações são carregadas através da configuração do ambiente.


No GitHub Actions elas são armazenadas utilizando:


```
Repository Settings

      ↓

Secrets and variables

      ↓

Actions
```


---

# Executando os testes localmente


Executar todos os testes:


```bash
robot tests
```


Executar somente um módulo:


Auth:

```bash
robot tests/Auth
```


Cliente:

```bash
robot tests/Cliente
```


Conta:

```bash
robot tests/Conta
```


Health:

```bash
robot tests/Health
```


---

# Execução utilizando Tags


Os testes possuem tags para facilitar a execução.


Exemplo:


Smoke tests:


```bash
robot -i smoke tests
```


Regression:


```bash
robot -i regression tests
```


---

# GitHub Actions - CI/CD


O projeto possui integração contínua utilizando GitHub Actions.


O pipeline executa automaticamente:


## Push


Quando ocorre:


```
git push origin main
```


## Pull Request


Quando uma alteração é enviada para revisão.


## Execução manual


Também é possível executar através do GitHub:


```
Actions

 ↓

Robot Framework Tests API

 ↓

Run workflow
```


---

# Pipeline de Execução


Fluxo do CI/CD:


```
Developer

    |

    |

git push

    |

    v

GitHub Actions

    |

    |

Checkout código

    |

    |

Configura Python

    |

    |

Instala dependências

    |

    |

Carrega Secrets

    |

    |

Executa Robot Framework

    |

    |

Gera relatórios

    |

    v

Resultado PASS / FAIL

```


---

# Relatórios de Execução


Após cada execução são gerados:


```
results/

├── output.xml

├── log.html

└── report.html

```


Os relatórios ficam disponíveis como artefatos no GitHub Actions.


Eles permitem analisar:


- Testes executados
- Tempo de execução
- Keywords utilizadas
- Erros encontrados
- Evidências da execução


---

# Boas práticas aplicadas


✔ Separação entre testes e recursos

✔ Keywords reutilizáveis

✔ Validações centralizadas

✔ Configuração externa

✔ Uso de variáveis de ambiente

✔ Controle de código com Git

✔ Pipeline CI/CD

✔ Relatórios automatizados

✔ Execução manual e automática


---

# Roadmap


Próximas evoluções:


- [ ] API de Extrato

- [ ] API de Depósito

- [ ] API de Saque

- [ ] API PIX

- [ ] API Documentos

- [ ] Paginação e filtros

- [ ] Validação de contratos OpenAPI

- [ ] Execução em múltiplos ambientes

- [ ] Integração com ferramentas de gestão de testes


---

# Objetivo profissional


Este projeto representa uma estrutura de automação de APIs utilizando Robot Framework seguindo conceitos aplicados em equipes profissionais de QA Automation.

O foco é demonstrar:

- Conhecimento em testes de API
- Automação com Robot Framework
- Integração contínua
- Organização de framework
- Boas práticas de engenharia de qualidade