# SimulaBank - AI Quality Analysis

## Módulo de Inteligência Artificial para Quality Engineering

Este módulo adiciona uma camada de Inteligência Artificial ao processo
de automação de testes.

A responsabilidade deste módulo é analisar os resultados das execuções
automatizadas e produzir informações complementares sobre:

- falhas;
- possíveis causas;
- camada provável do problema;
- impacto;
- risco;
- recomendações;
- qualidade da execução;
- possíveis ações para investigação.

A IA NÃO substitui o resultado dos testes.

O resultado dos testes continua sendo produzido pelo framework de
automação.

A IA atua como uma camada de análise sobre os dados produzidos.

---

# 1. Objetivo

O objetivo é transformar:

    Teste falhou
        |
        v
    Erro encontrado
        |
        v
    Análise técnica
        |
        v
    Causa provável
        |
        v
    Impacto
        |
        v
    Risco
        |
        v
    Recomendação

Dessa forma, o projeto evolui de uma simples execução de testes para
uma plataforma de Quality Engineering orientada por dados.

---

# 2. Arquitetura

A arquitetura foi desenvolvida de forma modular.

    Robot Framework
            |
            v
        output.xml
            |
            v
    prepare_execution_data.py
            |
            v
    execution_context.json
            |
            v
    normalize_failures.py
            |
            v
    ai_analysis_context.json
            |
            v
    analyze_failures.py
            |
            v
    ai_quality_analysis.json
            |
            v
    risk_analysis
            |
            v
    ai_risk_analysis.json
            |
            v
    quality_report
            |
            v
    ai_quality_report.json
            |
            v
       AI Provider
            |
       +----+----+
       |         |
       v         v
     Local   Corporate
            |
            v
       AI Engine
            |
            v
       AI Analysis

---

# 3. Independência do Allure

Este módulo NÃO depende do Allure para funcionar.

A entrada principal da análise é o resultado do Robot Framework:

    results/output.xml

Isso permite que:

- Allure seja utilizado independentemente;
- IA seja utilizada independentemente;
- ambos sejam executados juntos no CI/CD.

Arquitetura:

    Robot Framework
       |
       +------------------> Allure
       |
       +------------------> AI Quality Analysis

O Allure continua responsável pela visualização e histórico
dos testes.

A IA é responsável pela análise inteligente dos resultados.

---

# 4. Estrutura da pasta

    ai/
    |
    +-- README.md
    |
    +-- config/
    |     |
    |     +-- ai_config.py
    |
    +-- providers/
    |     |
    |     +-- base_provider.py
    |     +-- local_provider.py
    |     +-- corporate_provider.py
    |     +-- provider_factory.py
    |
    +-- analyzers/
    |     |
    |     +-- normalize_failures.py
    |     +-- analyze_failures.py
    |     +-- risk_analyzer.py
    |     +-- quality_report.py
    |
    +-- scripts/
    |     |
    |     +-- prepare_execution_data.py
    |
    +-- data/
          |
          +-- execution_context.json
          +-- ai_analysis_context.json
          +-- ai_quality_analysis.json
          +-- ai_risk_analysis.json
          +-- ai_quality_report.json

Os arquivos dentro de `data/` são gerados durante a execução.

---

# 5. Pré-requisitos

Para executar o módulo é necessário:

- Python 3.9 ou superior;
- ambiente virtual Python recomendado;
- Robot Framework;
- execução dos testes Robot Framework;
- arquivo `results/output.xml`.

O módulo de IA foi desenvolvido para trabalhar com os resultados
produzidos pelo Robot Framework.

---

# 6. Configuração

A configuração do provider é realizada através de variáveis
de ambiente.

No arquivo `.env`:

    AI_PROVIDER=local
    AI_MODEL=test-model

---

# 7. AI_PROVIDER

Define qual motor de IA será utilizado.

Providers suportados atualmente:

    local
    openai
    azure
    corporate

Exemplo:

    AI_PROVIDER=local

ou:

    AI_PROVIDER=corporate

---

# 8. AI_MODEL

Define o modelo utilizado pelo provider.

Exemplo:

    AI_MODEL=test-model

Para uma IA corporativa:

    AI_MODEL=corporate-model

O nome do modelo depende do provider utilizado.

---

# 9. Providers

A arquitetura utiliza o padrão Provider.

Isso permite trocar o motor de IA sem alterar os analisadores
ou os testes automatizados.

Exemplo:

    AI_PROVIDER=local

utiliza:

    LocalProvider

Enquanto:

    AI_PROVIDER=corporate

utiliza:

    CorporateProvider

A seleção é realizada automaticamente pela:

    provider_factory.py

---

# 10. Segurança

Credenciais NÃO devem ser armazenadas:

- no código;
- no README;
- no Git;
- no arquivo de configuração versionado.

Credenciais devem ser fornecidas através de:

- variáveis de ambiente;
- GitHub Secrets;
- secrets do CI/CD;
- mecanismos de segurança da infraestrutura corporativa.

Exemplo:

    AI_API_KEY=********

Nunca colocar uma chave real no `.env` versionado.

---

# 11. Execução local

Primeiro execute os testes:

    robot tests

O Robot Framework deverá gerar:

    results/output.xml

Depois prepare os dados:

    python ai/scripts/prepare_execution_data.py

Depois normalize as falhas:

    python ai/analyzers/normalize_failures.py

Depois execute a análise:

    python ai/analyzers/analyze_failures.py

Depois execute a análise de risco:

    python ai/analyzers/risk_analyzer.py

Depois gere o relatório:

    python ai/analyzers/quality_report.py

---

# 12. Arquivos gerados

Durante a execução serão criados arquivos JSON dentro de:

    ai/data/

Principais arquivos:

## execution_context.json

Contém os dados básicos da execução do Robot Framework.

Exemplo:

    {
        "total": 37,
        "passed": 36,
        "failed": 1
    }

---

## ai_analysis_context.json

Contém os dados preparados para análise inteligente.

Inclui informações como:

- teste;
- status;
- mensagem de erro;
- tipo de erro;
- keyword que falhou;
- evidências;
- camada provável.

---

## ai_quality_analysis.json

Contém a análise das falhas.

Exemplo:

    {
        "probable_cause": "...",
        "confidence": 0.85,
        "recommendation": "..."
    }

---

## ai_risk_analysis.json

Contém a avaliação de risco da execução.

Exemplo:

    {
        "score": 50,
        "level": "MEDIUM",
        "release_recommendation": "REVIEW"
    }

---

## ai_quality_report.json

É o relatório consolidado.

Ele reúne:

- execução;
- falhas;
- análise;
- risco;
- recomendações;
- informações do provider.

---

# 13. Exemplo de análise

Uma execução pode apresentar:

    37 testes
    36 passed
    1 failed

A falha:

    CT-PIX-013

Mensagem:

    400 != 250

A camada de análise pode identificar:

    Categoria:
    Product defects

    Camada provável:
    API

    Impacto:
    Medium

    Keyword:
    Validar Status HTTP

A análise pode recomendar:

    Investigar o status HTTP retornado e comparar
    com o status esperado pelo cenário.

---

# 14. O que significa "IA"

O projeto separa claramente:

    Resultado do teste
            +
    Análise inteligente

O Robot Framework fornece os fatos.

O AI Engine interpreta esses fatos.

Portanto:

    Robot Framework
    =
    Evidência

    IA
    =
    Interpretação

A IA pode indicar uma causa provável, mas não deve ser considerada
uma prova definitiva de defeito.

---

# 15. IA Corporativa

O projeto foi preparado para utilização em ambientes corporativos.

A arquitetura permite utilizar uma IA interna da empresa.

Exemplo:

    AI_PROVIDER=corporate

    AI_MODEL=corporate-model

O CorporateProvider funciona inicialmente como adapter/mock.

Futuramente poderá ser conectado a:

- API interna;
- Azure OpenAI corporativo;
- gateway corporativo;
- modelo privado;
- LLM hospedado internamente.

A implementação do provider pode ser substituída sem alterar os testes.

---

# 16. Uso em outro projeto

A pasta `ai/` foi projetada para ser reutilizável.

Para utilizar em outro projeto:

    1. Copie a pasta ai/

    2. Garanta que o novo projeto possua Python.

    3. Execute os testes Robot Framework.

    4. Garanta que exista:

       results/output.xml

    5. Configure o provider no `.env`.

Exemplo mínimo:

    AI_PROVIDER=local
    AI_MODEL=test-model

Depois:

    python ai/scripts/prepare_execution_data.py

    python ai/analyzers/normalize_failures.py

    python ai/analyzers/analyze_failures.py

    python ai/analyzers/risk_analyzer.py

    python ai/analyzers/quality_report.py

---

# 17. Requisitos para reutilização

O projeto que receber a pasta `ai/` precisa fornecer:

    Python
        |
        +-- results/output.xml
        |
        +-- .env
              |
              +-- AI_PROVIDER
              +-- AI_MODEL

O módulo não precisa do Allure.

O módulo não precisa acessar o banco de dados da aplicação.

O módulo não precisa conhecer os testes individualmente.

Ele trabalha sobre os resultados produzidos pela automação.

---

# 18. GitHub Actions

No CI/CD, Allure e IA podem executar de forma independente.

Exemplo conceitual:

    GitHub Actions
          |
          v
    Robot Framework
          |
          +--------------------+
          |                    |
          v                    v
       Allure              AI Module
          |                    |
          v                    v
    GitHub Pages          AI Report

O workflow pode executar os dois módulos na mesma pipeline.

---

# 19. Segurança no GitHub Actions

Para ambientes corporativos, as credenciais devem ser configuradas
como GitHub Secrets.

Exemplo:

    AI_API_KEY

ou:

    CORPORATE_AI_TOKEN

O workflow disponibiliza a credencial como variável de ambiente.

Nunca adicionar credenciais diretamente no YAML.

---

# 20. Princípio de modularidade

Uma das principais regras deste projeto é:

    NÃO ALTERAR O QUE JÁ FUNCIONA.

O módulo de IA deve permanecer desacoplado de:

- testes Robot;
- Allure;
- código da aplicação;
- infraestrutura;
- provider específico.

Isso permite evoluir a IA sem modificar o framework de automação.

---

# 21. Evolução planejada

A arquitetura permite evoluir para:

## Análise inteligente

    Falha
      |
      v
    Causa provável
      |
      v
    Confiança
      |
      v
    Recomendação

## Análise de risco

    Histórico
      +
    Falhas
      +
    Alterações
      |
      v
    Risk Score

## Priorização inteligente

    Alterações
      +
    Histórico
      +
    Risco
      |
      v
    Testes prioritários

## Geração de cenários

Futuramente a IA poderá analisar:

- requisitos;
- contratos;
- endpoints;
- código;
- histórico de defeitos;

e sugerir novos cenários de teste.

---

# 22. Visão final

A arquitetura planejada do projeto é:

    API
      |
    Web
      |
    Testes Funcionais
      |
    Testes Negativos
      |
    Contract Testing
      |
    Segurança
      |
    Robot Framework
      |
    Playwright
      |
    CI/CD
      |
    Allure
      |
    AI Quality Analysis
      |
    Risk Analysis
      |
    AI Test Generation

Objetivo:

    Automatizar
        ↓
    Detectar
        ↓
    Analisar
        ↓
    Explicar
        ↓
    Classificar
        ↓
    Avaliar risco
        ↓
    Recomendar
        ↓
    Gerar novos testes

---

# 23. Status atual

Implementado:

- preparação dos resultados do Robot;
- normalização das falhas;
- análise das falhas;
- análise de risco;
- relatório consolidado;
- interface de AI Provider;
- configuração de AI Provider;
- Provider Factory;
- Local Provider;
- Corporate Provider (mock).

Próximas etapas:

- AI Engine;
- integração real com providers;
- análise baseada em LLM;
- histórico de execuções;
- correlação com Git;
- priorização de testes;
- geração automática de cenários de teste.