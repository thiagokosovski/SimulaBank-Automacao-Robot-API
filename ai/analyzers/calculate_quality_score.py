# ============================================================
# MÓDULO 8.10.16 - AI QUALITY SCORE
# ============================================================
#
# Responsabilidade:
# Calcular uma Pontuação de Qualidade de 0 a 100
# e persistir o resultado no relatório final.
#
# Entrada:
#   ai/data/ai_final_report.json
#
# Saída:
#   ai/data/ai_final_report.json
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
    / "ai_final_report.json"
)


# ============================================================
# CONFIGURAÇÃO DO SCORE
# ============================================================

MAX_EXECUTION_SCORE = 50
MAX_FAILURE_SCORE = 20
MAX_RISK_SCORE = 20
MAX_IMPACT_SCORE = 10


# ============================================================
# CLASSIFICAÇÃO DO QUALITY SCORE
# ============================================================

def classify_quality_score(score):

    if score >= 90:
        return "EXCELENTE"

    if score >= 75:
        return "BOM"

    if score >= 60:
        return "MÉDIO"

    if score >= 40:
        return "ALTO RISCO"

    return "CRÍTICO"


# ============================================================
# CALCULAR PONTUAÇÃO DA EXECUÇÃO
# ============================================================

def calculate_execution_score(success_rate):

    score = (
        success_rate / 100
    ) * MAX_EXECUTION_SCORE

    return round(score, 2)


# ============================================================
# CALCULAR PONTUAÇÃO DAS FALHAS
# ============================================================

def calculate_failure_score(failed, total):

    if total <= 0:
        return 0

    failure_rate = failed / total

    penalty = (
        failure_rate
        * MAX_FAILURE_SCORE
    )

    score = (
        MAX_FAILURE_SCORE
        - penalty
    )

    return round(
        max(score, 0),
        2
    )


# ============================================================
# CALCULAR COMPONENTE DE RISCO
# ============================================================

def calculate_risk_score(risk_score):

    risk_score = max(
        0,
        min(risk_score, 100)
    )

    score = (
        (100 - risk_score)
        / 100
    ) * MAX_RISK_SCORE

    return round(score, 2)


# ============================================================
# CALCULAR PONTUAÇÃO DE IMPACTO
# ============================================================

def calculate_impact_score(failures):

    if not failures:
        return MAX_IMPACT_SCORE

    impact_penalty = 0

    for failure in failures:

        impact = str(
            failure.get("impact", "")
        ).upper()

        if impact == "CRITICAL":
            impact_penalty += 10

        elif impact == "HIGH":
            impact_penalty += 7

        elif impact == "MEDIUM":
            impact_penalty += 4

        elif impact == "LOW":
            impact_penalty += 2

    score = (
        MAX_IMPACT_SCORE
        - impact_penalty
    )

    return round(
        max(score, 0),
        2
    )


# ============================================================
# CALCULAR QUALITY SCORE
# ============================================================

def calculate_quality_score(report):

    execution = report["execution"]

    total = execution["total"]
    failed = execution["failed"]
    success_rate = execution["success_rate"]

    risk = report["risk"]

    risk_score = risk["score"]

    failures = report["failures"]


    # --------------------------------------------------------
    # COMPONENTES
    # --------------------------------------------------------

    execution_score = calculate_execution_score(
        success_rate
    )

    failure_score = calculate_failure_score(
        failed,
        total
    )

    risk_points = calculate_risk_score(
        risk_score
    )

    impact_score = calculate_impact_score(
        failures
    )


    # --------------------------------------------------------
    # SCORE FINAL
    # --------------------------------------------------------

    quality_score = (
        execution_score
        + failure_score
        + risk_points
        + impact_score
    )

    quality_score = round(
        min(
            max(
                quality_score,
                0
            ),
            100
        ),
        2
    )


    quality_level = classify_quality_score(
        quality_score
    )


    return {
        "score": quality_score,
        "level": quality_level,
        "components": {
            "execution_score": execution_score,
            "failure_score": failure_score,
            "risk_score": risk_points,
            "impact_score": impact_score
        }
    }


# ============================================================
# SALVAR QUALITY SCORE NO RELATÓRIO
# ============================================================

def save_quality_score(report, quality_score):

    report["quality_score"] = quality_score

    with open(
        INPUT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            report,
            file,
            ensure_ascii=False,
            indent=4
        )


# ============================================================
# EXECUÇÃO
# ============================================================

if __name__ == "__main__":

    print()
    print("=" * 60)
    print("MÓDULO 8.10.16 - AI QUALITY SCORE")
    print("=" * 60)
    print()

    print(
        f"Entrada: {INPUT_FILE}"
    )

    print()


    # ========================================================
    # VERIFICAR ARQUIVO
    # ========================================================

    if not INPUT_FILE.exists():

        print(
            "❌ Arquivo "
            "ai_final_report.json "
            "não encontrado."
        )

        raise SystemExit(1)


    # ========================================================
    # CARREGAR RELATÓRIO
    # ========================================================

    try:

        with open(
            INPUT_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            report = json.load(file)

    except json.JSONDecodeError as error:

        print(
            f"❌ JSON inválido: {error}"
        )

        raise SystemExit(1)


    # ========================================================
    # CALCULAR SCORE
    # ========================================================

    quality_score = calculate_quality_score(
        report
    )


    # ========================================================
    # SALVAR SCORE
    # ========================================================

    save_quality_score(
        report,
        quality_score
    )


    # ========================================================
    # DADOS DA EXECUÇÃO
    # ========================================================

    execution = report["execution"]


    # ========================================================
    # RESULTADO
    # ========================================================

    print("-" * 60)

    print(
        f"Total de testes: "
        f"{execution['total']}"
    )

    print(
        f"Testes aprovados: "
        f"{execution['passed']}"
    )

    print(
        f"Testes falhos: "
        f"{execution['failed']}"
    )

    print(
        f"Taxa de sucesso: "
        f"{str(execution['success_rate']).replace('.', ',')}%"
    )

    print()

    print(
        f"Pontuação de Execução: "
        f"{str(quality_score['components']['execution_score']).replace('.', ',')}/50"
    )

    print(
        f"Pontuação de Falhas: "
        f"{str(quality_score['components']['failure_score']).replace('.', ',')}/20"
    )

    print(
        f"Componente de Risco: "
        f"{str(quality_score['components']['risk_score']).replace('.', ',')}/20"
    )

    print(
        f"Pontuação de Impacto: "
        f"{str(quality_score['components']['impact_score']).replace('.', ',')}/10"
    )

    print()

    print(
        f"PONTUAÇÃO DE QUALIDADE: "
        f"{str(quality_score['score']).replace('.', ',')}/100"
    )

    print(
        f"NÍVEL DE QUALIDADE: "
        f"{quality_score['level']}"
    )

    print()

    print(
        "✅ Quality Score salvo em "
        "ai_final_report.json"
    )

    print("=" * 60)