import json
from pathlib import Path


# ============================================================
# MÓDULO 8.8 - ANÁLISE DE RISCO
# ============================================================

print("==========================================")
print("MÓDULO 8.8 - ANÁLISE DE RISCO")
print("==========================================")


# ============================================================
# CAMINHOS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "ai" / "data"

ANALYSIS_FILE = DATA_DIR / "ai_quality_analysis.json"

OUTPUT_FILE = DATA_DIR / "ai_risk_analysis.json"


print()
print("Entrada:")
print(ANALYSIS_FILE)


# ============================================================
# VALIDAR ARQUIVO DE ENTRADA
# ============================================================

if not ANALYSIS_FILE.exists():

    print()
    print("ERRO: arquivo de análise não encontrado.")

    print(ANALYSIS_FILE)

    raise SystemExit(1)


# ============================================================
# CARREGAR ANÁLISE
# ============================================================

with open(
    ANALYSIS_FILE,
    "r",
    encoding="utf-8"
) as file:

    data = json.load(file)


# ============================================================
# INFORMAÇÕES DA EXECUÇÃO
# ============================================================

execution = data.get("execution", {})

total = execution.get("total", 0)

passed = execution.get("passed", 0)

failed = execution.get("failed", 0)

success_rate = execution.get("success_rate", 0)


# ============================================================
# FATORES DE RISCO
# ============================================================

risk_score = 0

risk_factors = []


# ============================================================
# FATOR 1 — TESTES FALHANDO
# ============================================================

if failed > 0:

    risk_score += 30

    risk_factors.append(
        {
            "factor": "Test failures detected",
            "impact": "HIGH",
            "description": (
                f"{failed} test(s) failed during the execution."
            )
        }
    )


# ============================================================
# FATOR 2 — TAXA DE SUCESSO
# ============================================================

if success_rate < 90:

    risk_score += 30

    risk_factors.append(
        {
            "factor": "Low success rate",
            "impact": "HIGH",
            "description": (
                f"Success rate is {success_rate}%."
            )
        }
    )

elif success_rate < 95:

    risk_score += 20

    risk_factors.append(
        {
            "factor": "Success rate below target",
            "impact": "MEDIUM",
            "description": (
                f"Success rate is {success_rate}%."
            )
        }

    )

elif success_rate < 100:

    risk_score += 10

    risk_factors.append(
        {
            "factor": "Execution contains failures",
            "impact": "LOW",
            "description": (
                f"Success rate is {success_rate}%."
            )
        }
    )


# ============================================================
# FATOR 3 — ANÁLISES DE FALHAS
# ============================================================

failures = data.get("failures", [])

for failure in failures:

    category = failure.get("category", "Unknown")

    layer = failure.get("probable_layer", "Unknown")

    impact = failure.get("impact", "Low")

    if impact.upper() == "HIGH":

        risk_score += 20

    elif impact.upper() == "MEDIUM":

        risk_score += 10

    risk_factors.append(
        {
            "factor": "Failure analysis",
            "impact": impact.upper(),
            "category": category,
            "layer": layer
        }
    )


# ============================================================
# LIMITAR SCORE
# ============================================================

if risk_score > 100:

    risk_score = 100


# ============================================================
# CLASSIFICAÇÃO DO RISCO
# ============================================================

if risk_score >= 70:

    risk_level = "HIGH"

    recommendation = "REVIEW"

elif risk_score >= 40:

    risk_level = "MEDIUM"

    recommendation = "REVIEW"

elif risk_score > 0:

    risk_level = "LOW"

    recommendation = "PROCEED_WITH_CAUTION"

else:

    risk_level = "NONE"

    recommendation = "PROCEED"


# ============================================================
# RECOMENDAÇÕES
# ============================================================

recommendations = []


if failed > 0:

    recommendations.append(
        "Investigate failed automated tests."
    )


for failure in failures:

    layer = failure.get(
        "probable_layer",
        "unknown"
    )

    recommendations.append(
        f"Review failures in the {layer} layer."
    )


if risk_level == "HIGH":

    recommendations.append(
        "Consider blocking the release until critical failures are investigated."
    )


elif risk_level == "MEDIUM":

    recommendations.append(
        "Perform additional regression testing before release."
    )


elif risk_level == "LOW":

    recommendations.append(
        "Monitor the identified failures in the next execution."
    )


# ============================================================
# RESULTADO
# ============================================================

result = {

    "risk": {

        "score": risk_score,

        "level": risk_level,

        "release_recommendation": recommendation
    },

    "execution": {

        "total": total,

        "passed": passed,

        "failed": failed,

        "success_rate": success_rate
    },

    "factors": risk_factors,

    "recommendations": recommendations
}


# ============================================================
# SALVAR RESULTADO
# ============================================================

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
# RESUMO
# ============================================================

print()

print("Análise de risco criada:")

print(OUTPUT_FILE)

print()

print("==========================================")
print("RESUMO")
print("==========================================")

print(f"Total: {total}")

print(f"Passed: {passed}")

print(f"Failed: {failed}")

print(f"Success Rate: {success_rate}%")

print()

print(f"Risk Score: {risk_score}")

print(f"Risk Level: {risk_level}")

print(
    f"Release Recommendation: {recommendation}"
)

print()

print(
    f"Fatores de risco: {len(risk_factors)}"
)

print(
    f"Recomendações: {len(recommendations)}"
)