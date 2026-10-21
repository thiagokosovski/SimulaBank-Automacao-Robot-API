"""
============================================================
MÓDULO 8.10.3 - AI PROVIDER FACTORY
============================================================

Responsabilidade:

Selecionar automaticamente o provider de IA configurado
no sistema.

Este módulo NÃO realiza a análise da IA.

Ele apenas decide qual provider deverá ser utilizado.

Exemplo:

    AI_PROVIDER=local

Resultado:

    LocalProvider

Outro exemplo:

    AI_PROVIDER=corporate

Resultado:

    CorporateProvider


IMPORTANTE:

A Factory permite trocar o motor da IA sem alterar:

- Robot Framework
- Allure
- análise de falhas
- análise de risco
- relatório de qualidade

============================================================
"""
"""
============================================================
MÓDULO 8.10.3 - AI PROVIDER FACTORY
============================================================

Responsabilidade:
Selecionar o provider de IA configurado no sistema.

A Factory não executa a análise.

A seleção do provider não deve exigir alterações no
Robot Framework, Allure ou módulos de análise de qualidade.
============================================================
"""

from ai.config.ai_config import get_config


# ============================================================
# PROVIDER FACTORY
# ============================================================

def get_ai_provider():
    """Cria e retorna o provider de IA configurado."""

    config = get_config()

    provider = config["provider"]
    model = config["model"]


    # ========================================================
    # PROVIDER LOCAL
    # ========================================================

    if provider == "local":

        from ai.providers.local_provider import LocalProvider

        return LocalProvider(model=model)


    # ========================================================
    # PROVIDER OPENAI
    # ========================================================

    if provider == "openai":

        from ai.providers.openai_provider import OpenAIProvider

        return OpenAIProvider(model=model)


    # ========================================================
    # PROVIDER AZURE
    # ========================================================

    if provider == "azure":

        from ai.providers.azure_provider import AzureProvider

        return AzureProvider(model=model)


    # ========================================================
    # PROVIDER CORPORATIVO
    # ========================================================

    if provider == "corporate":

        from ai.providers.corporate_provider import CorporateProvider

        return CorporateProvider(model=model)


    # ========================================================
    # PROVIDER GEMINI
    # ========================================================

    if provider == "gemini":

        from ai.providers.gemini_provider import GeminiProvider

        return GeminiProvider(model=model)


    # ========================================================
    # PROTEÇÃO CONTRA CONFIGURAÇÃO INVÁLIDA
    # ========================================================

    raise ValueError(
        f"Provider de IA não suportado: {provider}"
    )


# ============================================================
# TESTE MANUAL
# ============================================================

if __name__ == "__main__":

    print("=" * 50)
    print("MÓDULO 8.10.3 - AI PROVIDER FACTORY")
    print("=" * 50)
    print()

    print("Lendo configuração do AI Provider...")

    provider = get_ai_provider()

    print()
    print("Provider selecionado:")
    print(provider.__class__.__name__)

    print(f"Modelo: {provider.model}")
    print()
    print("Factory funcionando.")