"""
============================================================
MÓDULO 8.10.4 - LOCAL AI PROVIDER
============================================================

Responsabilidade:

Implementar o primeiro provider concreto de IA.

Neste momento o provider funciona localmente e NÃO realiza
chamadas para serviços externos.

Ele serve para:

- validar a arquitetura;
- validar a integração com a Factory;
- testar o fluxo completo;
- manter os dados dentro do projeto;
- preparar a futura integração com um modelo local.

Futuramente este provider poderá utilizar, por exemplo:

    Ollama
    LLM local
    Modelo privado
    Outro motor executado internamente

Contrato implementado:

    BaseAIProvider

============================================================
"""

from typing import Dict, Any

from ai.providers.base_provider import BaseAIProvider


class LocalProvider(BaseAIProvider):
    """
    Provider de IA executado localmente.

    Neste estágio inicial, a análise é baseada nas informações
    fornecidas pelo contexto.

    Nenhum dado é enviado para a internet.
    """

    # ========================================================
    # CONSTRUTOR
    # ========================================================

    def __init__(self, model: str):
        """
        Inicializa o provider local.

        Args:
            model:
                Nome do modelo configurado.
        """

        super().__init__(model)


    # ========================================================
    # NOME DO PROVIDER
    # ========================================================

    def get_provider_name(self) -> str:
        """
        Retorna o nome do provider.
        """

        return "local"


    # ========================================================
    # ANÁLISE
    # ========================================================

    def analyze(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analisa o contexto de execução.

        Neste primeiro estágio não existe chamada para um
        modelo de IA externo.

        O objetivo é validar o contrato e preparar a
        arquitetura para o futuro motor de IA.

        Args:
            context:
                Dados preparados pelos módulos anteriores.

        Returns:
            Dicionário contendo uma análise estruturada.
        """

        # ----------------------------------------------------
        # Obtém informações da execução
        # ----------------------------------------------------

        execution = context.get(
            "execution",
            {}
        )

        total = execution.get(
            "total",
            0
        )

        passed = execution.get(
            "passed",
            0
        )

        failed = execution.get(
            "failed",
            0
        )

        skipped = execution.get(
            "skipped",
            0
        )

        success_rate = execution.get(
            "success_rate",
            0
        )


        # ----------------------------------------------------
        # Obtém as falhas
        # ----------------------------------------------------

        failures = context.get(
            "failures",
            []
        )


        # ----------------------------------------------------
        # Classificação inicial
        # ----------------------------------------------------

        if failed == 0:

            quality_status = "HEALTHY"

        elif success_rate >= 95:

            quality_status = "ATTENTION"

        else:

            quality_status = "CRITICAL"


        # ----------------------------------------------------
        # Preparação das análises das falhas
        # ----------------------------------------------------

        failure_analysis = []


        for failure in failures:

            test_name = failure.get(
                "test",
                "Unknown test"
            )

            failure_data = failure.get(
                "failure",
                {}
            )

            message = failure_data.get(
                "message",
                "Unknown error"
            )

            error_type = failure_data.get(
                "error_type",
                "unknown"
            )

            failed_keyword = failure_data.get(
                "failed_keyword",
                "unknown"
            )


            failure_analysis.append(
                {
                    "test": test_name,

                    "error_type": error_type,

                    "failed_keyword": failed_keyword,

                    "message": message,

                    "probable_cause":
                        "Failure requires investigation.",

                    "confidence": 0.50,

                    "recommendation":
                        "Investigate the failed test and "
                        "its associated evidence."
                }
            )


        # ----------------------------------------------------
        # Resultado da análise
        # ----------------------------------------------------

        return {

            "provider": self.get_provider_name(),

            "model": self.model,

            "analysis_type": "local",

            "quality_status": quality_status,

            "execution": {

                "total": total,

                "passed": passed,

                "failed": failed,

                "skipped": skipped,

                "success_rate": success_rate
            },

            "failures": failure_analysis,

            "recommendations": [

                "Review failed automated tests.",

                "Investigate the evidence associated "
                "with each failure.",

                "Use execution history to identify "
                "possible regressions."
            ]
        }


# ============================================================
# TESTE MANUAL
# ============================================================

if __name__ == "__main__":

    print("==========================================")
    print("MÓDULO 8.10.4 - LOCAL AI PROVIDER")
    print("==========================================")

    print()

    # --------------------------------------------------------
    # Contexto de teste
    # --------------------------------------------------------

    test_context = {

        "execution": {

            "total": 10,

            "passed": 9,

            "failed": 1,

            "skipped": 0,

            "success_rate": 90.0
        },

        "failures": [

            {

                "test": "CT-TEST-001",

                "failure": {

                    "message": "500 != 200",

                    "error_type": "http",

                    "failed_keyword":
                        "Validar Status HTTP"
                }
            }
        ]
    }


    # --------------------------------------------------------
    # Cria o provider
    # --------------------------------------------------------

    provider = LocalProvider(
        model="test-model"
    )


    # --------------------------------------------------------
    # Executa análise
    # --------------------------------------------------------

    result = provider.analyze(
        test_context
    )


    # --------------------------------------------------------
    # Exibe resultado
    # --------------------------------------------------------

    print(
        f"Provider: {provider.get_provider_name()}"
    )

    print(
        f"Model:    {provider.model}"
    )

    print()

    print("Análise:")

    print(result)

    print()

    print("Local Provider funcionando.")