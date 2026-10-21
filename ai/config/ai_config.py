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

"""
============================================================
MÓDULO 8.10.2 - CONFIGURAÇÃO DO AI PROVIDER
============================================================

Responsabilidade:
Centralizar as configurações do motor de IA.

Este módulo não realiza chamadas para provedores de IA.
Credenciais devem ser fornecidas por variáveis de ambiente.
============================================================
"""

import os

from dotenv import load_dotenv


# ============================================================
# CARREGAR VARIÁVEIS DO .ENV
# ============================================================

load_dotenv()


# ============================================================
# CONFIGURAÇÕES
# ============================================================

AI_PROVIDER = os.getenv(
    "AI_PROVIDER",
    "local"
).strip().lower()

AI_MODEL = os.getenv(
    "AI_MODEL",
    "test-model"
).strip()


# ============================================================
# PROVIDERS SUPORTADOS
# ============================================================

SUPPORTED_PROVIDERS = [
    "local",
    "openai",
    "azure",
    "corporate",
    "gemini",
]


# ============================================================
# VALIDAÇÃO
# ============================================================

def validate_config():
    """Valida a configuração do provider e do modelo."""

    if AI_PROVIDER not in SUPPORTED_PROVIDERS:
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
    """Retorna a configuração validada."""

    validate_config()

    return {
        "provider": AI_PROVIDER,
        "model": AI_MODEL,
    }


# ============================================================
# EXECUÇÃO DIRETA
# ============================================================

if __name__ == "__main__":

    print("=" * 50)
    print("MÓDULO 8.10.2 - CONFIGURAÇÃO DA IA")
    print("=" * 50)

    config = get_config()

    print(f"Provider: {config['provider']}")
    print(f"Model:    {config['model']}")
    print()
    print("Configuração válida.")