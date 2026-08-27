"""
============================================================
MÓDULO 8.10.2 - CONFIGURAÇÃO DO AI PROVIDER
============================================================

Responsabilidade:

Centralizar as configurações relacionadas ao motor de IA.

IMPORTANTE:

Este módulo NÃO realiza chamadas para IA.

Ele apenas informa:

- qual provider utilizar;
- qual modelo utilizar;
- se a configuração está válida.

Exemplos:

    AI_PROVIDER=openai
    AI_PROVIDER=azure
    AI_PROVIDER=corporate
    AI_PROVIDER=local

As credenciais NÃO ficam neste arquivo.

Elas deverão ser fornecidas através de variáveis
de ambiente / GitHub Secrets.

============================================================
"""

import os


# ============================================================
# CONFIGURAÇÕES
# ============================================================

AI_PROVIDER = os.getenv(
    "AI_PROVIDER",
    "local"
)

AI_MODEL = os.getenv(
    "AI_MODEL",
    "test-model"
)


# ============================================================
# PROVIDERS SUPORTADOS
# ============================================================

SUPPORTED_PROVIDERS = [
    "local",
    "openai",
    "azure",
    "corporate"
]


# ============================================================
# VALIDAÇÃO
# ============================================================

def validate_config():
    """
    Valida se o provider configurado é suportado.
    """

    provider = AI_PROVIDER.lower()

    if provider not in SUPPORTED_PROVIDERS:

        raise ValueError(
            f"AI_PROVIDER inválido: {AI_PROVIDER}. "
            f"Valores permitidos: "
            f"{', '.join(SUPPORTED_PROVIDERS)}"
        )

    if not AI_MODEL:

        raise ValueError(
            "AI_MODEL não foi configurado."
        )


# ============================================================
# INFORMAÇÕES DA CONFIGURAÇÃO
# ============================================================

def get_config():

    validate_config()

    return {
        "provider": AI_PROVIDER.lower(),
        "model": AI_MODEL
    }


# ============================================================
# EXECUÇÃO DIRETA
# ============================================================

if __name__ == "__main__":

    print("==========================================")
    print("MÓDULO 8.10.2 - CONFIGURAÇÃO DA IA")
    print("==========================================")
    print()

    config = get_config()

    print(f"Provider: {config['provider']}")
    print(f"Model:    {config['model']}")

    print()
    print("Configuração válida.")