# =========================================================
# MÓDULO 8.10.15 - AI REPORT VALIDATION
# =========================================================
#
# Responsabilidade:
#
# Validar a consistência do relatório final produzido
# pelo pipeline de IA.
#
# Entrada:
#   ai/data/ai_final_report.json
#
# Saída:
#   Validação no terminal
#
# O módulo NÃO altera o relatório.
#
# =========================================================


import json
import sys
from pathlib import Path


# =========================================================
# CONFIGURAÇÃO DE CAMINHOS
# =========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_FILE = (
    PROJECT_ROOT
    / "ai"
    / "data"
    / "ai_final_report.json"
)


# =========================================================
# FUNÇÃO PRINCIPAL DE VALIDAÇÃO
# =========================================================

def validate_report():

    print()
    print("=" * 60)
    print("MÓDULO 8.10.15 - AI REPORT VALIDATION")
    print("=" * 60)

    print()
    print(f"Entrada: {INPUT_FILE}")

    errors = []
    warnings = []


    # =====================================================
    # 1. VERIFICAR EXISTÊNCIA DO ARQUIVO
    # =====================================================

    if not INPUT_FILE.exists():

        errors.append(
            "Arquivo ai_final_report.json não encontrado."
        )

        return False, errors, warnings


    # =====================================================
    # 2. CARREGAR JSON
    # =====================================================

    try:

        with open(
            INPUT_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            report = json.load(file)

    except json.JSONDecodeError as error:

        errors.append(
            f"JSON inválido: {error}"
        )

        return False, errors, warnings


    # =====================================================
    # 3. VALIDAR ESTRUTURA PRINCIPAL
    # =====================================================

    required_sections = [
        "report",
        "execution",
        "failures",
        "risk",
        "ai",
        "recommendations"
    ]

    for section in required_sections:

        if section not in report:

            errors.append(
                f"Seção obrigatória ausente: {section}"
            )


    if errors:

        return False, errors, warnings


    # =====================================================
    # 4. VALIDAR EXECUÇÃO
    # =====================================================

    execution = report["execution"]

    required_execution_fields = [
        "total",
        "passed",
        "failed",
        "skipped",
        "success_rate"
    ]

    for field in required_execution_fields:

        if field not in execution:

            errors.append(
                f"Campo de execução ausente: {field}"
            )


    if errors:

        return False, errors, warnings


    total = execution["total"]
    passed = execution["passed"]
    failed = execution["failed"]
    skipped = execution["skipped"]
    success_rate = execution["success_rate"]


    # =====================================================
    # 5. VALIDAR TOTAL DOS TESTES
    # =====================================================

    calculated_total = (
        passed
        + failed
        + skipped
    )

    if total != calculated_total:

        errors.append(
            "Total de testes inconsistente: "
            f"{total} != {calculated_total}"
        )


    # =====================================================
    # 6. VALIDAR SUCCESS RATE
    # =====================================================

    if total > 0:

        calculated_success_rate = round(
            (passed / total) * 100,
            1
        )

        if success_rate != calculated_success_rate:

            errors.append(
                "Success rate inconsistente: "
                f"{success_rate}% != "
                f"{calculated_success_rate}%"
            )


    # =====================================================
    # 7. VALIDAR RISK
    # =====================================================

    risk = report["risk"]

    required_risk_fields = [
        "score",
        "level",
        "release_recommendation",
        "factors"
    ]

    for field in required_risk_fields:

        if field not in risk:

            errors.append(
                f"Campo de risco ausente: {field}"
            )


    score = risk.get("score")

    if score is not None:

        if not isinstance(score, (int, float)):

            errors.append(
                "Risk score deve ser numérico."
            )

        elif score < 0 or score > 100:

            errors.append(
                "Risk score deve estar entre 0 e 100."
            )


    # =====================================================
    # 8. VALIDAR FAILURES
    # =====================================================

    failures = report["failures"]

    if not isinstance(failures, list):

        errors.append(
            "O campo failures deve ser uma lista."
        )

    else:

        if failed > 0 and len(failures) == 0:

            errors.append(
                "Existem testes falhos, "
                "mas nenhuma falha foi registrada."
            )


        if failed == 0 and len(failures) > 0:

            warnings.append(
                "Existem registros de falha, "
                "mas failed está igual a zero."
            )


    # =====================================================
    # 9. VALIDAR RECOMMENDATIONS
    # =====================================================

    recommendations = report["recommendations"]

    if not isinstance(
        recommendations,
        list
    ):

        errors.append(
            "Recommendations deve ser uma lista."
        )

    elif failed > 0 and len(recommendations) == 0:

        warnings.append(
            "Existem falhas, mas nenhuma "
            "recomendação foi registrada."
        )


    # =====================================================
    # 10. VALIDAR AI
    # =====================================================

    ai = report["ai"]

    required_ai_fields = [
        "provider",
        "model",
        "engine_status",
        "analysis",
        "response_status"
    ]

    for field in required_ai_fields:

        if field not in ai:

            errors.append(
                f"Campo de IA ausente: {field}"
            )


    # =====================================================
    # 11. VALIDAR AI ANALYSIS
    # =====================================================

    ai_analysis = ai.get(
        "analysis",
        {}
    )

    required_ai_analysis_fields = [
        "probable_cause",
        "confidence",
        "impact",
        "risk",
        "regression",
        "recommendations"
    ]

    for field in required_ai_analysis_fields:

        if field not in ai_analysis:

            errors.append(
                f"Campo da análise de IA ausente: {field}"
            )


    # =====================================================
    # 12. VALIDAR CONFIDENCE
    # =====================================================

    confidence = ai_analysis.get(
        "confidence"
    )

    if confidence is not None:

        if not isinstance(
            confidence,
            (int, float)
        ):

            errors.append(
                "AI confidence deve ser numérica."
            )

        elif confidence < 0 or confidence > 1:

            errors.append(
                "AI confidence deve estar entre 0 e 1."
            )


    # =====================================================
    # 13. VALIDAR PROVIDER
    # =====================================================

    provider = ai.get("provider")

    if not provider:

        errors.append(
            "AI Provider não informado."
        )


    # =====================================================
    # 14. VALIDAR MODEL
    # =====================================================

    model = ai.get("model")

    if not model:

        errors.append(
            "AI Model não informado."
        )


    # =====================================================
    # 15. VALIDAR STATUS DA IA
    # =====================================================

    response_status = ai.get(
        "response_status"
    )

    if response_status not in [
        "success",
        "failed"
    ]:

        warnings.append(
            "AI response_status possui "
            "um valor inesperado: "
            f"{response_status}"
        )


    # =====================================================
    # RESULTADO FINAL
    # =====================================================

    valid = len(errors) == 0

    return valid, errors, warnings


# =========================================================
# EXECUÇÃO
# =========================================================

if __name__ == "__main__":

    valid, errors, warnings = validate_report()


    print()
    print("-" * 60)


    # =====================================================
    # ERROS
    # =====================================================

    if errors:

        print("ERROS ENCONTRADOS:")

        for error in errors:

            print(
                f"  ❌ {error}"
            )


    # =====================================================
    # WARNINGS
    # =====================================================

    if warnings:

        print()
        print("WARNINGS:")

        for warning in warnings:

            print(
                f"  ⚠️ {warning}"
            )


    # =====================================================
    # RESULTADO
    # =====================================================

    print()

    if valid:

        print(
            "✅ AI FINAL REPORT VÁLIDO"
        )

        print(
            "O relatório passou por todas "
            "as validações obrigatórias."
        )

        print("=" * 60)

        sys.exit(0)

    else:

        print(
            "❌ AI FINAL REPORT INVÁLIDO"
        )

        print(
            "O relatório possui inconsistências."
        )

        print("=" * 60)

        sys.exit(1)