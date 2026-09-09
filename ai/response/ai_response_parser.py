"""
============================================================
MÓDULO 8.10.10 - AI RESPONSE PARSER
============================================================

Responsabilidade:

Normalizar a resposta retornada pelo motor de IA.

Este módulo NÃO:

- chama a IA;
- realiza requisições HTTP;
- executa testes;
- altera o Robot Framework;
- altera o Allure;
- calcula o resultado dos testes.

Sua responsabilidade é:

    RESPOSTA DA IA
          ↓
    FORMATO PADRONIZADO
          ↓
    SISTEMA DE QUALIDADE

Objetivo:

Permitir que diferentes providers de IA retornem
um resultado consistente para o restante do sistema.

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

OUTPUT_FILE = (
    DATA_DIR / "ai_response_normalized.json"
)


# ============================================================
# PARSER
# ============================================================

class AIResponseParser:
    """
    Responsável por normalizar respostas da IA.
    """

    def parse(
        self,
        response: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Normaliza a resposta recebida.

        Args:
            response:
                Resposta retornada pelo provider.

        Returns:
            Resposta em formato padronizado.
        """

        if not isinstance(response, dict):

            raise ValueError(
                "A resposta da IA deve ser um dicionário."
            )


        # ====================================================
        # IDENTIFICAÇÃO DO PROVIDER
        # ====================================================

        provider = response.get(
            "provider",
            "unknown"
        )

        model = response.get(
            "model",
            "unknown"
        )

        status = response.get(
            "status",
            "unknown"
        )


        # ====================================================
        # ANÁLISE
        # ====================================================

        analysis = response.get(
            "analysis",
            {}
        )


        if not isinstance(
            analysis,
            dict
        ):

            analysis = {}


        # ====================================================
        # RESULTADO PADRONIZADO
        # ====================================================

        normalized = {

            "provider": provider,

            "model": model,

            "status": status,

            "analysis": {

                "probable_cause": analysis.get(
                    "probable_cause"
                ),

                "confidence": analysis.get(
                    "confidence"
                ),

                "impact": analysis.get(
                    "impact"
                ),

                "risk": analysis.get(
                    "risk"
                ),

                "regression": analysis.get(
                    "regression"
                ),

                "recommendations": analysis.get(
                    "recommendations",
                    []
                )
            }
        }


        return normalized


# ============================================================
# SALVAR RESULTADO
# ============================================================

def save_response(
    response: Dict[str, Any]
) -> Path:
    """
    Salva a resposta normalizada.
    """

    DATA_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            response,
            file,
            indent=4,
            ensure_ascii=False
        )


    return OUTPUT_FILE


# ============================================================
# TESTE DO MÓDULO
# ============================================================

def main():

    print("==========================================")
    print("MÓDULO 8.10.10 - AI RESPONSE PARSER")
    print("==========================================")
    print()


    # ========================================================
    # RESPOSTA SIMULADA
    # ========================================================

    mock_response = {

        "provider": "CorporateProvider",

        "model": "corporate-model",

        "status": "success",

        "analysis": {

            "probable_cause": (
                "Possível inconsistência no "
                "status HTTP retornado pela API."
            ),

            "confidence": 0.91,

            "impact": "HIGH",

            "risk": "HIGH",

            "regression": True,

            "recommendations": [

                "Investigar o endpoint PIX.",

                "Comparar o status esperado "
                "com o status retornado.",

                "Executar regressão adicional."
            ]
        }
    }


    # ========================================================
    # PARSER
    # ========================================================

    parser = AIResponseParser()

    normalized = parser.parse(
        mock_response
    )


    # ========================================================
    # SALVAR
    # ========================================================

    output = save_response(
        normalized
    )


    print(
        "Resposta normalizada criada:"
    )

    print(output)

    print()

    print(
        "=========================================="
    )

    print(
        "AI Response Parser funcionando."
    )


# ============================================================
# EXECUÇÃO DIRETA
# ============================================================

if __name__ == "__main__":

    main()