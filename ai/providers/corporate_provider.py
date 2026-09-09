"""
============================================================
MÓDULO 8.10.13 - CORPORATE AI PROVIDER INTEGRATION
============================================================

Responsabilidade:

Integrar o CorporateProvider com o AI Provider Client.

Fluxo:

    AI Engine
        ↓
    CorporateProvider
        ↓
    AIProviderClient
        ↓
    API Corporativa
        ↓
    resposta JSON

IMPORTANTE:

Este módulo não conhece:

- Robot Framework;
- Allure;
- regras de negócio;
- cálculo de risco;
- análise de testes.

Ele apenas adapta o contexto para o serviço
corporativo de IA.

============================================================
"""

from typing import Dict, Any

from ai.providers.base_provider import BaseAIProvider
from ai.client.ai_provider_client import AIProviderClient


class CorporateProvider(BaseAIProvider):
    """
    Provider responsável pela integração com uma IA corporativa.
    """

    def __init__(
        self,
        model: str
    ):
        super().__init__(model)

        self.client = AIProviderClient()


    # ========================================================
    # ANÁLISE
    # ========================================================

    def analyze(
        self,
        context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Envia o contexto para a IA corporativa.

        Se a URL corporativa não estiver configurada,
        retorna uma resposta informativa para permitir
        testes locais da arquitetura.
        """

        try:

            response = self.client.send(
                context
            )

            return {

                "provider": self.get_provider_name(),

                "model": self.model,

                "status": "success",

                "analysis": response
            }

        except ValueError as error:

            return {

                "provider": self.get_provider_name(),

                "model": self.model,

                "status": "not_configured",

                "message": str(error)
            }


    # ========================================================
    # PROVIDER NAME
    # ========================================================

    def get_provider_name(self) -> str:
        """
        Retorna o nome do provider.
        """

        return "CorporateProvider"


# ============================================================
# TESTE DIRETO
# ============================================================

if __name__ == "__main__":

    print("==========================================")
    print("MÓDULO 8.10.13 - CORPORATE AI PROVIDER")
    print("==========================================")
    print()

    provider = CorporateProvider(
        model="corporate-model"
    )

    result = provider.analyze(
        {
            "request_type": "quality_analysis",

            "application": "SimulaBank",

            "execution": {

                "total": 37,

                "passed": 36,

                "failed": 1,

                "success_rate": 97.3
            }
        }
    )

    print(
        f"Provider: {result['provider']}"
    )

    print(
        f"Model:    {result['model']}"
    )

    print(
        f"Status:   {result['status']}"
    )

    if "message" in result:

        print(
            f"Message:  {result['message']}"
        )

    print()

    print(
        "Corporate Provider validado."
    )