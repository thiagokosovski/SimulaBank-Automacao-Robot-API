# ============================================================
# MÓDULO 8.6
# ANÁLISE DA CAUSA PROVÁVEL
# ============================================================
#
# Responsabilidade:
#
# Analisar as evidências de uma falha e determinar uma
# possível causa raiz.
#
# IMPORTANTE:
#
# Este módulo NÃO depende do Allure.
#
# Entrada:
#
# ai/data/ai_quality_analysis.json
#
# Saída:
#
# ai/data/ai_root_cause_analysis.json
#
# Nesta primeira versão utilizamos regras determinísticas.
#
# Futuramente este módulo poderá utilizar uma IA/LLM.
#
# ============================================================

import json
from pathlib import Path


# ============================================================
# CONFIGURAÇÃO
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_FILE = (
    PROJECT_ROOT
    / "ai"
    / "data"
    / "ai_quality_analysis.json"
)

OUTPUT_FILE = (
    PROJECT_ROOT
    / "ai"
    / "data"
    / "ai_root_cause_analysis.json"
)


# ============================================================
# CARREGAR DADOS
# ============================================================

def load_analysis():

    with open(
        INPUT_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


# ============================================================
# ANALISAR CAUSA
# ============================================================

def analyze_root_cause(failure):

    message = failure.get(
        "message",
        ""
    )

    message_lower = message.lower()

    category = failure.get(
        "category",
        "Unknown"
    )

    probable_layer = failure.get(
        "probable_layer",
        "unknown"
    )

    failed_keyword = failure.get(
        "failed_keyword",
        "Unknown"
    )


    # ========================================================
    # REGRA 1 — AUTENTICAÇÃO
    # ========================================================

    if (
        "401" in message_lower
        or "unauthorized" in message_lower
        or "token" in message_lower
    ):

        return {

            "cause": (
                "Possível falha no processo de autenticação "
                "ou utilização de token inválido/expirado."
            ),

            "confidence": 0.90,

            "evidence": [
                "A falha apresenta indícios relacionados à autenticação.",
                f"Keyword com falha: {failed_keyword}",
                f"Camada provável: {probable_layer}"
            ],

            "recommendation": (
                "Validar credenciais, geração do token, "
                "validade do token e autorização do endpoint."
            )
        }


    # ========================================================
    # REGRA 2 — ERRO HTTP 400
    # ========================================================

    if "400" in message_lower:

        return {

            "cause": (
                "A API rejeitou a requisição enviada pelo teste. "
                "A causa provável está relacionada ao payload, "
                "regra de validação ou dados utilizados na requisição."
            ),

            "confidence": 0.85,

            "evidence": [
                "A resposta HTTP recebida foi 400.",
                f"Keyword com falha: {failed_keyword}",
                f"Camada provável: {probable_layer}",
                f"Mensagem original: {message}"
            ],

            "recommendation": (
                "Verificar o payload enviado, os dados utilizados "
                "pelo cenário e as regras de validação do endpoint."
            )
        }


    # ========================================================
    # REGRA 3 — ERRO HTTP 5XX
    # ========================================================

    if any(
        code in message_lower
        for code in [
            "500",
            "502",
            "503",
            "504"
        ]
    ):

        return {

            "cause": (
                "Possível erro interno ou indisponibilidade "
                "do serviço da aplicação."
            ),

            "confidence": 0.90,

            "evidence": [
                "Foi identificado um status HTTP da família 5xx.",
                f"Keyword com falha: {failed_keyword}",
                f"Camada provável: {probable_layer}"
            ],

            "recommendation": (
                "Verificar logs da aplicação, disponibilidade "
                "dos serviços, banco de dados e dependências."
            )
        }


    # ========================================================
    # REGRA 4 — ERRO DE API
    # ========================================================

    if probable_layer == "api":

        return {

            "cause": (
                "Falha provavelmente localizada na comunicação "
                "ou regra de negócio da API."
            ),

            "confidence": 0.70,

            "evidence": [
                f"Camada identificada: {probable_layer}",
                f"Categoria: {category}",
                f"Keyword com falha: {failed_keyword}"
            ],

            "recommendation": (
                "Verificar request, response, contrato da API "
                "e regras de negócio relacionadas ao cenário."
            )
        }


    # ========================================================
    # REGRA PADRÃO
    # ========================================================

    return {

        "cause": (
            "Não foi possível determinar uma causa específica "
            "com as evidências disponíveis."
        ),

        "confidence": 0.40,

        "evidence": [
            f"Categoria: {category}",
            f"Camada: {probable_layer}",
            f"Keyword: {failed_keyword}",
            f"Mensagem: {message}"
        ],

        "recommendation": (
            "Investigar os logs e evidências adicionais "
            "disponíveis para o teste."
        )
    }


# ============================================================
# PROCESSAMENTO
# ============================================================

def main():

    print("==========================================")
    print("MÓDULO 8.6 - ANÁLISE DA CAUSA PROVÁVEL")
    print("==========================================")
    print()

    print("Entrada:")
    print(INPUT_FILE)
    print()


    # --------------------------------------------------------
    # Carregar análise anterior
    # --------------------------------------------------------

    data = load_analysis()


    execution = data.get(
        "execution",
        {}
    )

    failures = data.get(
        "failures",
        []
    )


    # --------------------------------------------------------
    # Analisar cada falha
    # --------------------------------------------------------

    analyzed_failures = []


    for failure in failures:

        root_cause = analyze_root_cause(
            failure
        )


        analyzed_failure = {

            "test": failure.get(
                "test",
                "Unknown"
            ),

            "category": failure.get(
                "category",
                "Unknown"
            ),

            "impact": failure.get(
                "impact",
                "Unknown"
            ),

            "error_type": failure.get(
                "error_type",
                "Unknown"
            ),

            "probable_layer": failure.get(
                "probable_layer",
                "Unknown"
            ),

            "failed_keyword": failure.get(
                "failed_keyword",
                "Unknown"
            ),

            "message": failure.get(
                "message",
                ""
            ),

            "root_cause": root_cause
        }


        analyzed_failures.append(
            analyzed_failure
        )


    # ========================================================
    # RESULTADO
    # ========================================================

    result = {

        "execution": execution,

        "analysis": {

            "type": "deterministic",

            "engine": "SimulaBank AI Quality Analyzer",

            "version": "1.0"
        },

        "failures": analyzed_failures
    }


    # --------------------------------------------------------
    # Salvar
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
        f"{execution.get('total', 0)}"
    )

    print(
        f"Falhas analisadas: "
        f"{len(analyzed_failures)}"
    )

    print()


    for failure in analyzed_failures:

        root_cause = failure["root_cause"]

        print(
            f"Teste: {failure['test']}"
        )

        print(
            f"Causa provável: "
            f"{root_cause['cause']}"
        )

        print(
            f"Confiança: "
            f"{root_cause['confidence'] * 100:.0f}%"
        )

        print(
            f"Recomendação: "
            f"{root_cause['recommendation']}"
        )

        print()


# ============================================================
# EXECUÇÃO
# ============================================================

if __name__ == "__main__":

    main()