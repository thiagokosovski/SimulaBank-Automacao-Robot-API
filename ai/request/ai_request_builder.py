"""
============================================================
MÓDULO 8.10.9 - AI REQUEST BUILDER
============================================================

Responsabilidade:

Transformar o relatório de qualidade do projeto em um
payload padronizado para envio ao motor de IA.

Este módulo NÃO:

- chama a IA;
- realiza requisições HTTP;
- conhece OpenAI;
- conhece Azure;
- conhece IA corporativa;
- altera resultados do Robot Framework;
- altera o Allure.

Sua responsabilidade é somente:

    RELATÓRIO
        ↓
    PAYLOAD PARA IA

============================================================
"""

import json
from pathlib import Path
from typing import Dict, Any


# ============================================================
# CONFIGURAÇÃO
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "ai" / "data"

QUALITY_REPORT_FILE = (
    DATA_DIR / "ai_quality_report.json"
)


# ============================================================
# CARREGAR RELATÓRIO
# ============================================================

def load_quality_report() -> Dict[str, Any]:
    """
    Carrega o relatório de qualidade gerado
    pelos módulos anteriores.
    """

    if not QUALITY_REPORT_FILE.exists():

        raise FileNotFoundError(
            "Relatório de qualidade não encontrado:\n"
            f"{QUALITY_REPORT_FILE}"
        )

    with open(
        QUALITY_REPORT_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


# ============================================================
# CONSTRUIR REQUEST
# ============================================================

def build_ai_request(
    quality_report: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Constrói o payload padronizado para a IA.

    O formato foi criado para ser independente
    do fornecedor de IA.
    """

    report = quality_report.get(
        "report",
        {}
    )

    execution = quality_report.get(
        "execution",
        {}
    )

    failures = quality_report.get(
        "failures",
        []
    )

    risk = quality_report.get(
        "risk",
        {}
    )

    recommendations = quality_report.get(
        "recommendations",
        []
    )


    # ========================================================
    # REQUEST
    # ========================================================

    return {

        "request_type": "quality_analysis",

        "application": report.get(
            "application"
        ),

        "framework": report.get(
            "framework"
        ),

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

        "failures": failures,

        "risk": risk,

        "recommendations": recommendations,

        "instructions": {

            "objective": (
                "Analyze the software quality execution "
                "using the provided evidence."
            ),

            "expected_analysis": [

                "Identify probable root causes.",

                "Classify the failures.",

                "Estimate impact.",

                "Evaluate regression risk.",

                "Recommend additional tests.",

                "Provide release recommendations."

            ]
        }
    }


# ============================================================
# SALVAR REQUEST
# ============================================================

def save_ai_request(
    request: Dict[str, Any]
) -> Path:
    """
    Salva o payload preparado para a IA.
    """

    output_file = (
        DATA_DIR / "ai_request.json"
    )

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            request,
            file,
            indent=4,
            ensure_ascii=False
        )

    return output_file


# ============================================================
# EXECUÇÃO
# ============================================================

def main():

    print("==========================================")
    print("MÓDULO 8.10.9 - AI REQUEST BUILDER")
    print("==========================================")
    print()

    print(
        "Carregando relatório de qualidade..."
    )

    quality_report = load_quality_report()

    print(
        f"Arquivo:\n{QUALITY_REPORT_FILE}"
    )

    print()

    print(
        "Construindo payload para IA..."
    )

    request = build_ai_request(
        quality_report
    )

    output_file = save_ai_request(
        request
    )

    print()

    print(
        "Request criado:"
    )

    print(output_file)

    print()

    print(
        "=========================================="
    )

    print(
        "AI Request Builder funcionando."
    )


# ============================================================
# EXECUÇÃO DIRETA
# ============================================================

if __name__ == "__main__":

    main()