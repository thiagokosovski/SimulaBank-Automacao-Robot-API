"""
============================================================
MÓDULO 8.3
PREPARAÇÃO DOS DADOS PARA ANÁLISE DE IA
============================================================

Responsabilidade:

    Ler os resultados produzidos pelo Robot Framework / Allure
    e criar um contexto estruturado que futuramente será
    utilizado pela camada de Inteligência Artificial.

IMPORTANTE:

    Este módulo NÃO executa IA.

    Ele apenas prepara os dados.

Fluxo:

    output/
        ↓
    preparação das evidências
        ↓
    execution_context.json
        ↓
    futura análise de IA
============================================================
"""

import json
from pathlib import Path


# ============================================================
# CONFIGURAÇÕES
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

OUTPUT_DIR = PROJECT_ROOT / "output"

ALLURE_DIR = OUTPUT_DIR / "allure"

AI_DATA_DIR = PROJECT_ROOT / "ai" / "data"

EXECUTION_CONTEXT_FILE = AI_DATA_DIR / "execution_context.json"


# ============================================================
# FUNÇÕES AUXILIARES
# ============================================================

def load_json_files(directory):
    """
    Localiza arquivos JSON dentro de um diretório.

    Retorna uma lista contendo os dados carregados.
    """

    json_files = list(directory.glob("*.json"))

    data = []

    for json_file in json_files:

        try:

            with open(
                json_file,
                "r",
                encoding="utf-8"
            ) as file:

                content = json.load(file)

                data.append(
                    {
                        "file": json_file.name,
                        "content": content
                    }
                )

        except json.JSONDecodeError:

            print(
                f"[WARNING] JSON inválido ignorado: "
                f"{json_file}"
            )

    return data


# ============================================================
# COLETA DE RESULTADOS
# ============================================================

def collect_allure_results():
    """
    Coleta os arquivos de resultado produzidos pelo Allure.
    """

    result_files = list(
        ALLURE_DIR.glob("*-result.json")
    )

    results = []

    for result_file in result_files:

        try:

            with open(
                result_file,
                "r",
                encoding="utf-8"
            ) as file:

                result = json.load(file)

                results.append(result)

        except json.JSONDecodeError:

            print(
                f"[WARNING] Não foi possível ler: "
                f"{result_file.name}"
            )

    return results


# ============================================================
# EXTRAÇÃO DE DETALHES DA FALHA
# ============================================================

def extract_failure_details(result):
    """
    Extrai informações relevantes de uma execução
    que apresentou falha.

    IMPORTANTE:

        Esta função apenas coleta evidências.

        Ela não interpreta a causa da falha.
        A interpretação será responsabilidade da IA.
    """

    status_details = result.get(
        "statusDetails",
        {}
    )

    details = {
        "name": result.get(
            "name"
        ),

        "status": result.get(
            "status"
        ),

        "message": status_details.get(
            "message"
        ),

        "trace": status_details.get(
            "trace"
        ),

        "known": status_details.get(
            "known",
            False
        ),

        "muted": status_details.get(
            "muted",
            False
        ),

        "flaky": status_details.get(
            "flaky",
            False
        ),

        "categories": [],

        "steps": [],

        "attachments": []
    }

    # --------------------------------------------------------
    # CATEGORIAS
    # --------------------------------------------------------

    for label in result.get(
        "labels",
        []
    ):

        if label.get("name") == "category":

            details["categories"].append(
                label.get("value")
            )

    # --------------------------------------------------------
    # STEPS
    # --------------------------------------------------------

    for step in result.get(
        "steps",
        []
    ):

        step_data = {
            "name": step.get(
                "name"
            ),

            "status": step.get(
                "status"
            )
        }

        details["steps"].append(
            step_data
        )

    # --------------------------------------------------------
    # ANEXOS
    # --------------------------------------------------------

    for attachment in result.get(
        "attachments",
        []
    ):

        attachment_data = {
            "name": attachment.get(
                "name"
            ),

            "type": attachment.get(
                "type"
            ),

            "source": attachment.get(
                "source"
            )
        }

        details["attachments"].append(
            attachment_data
        )

    return details


# ============================================================
# ANÁLISE BÁSICA DOS RESULTADOS
# ============================================================

def analyze_results(results):

    total = len(results)

    passed = 0
    failed = 0
    broken = 0
    skipped = 0

    failures = []

    for result in results:

        status = result.get(
            "status",
            "unknown"
        )

        if status == "passed":

            passed += 1

        elif status == "failed":

            failed += 1

            failures.append(
                extract_failure_details(
                    result
                )
            )

        elif status == "broken":

            broken += 1

            failures.append(
                extract_failure_details(
                    result
                )
            )

        elif status == "skipped":

            skipped += 1

    if total > 0:

        success_rate = round(
            (passed / total) * 100,
            2
        )

    else:

        success_rate = 0

    return {
        "total": total,
        "passed": passed,
        "failed": failed,
        "broken": broken,
        "skipped": skipped,
        "success_rate": success_rate,
        "failures": failures
    }


# ============================================================
# CRIAÇÃO DO CONTEXTO
# ============================================================

def create_execution_context():

    print(
        "=========================================="
    )

    print(
        "MÓDULO 8.3 - PREPARAÇÃO DOS DADOS"
    )

    print(
        "=========================================="
    )

    print()

    print(
        f"Projeto: {PROJECT_ROOT}"
    )

    print(
        f"Allure: {ALLURE_DIR}"
    )

    print()

    # --------------------------------------------------------
    # Verificar diretório
    # --------------------------------------------------------

    if not ALLURE_DIR.exists():

        raise FileNotFoundError(
            f"Diretório Allure não encontrado: "
            f"{ALLURE_DIR}"
        )

    # --------------------------------------------------------
    # Coletar resultados
    # --------------------------------------------------------

    print(
        "Coletando resultados do Allure..."
    )

    results = collect_allure_results()

    print(
        f"Resultados encontrados: {len(results)}"
    )

    print()

    # --------------------------------------------------------
    # Analisar resultados
    # --------------------------------------------------------

    execution = analyze_results(
        results
    )

    # --------------------------------------------------------
    # Montar contexto
    # --------------------------------------------------------

    context = {

        "execution": execution,

        "environment": {
            "application": "SimulaBank",
            "framework": "Robot Framework",
            "python": "3.9",
            "robot_version": "7.4.2"
        },

        "source": {
            "allure_directory": str(
                ALLURE_DIR
            )
        }
    }

    # --------------------------------------------------------
    # Criar diretório
    # --------------------------------------------------------

    AI_DATA_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    # --------------------------------------------------------
    # Salvar contexto
    # --------------------------------------------------------

    with open(
        EXECUTION_CONTEXT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            context,
            file,
            indent=4,
            ensure_ascii=False
        )

    print()

    print(
        "Contexto da execução criado:"
    )

    print(
        EXECUTION_CONTEXT_FILE
    )

    print()

    print(
        "=========================================="
    )

    print(
        "RESUMO"
    )

    print(
        "=========================================="
    )

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
        f"Broken: {execution['broken']}"
    )

    print(
        f"Skipped: {execution['skipped']}"
    )

    print(
        f"Success Rate: "
        f"{execution['success_rate']}%"
    )


# ============================================================
# EXECUÇÃO
# ============================================================

if __name__ == "__main__":

    create_execution_context()