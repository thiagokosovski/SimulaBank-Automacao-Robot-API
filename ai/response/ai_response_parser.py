"""
============================================================
MÓDULO 8.10.10 - AI RESPONSE PARSER
============================================================

Responsabilidade:
Normalizar as respostas dos diferentes AI Providers.

Compatibilidade:
- Respostas estruturadas em dicionário.
- Respostas textuais, como a análise do Gemini.

Este módulo não chama a IA e não executa testes.
============================================================
"""

import json
from pathlib import Path
from typing import Any, Dict


# ============================================================
# CAMINHOS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "ai" / "data"

ENGINE_RESULT_FILE = DATA_DIR / "ai_engine_result.json"

OUTPUT_FILE = DATA_DIR / "ai_response_normalized.json"


# ============================================================
# PARSER
# ============================================================

class AIResponseParser:
    """Normaliza respostas retornadas pelos AI Providers."""

    def parse(self, response: Dict[str, Any]) -> Dict[str, Any]:
        """
        Converte a resposta do provider para um formato comum.

        Se a análise for textual, preserva o conteúdo em raw_text.
        Não inventa informações estruturadas que não foram fornecidas.
        """

        if not isinstance(response, dict):
            raise ValueError(
                "A resposta da IA deve ser um dicionário."
            )

        provider = response.get("provider", "unknown")
        model = response.get("model", "unknown")
        status = response.get("status", "unknown")

        analysis = response.get("analysis", {})

        # ----------------------------------------------------
        # CASO 1: ANÁLISE ESTRUTURADA
        # ----------------------------------------------------

        if isinstance(analysis, dict):

            probable_cause = analysis.get("probable_cause")
            confidence = analysis.get("confidence")
            impact = analysis.get("impact")
            risk = analysis.get("risk")
            regression = analysis.get("regression")
            recommendations = analysis.get("recommendations", [])
            raw_text = analysis.get("raw_text")

            if not isinstance(recommendations, list):
                recommendations = []

        # ----------------------------------------------------
        # CASO 2: ANÁLISE TEXTUAL, COMO A DO GEMINI
        # ----------------------------------------------------

        elif isinstance(analysis, str):

            probable_cause = None
            confidence = None
            impact = None
            risk = None
            regression = None

            # Extrai recomendações presentes na seção específica.
            recommendations = extract_recommendations(analysis)

            # Preserva integralmente a resposta original.
            raw_text = analysis

        # ----------------------------------------------------
        # CASO 3: FORMATO NÃO RECONHECIDO
        # ----------------------------------------------------

        else:

            probable_cause = None
            confidence = None
            impact = None
            risk = None
            regression = None
            recommendations = []
            raw_text = None

        # ----------------------------------------------------
        # RESULTADO PADRONIZADO
        # ----------------------------------------------------

        return {
            "provider": provider,
            "model": model,
            "status": status,
            "analysis": {
                "probable_cause": probable_cause,
                "confidence": confidence,
                "impact": impact,
                "risk": risk,
                "regression": regression,
                "recommendations": recommendations,
                "raw_text": raw_text,
            },
        }


# ============================================================
# EXTRAÇÃO DE RECOMENDAÇÕES DA ANÁLISE TEXTUAL
# ============================================================

def extract_recommendations(raw_text: str) -> list:
    """
    Extrai recomendações da seção específica da análise textual.

    Preserva o conteúdo original de cada item.
    Não cria recomendações que não estejam no texto.
    """

    if not isinstance(raw_text, str) or not raw_text.strip():
        return []

    lines = raw_text.splitlines()

    recommendations = []
    inside_section = False

    for line in lines:

        stripped_line = line.strip()

        # Identifica o início da seção.
        if stripped_line == "### 7. Recomendações":
            inside_section = True
            continue

        # Encerra a extração ao encontrar outro título de seção.
        if inside_section and stripped_line.startswith("### "):
            break

        if not inside_section:
            continue

        # Extrai somente itens de lista Markdown.
        if stripped_line.startswith("* "):

            recommendation = stripped_line[2:].strip()

            if recommendation:
                recommendations.append(recommendation)

    return recommendations


# ============================================================
# LEITURA DO RESULTADO REAL DO ENGINE
# ============================================================

def load_engine_response() -> Dict[str, Any]:
    """Carrega a resposta real salva pelo AI Engine."""

    if not ENGINE_RESULT_FILE.exists():
        raise FileNotFoundError(
            "Resultado do AI Engine não encontrado: "
            f"{ENGINE_RESULT_FILE}"
        )

    with open(
        ENGINE_RESULT_FILE,
        "r",
        encoding="utf-8",
    ) as file:
        response = json.load(file)

    if not isinstance(response, dict):
        raise ValueError(
            "O arquivo do AI Engine deve conter um objeto JSON."
        )

    return response


# ============================================================
# SALVAR RESPOSTA NORMALIZADA
# ============================================================

def save_response(response: Dict[str, Any]) -> Path:
    """Salva a resposta normalizada em JSON."""

    DATA_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            response,
            file,
            indent=4,
            ensure_ascii=False,
        )

    return OUTPUT_FILE


# ============================================================
# EXECUÇÃO DIRETA
# ============================================================

def main():

    print("=" * 60)
    print("MÓDULO 8.10.10 - AI RESPONSE PARSER")
    print("=" * 60)

    print()
    print("Carregando resposta real do AI Engine...")

    response = load_engine_response()

    parser = AIResponseParser()

    normalized = parser.parse(response)

    output = save_response(normalized)

    print()
    print(f"Provider: {normalized['provider']}")
    print(f"Modelo: {normalized['model']}")
    print(f"Status: {normalized['status']}")

    raw_text = normalized["analysis"]["raw_text"]

    if raw_text:
        print("Análise textual preservada: Sim")
    else:
        print("Análise textual preservada: Não necessária")

    print()
    print(f"Resposta normalizada: {output}")
    print()
    print("AI Response Parser concluído.")


if __name__ == "__main__":
    main()