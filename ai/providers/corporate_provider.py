"""
============================================================
MÓDULO 8.10.4 - CORPORATE AI PROVIDER
============================================================

Responsabilidade:

Representar o provider de uma IA corporativa.

IMPORTANTE:

Este módulo NÃO realiza chamadas externas neste momento.

Ele funciona como um adapter/mock para validar a arquitetura.

Futuramente poderá ser conectado a:

- API interna da empresa;
- Azure OpenAI corporativo;
- Gateway corporativo de IA;
- Modelo privado;
- LLM hospedado internamente.

Nenhuma credencial deve ficar neste arquivo.

============================================================
"""

from typing import Dict, Any

from ai.providers.base_provider import BaseAIProvider


class CorporateProvider(BaseAIProvider):
    """
    Provider para integração com uma IA corporativa.
    """

    def analyze(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Executa uma análise simulada.

        Futuramente este método será responsável por enviar
        o contexto para o serviço corporativo de IA.
        """

        return {
            "provider": self.get_provider_name(),
            "model": self.model,
            "status": "mock",
            "message": (
                "Corporate AI Provider configurado "
                "e pronto para integração."
            )
        }

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
    print("MÓDULO 8.10.4 - CORPORATE AI PROVIDER")
    print("==========================================")
    print()

    provider = CorporateProvider(
        model="corporate-model"
    )

    result = provider.analyze({})

    print(f"Provider: {result['provider']}")
    print(f"Model:    {result['model']}")
    print(f"Status:   {result['status']}")
    print(f"Message:  {result['message']}")

    print()
    print("Corporate Provider funcionando.")