"""
============================================================
MÓDULO 8.10.17 - OPENAI AI PROVIDER
============================================================

Responsabilidade:

Implementar a integração real com a OpenAI.

Fluxo:

    AI Engine
        ↓
    Provider Factory
        ↓
    OpenAIProvider
        ↓
    OpenAI Responses API
        ↓
    Modelo OpenAI
        ↓
    resposta normalizada

IMPORTANTE:

Este módulo NÃO conhece:

- Robot Framework;
- Allure;
- regras de negócio;
- cálculo de Quality Score;
- análise de risco;
- estrutura interna do SimulaBank.

Ele recebe um contexto preparado pelo AI Engine,
transforma esse contexto em uma instrução para o modelo
e retorna a resposta em formato padronizado.

Configuração:

    AI_PROVIDER=openai
    AI_MODEL=gpt-5.6-luna
    OPENAI_API_KEY=...

A API Key nunca deve ficar no código.

============================================================
"""



import json
import os
from dotenv import load_dotenv
from typing import Dict, Any

from openai import OpenAI

from ai.providers.base_provider import BaseAIProvider

# ============================================================
# CARREGA VARIÁVEIS DO ARQUIVO .ENV
# ============================================================

load_dotenv()


class OpenAIProvider(BaseAIProvider):
    """
    Provider responsável pela integração com a OpenAI.
    """

    # ========================================================
    # CONSTRUTOR
    # ========================================================

    def __init__(
        self,
        model: str
    ):
        """
        Inicializa o provider OpenAI.

        Args:
            model:
                Nome do modelo OpenAI utilizado.
        """

        super().__init__(
            model
        )

        # ----------------------------------------------------
        # Obtém API Key
        # ----------------------------------------------------

        api_key = os.getenv(
            "OPENAI_API_KEY"
        )

        if not api_key:

            raise ValueError(
                "OPENAI_API_KEY não configurada."
            )

        # ----------------------------------------------------
        # Cria cliente OpenAI
        # ----------------------------------------------------

        self.client = OpenAI(
            api_key=api_key
        )


    # ========================================================
    # NOME DO PROVIDER
    # ========================================================

    def get_provider_name(self) -> str:
        """
        Retorna o nome do provider.
        """

        return "OpenAIProvider"


    # ========================================================
    # CONSTRUÇÃO DO PROMPT
    # ========================================================

    def build_prompt(
        self,
        context: Dict[str, Any]
    ) -> str:
        """
        Converte o contexto de qualidade em uma instrução
        estruturada para o modelo de IA.

        Args:
            context:
                Dados preparados pelo AI Engine.

        Returns:
            Prompt estruturado.
        """

        context_json = json.dumps(
            context,
            ensure_ascii=False,
            indent=2
        )

        prompt = f"""
Você é um especialista em Quality Engineering,
automação de testes e análise de qualidade de software.

Analise os dados de execução fornecidos abaixo.

OBJETIVOS DA ANÁLISE:

1. Identificar as principais falhas.
2. Determinar a causa provável de cada falha.
3. Avaliar o impacto das falhas.
4. Avaliar o risco para a qualidade da aplicação.
5. Identificar possíveis regressões.
6. Recomendar ações para investigação.
7. Recomendar testes adicionais quando necessário.
8. Considerar o Quality Score da execução.

IMPORTANTE:

Não invente informações que não estejam presentes
nos dados fornecidos.

Quando não houver evidência suficiente para determinar
a causa exata, deixe claro que se trata de uma
hipótese ou causa provável.

DADOS DA EXECUÇÃO:

{context_json}

Forneça uma análise técnica, objetiva e estruturada.
"""

        return prompt


    # ========================================================
    # ANÁLISE
    # ========================================================

    def analyze(
        self,
        context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Envia o contexto para a OpenAI e retorna a análise.

        Args:
            context:
                Dados preparados pelo AI Engine.

        Returns:
            Dicionário contendo a resposta normalizada.
        """

        # ----------------------------------------------------
        # Construção do prompt
        # ----------------------------------------------------

        prompt = self.build_prompt(
            context
        )

        try:

            # ------------------------------------------------
            # Chamada real para a OpenAI
            # ------------------------------------------------

            response = self.client.responses.create(

                model=self.model,

                input=prompt
            )

            # ------------------------------------------------
            # Obtém resposta textual
            # ------------------------------------------------

            analysis = response.output_text

            # ------------------------------------------------
            # Retorno padronizado
            # ------------------------------------------------

            return {

                "provider":
                    self.get_provider_name(),

                "model":
                    self.model,

                "status":
                    "success",

                "engine_status":
                    "success",

                "analysis":
                    analysis,

                "response_status":
                    "success"
            }

        except Exception as error:

            # ------------------------------------------------
            # Tratamento de erro da integração
            # ------------------------------------------------

            return {

                "provider":
                    self.get_provider_name(),

                "model":
                    self.model,

                "status":
                    "failed",

                "engine_status":
                    "failed",

                "analysis":
                    None,

                "response_status":
                    "failed",

                "error":
                    str(error)
            }


# ============================================================
# TESTE MANUAL
# ============================================================

if __name__ == "__main__":

    print(
        "============================================================"
    )

    print(
        "MÓDULO 8.10.17 - OPENAI AI PROVIDER"
    )

    print(
        "============================================================"
    )

    print()


    # --------------------------------------------------------
    # Modelo
    # --------------------------------------------------------

    model = os.getenv(
        "OPENAI_MODEL",
        "gpt-5.6-luna"
    )


    # --------------------------------------------------------
    # Cria provider
    # --------------------------------------------------------

    provider = OpenAIProvider(
        model=model
    )


    print(
        f"Provider: {provider.get_provider_name()}"
    )

    print(
        f"Model:    {provider.model}"
    )

    print()


    # --------------------------------------------------------
    # Contexto de teste
    # --------------------------------------------------------

    test_context = {

        "request_type":
            "quality_analysis",

        "application":
            "SimulaBank",

        "execution": {

            "total":
                37,

            "passed":
                36,

            "failed":
                1,

            "skipped":
                0,

            "success_rate":
                97.3
        },

        "failures": [

            {

                "test":
                    "CT-PIX-013",

                "failure": {

                    "message":
                        "400 != 250",

                    "error_type":
                        "http",

                    "failed_keyword":
                        "Validar Status HTTP"
                }
            }
        ],

        "quality_score": {

            "score":
                84.11,

            "level":
                "BOM"
        }
    }


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
        "Status:"
    )

    print(
        result["status"]
    )

    print()


    if result["status"] == "success":

        print(
            "============================================================"
        )

        print(
            "RESPOSTA DA OPENAI"
        )

        print(
            "============================================================"
        )

        print()

        print(
            result["analysis"]
        )

    else:

        print(
            "============================================================"
        )

        print(
            "ERRO NA INTEGRAÇÃO COM OPENAI"
        )

        print(
            "============================================================"
        )

        print()

        print(
            result["error"]
        )


    print()

    print(
        "============================================================"
    )