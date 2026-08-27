# ============================================================
# MÓDULO 8.5
# ANÁLISE DAS FALHAS
# ============================================================
#
# Responsabilidade:
#
# Ler o contexto preparado pelo Módulo 8.4 e produzir uma
# análise estruturada das falhas encontradas na execução.
#
# IMPORTANTE:
#
# Este módulo NÃO utiliza Allure.
#
# Entrada:
#
# ai/data/ai_analysis_context.json
#
# Saída:
#
# ai/data/ai_quality_analysis.json
#
# Nesta primeira versão não existe IA externa ainda.
#
# Estamos criando uma camada determinística de análise que
# posteriormente poderá ser substituída/complementada por IA.
#
# ============================================================

import json
from pathlib import Path


# ============================================================
# CONFIGURAÇÃO DE CAMINHOS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_FILE = (
    PROJECT_ROOT
    / "ai"
    / "data"
    / "ai_analysis_context.json"
)

OUTPUT_FILE = (
    PROJECT_ROOT
    / "ai"
    / "data"
    / "ai_quality_analysis.json"
)


# ============================================================
# CARREGAR CONTEXTO
# ============================================================

def load_context():

    with open(
        INPUT_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


# ============================================================
# CLASSIFICAR IMPACTO
# ============================================================

def classify_impact(
    error_type,
    probable_layer,
    message
):

    message_lower = message.lower()

    # --------------------------------------------------------
    # Erros de autenticação
    # --------------------------------------------------------

    if (
        "401" in message_lower
        or "403" in message_lower
        or "authentication" in message_lower
        or "token" in message_lower
    ):

        return "High"


    # --------------------------------------------------------
    # Erros HTTP 5xx
    # --------------------------------------------------------

    if (
        "500" in message_lower
        or "502" in message_lower
        or "503" in message_lower
        or "504" in message_lower
    ):

        return "High"


    # --------------------------------------------------------
    # Erros HTTP 4xx
    # --------------------------------------------------------

    if (
        "400" in message_lower
        or "404" in message_lower
        or "409" in message_lower
        or "422" in message_lower
    ):

        return "Medium"


    # --------------------------------------------------------
    # Erros de API
    # --------------------------------------------------------

    if probable_layer == "api":

        return "Medium"


    # --------------------------------------------------------
    # Padrão
    # --------------------------------------------------------

    return "Low"


# ============================================================
# CLASSIFICAR CATEGORIA
# ============================================================

def classify_category(
    error_type,
    probable_layer,
    message
):

    message_lower = message.lower()

    if (
        "401" in message_lower
        or "403" in message_lower
        or "token" in message_lower
        or "authentication" in message_lower
    ):

        return "Authentication"


    if (
        "400" in message_lower
        or "404" in message_lower
        or "409" in message_lower
        or "422" in message_lower
    ):

        return "Product defects"


    if (
        "500" in message_lower
        or "502" in message_lower
        or "503" in message_lower
        or "504" in message_lower
    ):

        return "Server error"


    if error_type == "http":

        return "HTTP"


    if probable_layer == "api":

        return "API"


    return "Unknown"


# ============================================================
# GERAR ANÁLISE DE UMA FALHA
# ============================================================

def analyze_failure(failure):

    # --------------------------------------------------------
    # Estrutura gerada pelo Módulo 8.4
    # --------------------------------------------------------

    test_data = failure.get(
        "test",
        {}
    )

    failure_data = failure.get(
        "failure",
        {}
    )

    context_data = failure.get(
        "context",
        {}
    )


    # --------------------------------------------------------
    # Dados principais
    # --------------------------------------------------------

    test_name = test_data.get(
        "name",
        "Unknown test"
    )

    message = failure_data.get(
        "message",
        ""
    )

    error_type = failure_data.get(
        "error_type",
        "unknown"
    )

    failed_keyword = failure_data.get(
        "failed_keyword",
        "Unknown keyword"
    )

    probable_layer = context_data.get(
        "probable_layer",
        "unknown"
    )


    # --------------------------------------------------------
    # Classificações
    # --------------------------------------------------------

    category = classify_category(
        error_type,
        probable_layer,
        message
    )

    impact = classify_impact(
        error_type,
        probable_layer,
        message
    )


    # --------------------------------------------------------
    # Resultado estruturado
    # --------------------------------------------------------

    return {

        "test": test_name,

        "status": "failed",

        "category": category,

        "impact": impact,

        "error_type": error_type,

        "probable_layer": probable_layer,

        "failed_keyword": failed_keyword,

        "message": message,

        "analysis": {

            "probable_cause": (
                "Falha durante a validação da resposta HTTP."
            ),

            "confidence": 0.85,

            "recommendation": (
                "Investigar o status HTTP retornado e "
                "comparar com o status esperado pelo cenário."
            )
        }
    }


# ============================================================
# FUNÇÃO PRINCIPAL
# ============================================================

def main():

    print("==========================================")
    print("MÓDULO 8.5 - ANÁLISE DAS FALHAS")
    print("==========================================")
    print()

    print("Entrada:")
    print(INPUT_FILE)
    print()


    # --------------------------------------------------------
    # Carregar dados
    # --------------------------------------------------------

    context = load_context()


    execution = context.get(
        "execution",
        {}
    )

    failures = context.get(
        "failures",
        []
    )


    # --------------------------------------------------------
    # Analisar falhas
    # --------------------------------------------------------

    analyzed_failures = []

    for failure in failures:

        analyzed = analyze_failure(
            failure
        )

        analyzed_failures.append(
            analyzed
        )


    # --------------------------------------------------------
    # Criar resultado final
    # --------------------------------------------------------

    result = {

        "execution": {

            "total": execution.get(
                "total",
                0
            ),

            "passed": execution.get(
                "passed",
                0
            ),

            "failed": execution.get(
                "failed",
                0
            ),

            "skipped": execution.get(
                "skipped",
                0
            ),

            "success_rate": execution.get(
                "success_rate",
                0
            )
        },

        "failures": analyzed_failures
    }


    # --------------------------------------------------------
    # Salvar análise
    # --------------------------------------------------------

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            result,
            file,
            indent=4,
            ensure_ascii=False
        )


    # ========================================================
    # RESUMO
    # ========================================================

    print("Análise criada:")
    print(OUTPUT_FILE)
    print()

    print("==========================================")
    print("RESUMO")
    print("==========================================")

    print(
        f"Total de testes: "
        f"{result['execution']['total']}"
    )

    print(
        f"Passed: "
        f"{result['execution']['passed']}"
    )

    print(
        f"Failed: "
        f"{result['execution']['failed']}"
    )

    print(
        f"Falhas analisadas: "
        f"{len(analyzed_failures)}"
    )

    print()


    # --------------------------------------------------------
    # Mostrar detalhes
    # --------------------------------------------------------

    for failure in analyzed_failures:

        print(
            f"Teste: "
            f"{failure['test']}"
        )

        print(
            f"Categoria: "
            f"{failure['category']}"
        )

        print(
            f"Camada provável: "
            f"{failure['probable_layer']}"
        )

        print(
            f"Impacto: "
            f"{failure['impact']}"
        )

        print(
            f"Keyword: "
            f"{failure['failed_keyword']}"
        )

        print(
            f"Mensagem: "
            f"{failure['message']}"
        )

        print()


# ============================================================
# EXECUÇÃO
# ============================================================

if __name__ == "__main__":

    main()