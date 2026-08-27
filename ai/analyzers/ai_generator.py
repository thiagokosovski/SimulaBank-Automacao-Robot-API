"""
============================================================
MÓDULO 8.10 - GERADOR DE ANÁLISE COM IA
============================================================

Responsabilidade:

Receber o relatório consolidado de qualidade e preparar
os dados que posteriormente serão enviados para uma IA
generativa.

IMPORTANTE:

Este módulo NÃO altera:

- Robot Framework
- Allure
- resultados dos testes
- histórico
- execução dos testes

Ele trabalha exclusivamente dentro da pasta ai/.
============================================================
"""

import json
from pathlib import Path


# ============================================================
# CONFIGURAÇÃO DE CAMINHOS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

AI_DATA_DIR = PROJECT_ROOT / "ai" / "data"

INPUT_FILE = AI_DATA_DIR / "ai_quality_report.json"

OUTPUT_FILE = AI_DATA_DIR / "ai_quality_report_ai.json"


# ============================================================
# FUNÇÕES
# ============================================================

def load_quality_report():
    """
    Carrega o relatório consolidado produzido pelo Módulo 8.9.
    """

    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Relatório não encontrado: {INPUT_FILE}"
        )

    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def build_ai_context(report):
    """
    Prepara somente as informações relevantes para a IA.
    """

    return {
        "application": report["report"]["application"],
        "framework": report["report"]["framework"],
        "execution": report["execution"],
        "failures": report["failures"],
        "risk": report["risk"],
        "recommendations": report["recommendations"]
    }


def create_output(context):
    """
    Cria a estrutura que futuramente receberá
    a análise da IA generativa.
    """

    result = {
        "ai_analysis": {
            "status": "READY",
            "provider": None,
            "model": None,
            "summary": None,
            "failure_analysis": [],
            "risk_analysis": None,
            "recommendations": []
        },
        "source": context
    }

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


# ============================================================
# EXECUÇÃO PRINCIPAL
# ============================================================

def main():

    print("==========================================")
    print("MÓDULO 8.10 - PREPARAÇÃO PARA IA")
    print("==========================================")
    print()

    print(f"Entrada:")
    print(INPUT_FILE)
    print()

    report = load_quality_report()

    context = build_ai_context(report)

    create_output(context)

    print("Contexto preparado para IA:")
    print(OUTPUT_FILE)
    print()

    print("==========================================")
    print("RESUMO")
    print("==========================================")

    print(
        f"Total de testes: "
        f"{context['execution']['total']}"
    )

    print(
        f"Passed: "
        f"{context['execution']['passed']}"
    )

    print(
        f"Failed: "
        f"{context['execution']['failed']}"
    )

    print(
        f"Risk: "
        f"{context['risk']['level']}"
    )

    print()
    print("Contexto pronto para integração com IA.")


if __name__ == "__main__":
    main()