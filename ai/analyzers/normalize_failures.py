"""
============================================================
MÓDULO 8.4
NORMALIZAÇÃO E ENRIQUECIMENTO DAS FALHAS
============================================================

Objetivo:

Transformar os dados produzidos pelo Módulo 8.3 em um
contexto estruturado para futura análise por Inteligência
Artificial.

IMPORTANTE:

Este módulo NÃO utiliza IA.

Também NÃO depende do Allure.

Entrada:

    ai/data/execution_context.json

Saída:

    ai/data/ai_analysis_context.json

Fluxo:

    Robot Framework
          |
          v
    execution_context.json
          |
          v
    Módulo 8.4
          |
          v
    ai_analysis_context.json
          |
          v
    Futuramente: IA

============================================================
"""

import json
import re
from pathlib import Path


# ============================================================
# CAMINHOS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

AI_DATA_DIR = PROJECT_ROOT / "ai" / "data"

INPUT_FILE = AI_DATA_DIR / "execution_context.json"

OUTPUT_FILE = AI_DATA_DIR / "ai_analysis_context.json"


# ============================================================
# LEITURA
# ============================================================

def load_execution_context():

    if not INPUT_FILE.exists():

        raise FileNotFoundError(
            f"Arquivo não encontrado: {INPUT_FILE}"
        )

    with open(
        INPUT_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


# ============================================================
# CLASSIFICAÇÃO DO ERRO
# ============================================================

def classify_error(message):
    """
    Faz uma classificação inicial baseada em regras.

    IMPORTANTE:

    Isto ainda NÃO é IA.

    São regras simples que ajudam a estruturar os dados.
    """

    if not message:

        return "unknown"


    message_lower = message.lower()


    # --------------------------------------------------------
    # HTTP
    # --------------------------------------------------------

    if re.search(
        r"\b(400|401|403|404|405|408|409|422|429|500|502|503|504)\b",
        message
    ):

        return "http"


    # --------------------------------------------------------
    # TIMEOUT
    # --------------------------------------------------------

    if "timeout" in message_lower:

        return "timeout"


    # --------------------------------------------------------
    # CONNECTION
    # --------------------------------------------------------

    if (
        "connection" in message_lower
        or "connectionerror" in message_lower
        or "connect" in message_lower
    ):

        return "connection"


    # --------------------------------------------------------
    # ASSERTION
    # --------------------------------------------------------

    if (
        "!=" in message
        or "==" in message
        or "expected" in message_lower
        or "assert" in message_lower
    ):

        return "assertion"


    # --------------------------------------------------------
    # JSON
    # --------------------------------------------------------

    if (
        "json" in message_lower
        or "decode" in message_lower
    ):

        return "json"


    return "unknown"


# ============================================================
# CAMADA PROVÁVEL
# ============================================================

def identify_layer(test_name, keywords, error_type):

    text = (
        test_name
        + " "
        + " ".join(
            keyword["name"]
            for keyword in keywords
        )
    ).lower()


    if error_type == "http":

        return "api"


    if "pix" in text:

        return "api"


    if "login" in text:

        return "authentication"


    if (
        "database" in text
        or "sql" in text
        or "postgres" in text
    ):

        return "database"


    if (
        "browser" in text
        or "page" in text
        or "playwright" in text
    ):

        return "web"


    return "unknown"


# ============================================================
# KEYWORD QUE FALHOU
# ============================================================

def find_failed_keyword(keywords):

    for keyword in keywords:

        if keyword.get("status") == "FAIL":

            return keyword["name"]


    return None


# ============================================================
# KEYWORDS EXECUTADAS ANTES DA FALHA
# ============================================================

def get_previous_keywords(keywords):

    failed_index = None


    for index, keyword in enumerate(keywords):

        if keyword.get("status") == "FAIL":

            failed_index = index

            break


    if failed_index is None:

        return []


    return [
        keyword["name"]
        for keyword in keywords[:failed_index]
        if keyword.get("status") == "PASS"
    ]


# ============================================================
# NORMALIZAÇÃO DE UMA FALHA
# ============================================================

def normalize_failure(failure):

    name = failure.get(
        "name",
        "Teste sem nome"
    )


    message = failure.get(
        "message",
        ""
    )


    keywords = failure.get(
        "keywords",
        []
    )


    error_type = classify_error(
        message
    )


    layer = identify_layer(
        name,
        keywords,
        error_type
    )


    failed_keyword = find_failed_keyword(
        keywords
    )


    previous_keywords = get_previous_keywords(
        keywords
    )


    return {

        "test": {

            "name": name,

            "status": "failed"
        },


        "failure": {

            "message": message,

            "error_type": error_type,

            "failed_keyword": failed_keyword
        },


        "context": {

            "probable_layer": layer,

            "previous_successful_keywords": previous_keywords
        },


        "evidence": {

            "keywords": keywords
        }
    }


# ============================================================
# PROCESSAR EXECUÇÃO
# ============================================================

def build_analysis_context(context):

    execution = context.get(
        "execution",
        {}
    )


    failures = execution.get(
        "failures",
        []
    )


    normalized_failures = []


    for failure in failures:

        normalized_failures.append(
            normalize_failure(
                failure
            )
        )


    return {

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


        "failures": normalized_failures,


        "metadata": {

            "source": "Robot Framework",

            "ai_ready": True,

            "ai_analysis": False
        }
    }


# ============================================================
# SALVAR
# ============================================================

def save_context(context):

    AI_DATA_DIR.mkdir(
        parents=True,
        exist_ok=True
    )


    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            context,
            file,
            indent=4,
            ensure_ascii=False
        )


# ============================================================
# MAIN
# ============================================================

def main():

    print("=" * 42)

    print(
        "MÓDULO 8.4 - NORMALIZAÇÃO DAS FALHAS"
    )

    print("=" * 42)

    print()


    print(
        "Entrada:"
    )

    print(
        INPUT_FILE
    )

    print()


    context = load_execution_context()


    analysis_context = build_analysis_context(
        context
    )


    save_context(
        analysis_context
    )


    execution = analysis_context[
        "execution"
    ]


    print(
        "Contexto para IA criado:"
    )

    print(
        OUTPUT_FILE
    )

    print()


    print("=" * 42)

    print("RESUMO")

    print("=" * 42)


    print(
        f"Total: {execution['total']}"
    )

    print(
        f"Passed: {execution['passed']}"
    )

    print(
        f"Failed: {execution['failed']}"
    )

    print(
        f"Success Rate: {execution['success_rate']}%"
    )


    print()


    print(
        f"Falhas preparadas para análise: "
        f"{len(analysis_context['failures'])}"
    )


    print()


if __name__ == "__main__":

    main()