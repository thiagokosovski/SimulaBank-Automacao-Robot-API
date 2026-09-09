"""
============================================================
MÓDULO 8.10.11 - AI ANALYSIS ORCHESTRATOR
============================================================

Responsabilidade:

Orquestrar o fluxo completo de análise de qualidade
assistida por IA.

Fluxo:

    EXECUTION DATA
          ↓
    NORMALIZE FAILURES
          ↓
    ANALYZE FAILURES
          ↓
    RISK ANALYSIS
          ↓
    QUALITY REPORT
          ↓
    AI REQUEST BUILDER
          ↓
    AI ENGINE
          ↓
    AI PROVIDER
          ↓
    AI RESPONSE PARSER

IMPORTANTE:

O Orchestrator não implementa a lógica específica
de nenhum provider.

Ele apenas coordena os componentes.

============================================================
"""

import subprocess
import sys
from pathlib import Path


# ============================================================
# CONFIGURAÇÃO
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]


# ============================================================
# EXECUTAR MÓDULO
# ============================================================

def run_module(module_path: str):
    """
    Executa um módulo Python.

    Args:
        module_path:
            Caminho relativo do módulo.
    """

    print()
    print("------------------------------------------")
    print(f"Executando: {module_path}")
    print("------------------------------------------")

    result = subprocess.run(
        [
            sys.executable,
            str(PROJECT_ROOT / module_path)
        ],
        cwd=PROJECT_ROOT
    )

    if result.returncode != 0:

        raise RuntimeError(
            f"Falha na execução do módulo: "
            f"{module_path}"
        )


# ============================================================
# EXECUÇÃO DO FLUXO
# ============================================================

def run_pipeline():

    print("==========================================")
    print("MÓDULO 8.10.11 - AI ANALYSIS ORCHESTRATOR")
    print("==========================================")

    print()
    print("Projeto:")
    print(PROJECT_ROOT)

    print()
    print("Iniciando pipeline de análise...")


    # ========================================================
    # ETAPA 1
    # PREPARAÇÃO DOS DADOS
    # ========================================================

    run_module(
        "ai/scripts/prepare_execution_data.py"
    )


    # ========================================================
    # ETAPA 2
    # NORMALIZAÇÃO DAS FALHAS
    # ========================================================

    run_module(
        "ai/analyzers/normalize_failures.py"
    )


    # ========================================================
    # ETAPA 3
    # ANÁLISE DAS FALHAS
    # ========================================================

    run_module(
        "ai/analyzers/analyze_failures.py"
    )


    # ========================================================
    # ETAPA 4
    # ANÁLISE DE RISCO
    # ========================================================

    run_module(
        "ai/analyzers/analyze_risk.py"
    )


    # ========================================================
    # ETAPA 5
    # QUALITY REPORT
    # ========================================================

    run_module(
        "ai/analyzers/create_quality_report.py"
    )


    # ========================================================
    # ETAPA 6
    # AI REQUEST BUILDER
    # ========================================================

    run_module(
        "ai/request/ai_request_builder.py"
    )


    # ========================================================
    # ETAPA 7
    # AI ENGINE
    # ========================================================

    run_module(
        "ai/engine/ai_engine.py"
    )


    # ========================================================
    # ETAPA 8
    # AI RESPONSE PARSER
    # ========================================================

    run_module(
        "ai/response/ai_response_parser.py"
    )

    # ========================================================
    # ETAPA 9
    # AI FINAL REPORT
    # ========================================================

    run_module(
        "ai/reports/ai_final_report.py"
    )


    # ========================================================
    # ETAPA 10
    # AI REPORT VALIDATION
    # ========================================================

    run_module(
        "ai/validators/ai_report_validator.py"
    )    

    # ========================================================
    # ETAPA 11
    # AI MARKDOWN REPORT
    # ========================================================

    run_module(
        "ai/reports/ai_markdown_report.py"
    ) 

    # ========================================================
    # ETAPA 12
    # AI REPORT PUBLISHER
    # ========================================================

    run_module(
        "ai/reports/ai_report_publisher.py"
    )   

    # ========================================================
    # FINAL
    # ========================================================

    print()
    print("==========================================")
    print("PIPELINE DE IA CONCLUÍDO")
    print("==========================================")

    print()
    print("Arquivos principais:")

    print(
        "  ai/data/execution_context.json"
    )

    print(
        "  ai/data/ai_analysis_context.json"
    )

    print(
        "  ai/data/ai_quality_analysis.json"
    )

    print(
        "  ai/data/ai_risk_analysis.json"
    )

    print(
        "  ai/data/ai_quality_report.json"
    )

    print(
        "  ai/data/ai_request.json"
    )

    print(
    "  ai/reports/ai_final_report.md"
    )

    print(
            "  ai/reports/ai_final_report.html"
        )

    print(
        "  ai/data/ai_engine_result.json"
    )

    print(
        "  ai/data/ai_response_normalized.json"
    )

    print(
        "  ai/data/ai_final_report.json"
    )

    print()
    print("Relatório final de qualidade disponível.")

# ============================================================
# EXECUÇÃO DIRETA
# ============================================================

if __name__ == "__main__":

    try:

        run_pipeline()

    except Exception as error:

        print()
        print("==========================================")
        print("ERRO NO PIPELINE")
        print("==========================================")

        print()
        print(error)

        sys.exit(1)