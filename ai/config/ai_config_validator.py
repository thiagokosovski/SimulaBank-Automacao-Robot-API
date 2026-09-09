"""
============================================================
MÓDULO 8.10.7 - AI PROVIDER CONFIGURATION VALIDATOR
============================================================

Responsabilidade:

Validar a configuração utilizada pela camada de IA.

Este módulo NÃO realiza chamadas para nenhuma IA.

Ele apenas verifica se a configuração necessária
para utilizar o provider está presente e válida.

Objetivo:

Evitar que o AI Engine seja executado com uma
configuração inválida.

Exemplo:

    AI_PROVIDER=corporate
    AI_MODEL=corporate-model

============================================================
"""

import os

from ai.config.ai_config import get_config


# ============================================================
# VALIDAÇÃO DA CONFIGURAÇÃO
# ============================================================

def validate_ai_configuration():
    """
    Valida a configuração do AI Provider.
    """

    config = get_config()

    provider = config["provider"]
    model = config["model"]

    errors = []


    # ========================================================
    # VALIDAR MODELO
    # ========================================================

    if not model:

        errors.append(
            "AI_MODEL não foi configurado."
        )


    # ========================================================
    # VALIDAR PROVIDER CORPORATIVO
    # ========================================================

    if provider == "corporate":

        corporate_url = os.getenv(
            "AI_CORPORATE_URL",
            ""
        )

        corporate_api_key = os.getenv(
            "AI_CORPORATE_API_KEY",
            ""
        )

        # ----------------------------------------------------
        # Neste momento o CorporateProvider ainda é MOCK.
        #
        # Portanto não exigimos URL nem API Key.
        #
        # Essa validação será ativada quando fizermos
        # a integração real.
        # ----------------------------------------------------

        if corporate_url:

            print(
                "AI_CORPORATE_URL configurada."
            )

        if corporate_api_key:

            print(
                "AI_CORPORATE_API_KEY configurada."
            )


    # ========================================================
    # RESULTADO
    # ========================================================

    if errors:

        raise ValueError(
            "Configuração da IA inválida:\n"
            + "\n".join(errors)
        )


    return {
        "valid": True,
        "provider": provider,
        "model": model
    }


# ============================================================
# EXECUÇÃO DIRETA
# ============================================================

if __name__ == "__main__":

    print("==========================================")
    print("MÓDULO 8.10.7 - AI CONFIGURATION VALIDATOR")
    print("==========================================")
    print()

    result = validate_ai_configuration()

    print(
        f"Provider: {result['provider']}"
    )

    print(
        f"Model:    {result['model']}"
    )

    print()

    print("Configuração da IA válida.")