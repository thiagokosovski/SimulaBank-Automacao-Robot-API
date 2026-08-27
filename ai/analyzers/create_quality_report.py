import json
from pathlib import Path


# ============================================================
# MÓDULO 8.9 - CONSOLIDAÇÃO DO QUALITY REPORT
# ============================================================

print("==========================================")
print("MÓDULO 8.9 - QUALITY REPORT")
print("==========================================")


# ============================================================
# CAMINHOS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "ai" / "data"

EXECUTION_FILE = DATA_DIR / "execution_context.json"

FAILURE_ANALYSIS_FILE = DATA_DIR / "ai_quality_analysis.json"

RISK_ANALYSIS_FILE = DATA_DIR / "ai_risk_analysis.json"

OUTPUT_FILE = DATA_DIR / "ai_quality_report.json"


# ============================================================
# FUNÇÃO PARA CARREGAR JSON
# ============================================================

def load_json(file_path):

    if not file_path.exists():

        print()
        print("ERRO: arquivo não encontrado:")

        print(file_path)

        raise SystemExit(1)

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


# ============================================================
# CARREGAR DADOS
# ============================================================

print()

print("Carregando dados da execução...")

execution_data = load_json(
    EXECUTION_FILE
)


print("Carregando análise das falhas...")

failure_data = load_json(
    FAILURE_ANALYSIS_FILE
)


print("Carregando análise de risco...")

risk_data = load_json(
    RISK_ANALYSIS_FILE
)


# ============================================================
# EXTRAIR EXECUÇÃO
# ============================================================

execution = execution_data.get(
    "execution",
    {}
)


total = execution.get(
    "total",
    0
)

passed = execution.get(
    "passed",
    0
)

failed = execution.get(
    "failed",
    0
)

skipped = execution.get(
    "skipped",
    0
)

success_rate = execution.get(
    "success_rate",
    0
)


# ============================================================
# EXTRAIR FALHAS
# ============================================================

failures = failure_data.get(
    "failures",
    []
)


# ============================================================
# EXTRAIR RISCO
# ============================================================

risk = risk_data.get(
    "risk",
    {}
)


risk_score = risk.get(
    "score",
    0
)

risk_level = risk.get(
    "level",
    "UNKNOWN"
)

release_recommendation = risk.get(
    "release_recommendation",
    "UNKNOWN"
)


risk_factors = risk_data.get(
    "factors",
    []
)


recommendations = risk_data.get(
    "recommendations",
    []
)


# ============================================================
# RESUMO EXECUTIVO
# ============================================================

if failed == 0:

    execution_status = "PASSED"

else:

    execution_status = "FAILED"


if risk_level == "HIGH":

    quality_status = "HIGH RISK"

elif risk_level == "MEDIUM":

    quality_status = "MEDIUM RISK"

elif risk_level == "LOW":

    quality_status = "LOW RISK"

else:

    quality_status = "STABLE"


# ============================================================
# RESULTADO CONSOLIDADO
# ============================================================

quality_report = {

    "report": {

        "application": "SimulaBank",

        "framework": "Robot Framework",

        "execution_status": execution_status,

        "quality_status": quality_status
    },


    "execution": {

        "total": total,

        "passed": passed,

        "failed": failed,

        "skipped": skipped,

        "success_rate": success_rate
    },


    "failures": failures,


    "risk": {

        "score": risk_score,

        "level": risk_level,

        "release_recommendation":
            release_recommendation,

        "factors": risk_factors
    },


    "recommendations": recommendations,


    "ai": {

        "ready_for_ai_analysis": True,

        "analysis_source": [
            "Robot Framework execution",
            "Failure analysis",
            "Risk analysis"
        ]
    }
}


# ============================================================
# SALVAR RELATÓRIO
# ============================================================

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        quality_report,
        file,
        indent=4,
        ensure_ascii=False
    )


# ============================================================
# RESUMO
# ============================================================

print()

print("Quality Report criado:")

print(OUTPUT_FILE)

print()

print("==========================================")
print("RESUMO")
print("==========================================")

print(
    f"Status da execução: {execution_status}"
)

print(
    f"Total: {total}"
)

print(
    f"Passed: {passed}"
)

print(
    f"Failed: {failed}"
)

print(
    f"Skipped: {skipped}"
)

print(
    f"Success Rate: {success_rate}%"
)

print()

print(
    f"Quality Status: {quality_status}"
)

print(
    f"Risk Score: {risk_score}"
)

print(
    f"Risk Level: {risk_level}"
)

print(
    f"Release Recommendation: "
    f"{release_recommendation}"
)

print()

print(
    f"Falhas consolidadas: {len(failures)}"
)

print(
    f"Recomendações: {len(recommendations)}"
)

print()

print("Pronto para análise de IA: YES")