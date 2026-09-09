
"""
============================================================
MÓDULO 8.10.17.1 - GEMINI AI PROVIDER
============================================================

Objetivo:
Implementar integração real com a API Gemini através de HTTP.

Características:
- Não utiliza google-genai
- Utiliza requests
- API Key carregada através do .env
- Mantém compatibilidade com BaseAIProvider
- Teste isolado nesta etapa

============================================================
"""

import json
import os

import requests
from dotenv import load_dotenv

from ai.providers.base_provider import BaseAIProvider


# ============================================================
# CARREGAR VARIÁVEIS DO .ENV
# ============================================================

load_dotenv()


# ============================================================
# GEMINI PROVIDER
# ============================================================

class GeminiProvider(BaseAIProvider):

    def __init__(self, model: str):
        super().__init__(model)

        self.api_key = os.getenv("GEMINI_API_KEY")

        if not self.api_key:
            raise ValueError(
                "GEMINI_API_KEY não configurada."
            )

        self.base_url = (
            "https://generativelanguage.googleapis.com"
            "/v1beta/models"
        )

    # ========================================================
    # NOME DO PROVIDER
    # ========================================================

    def get_provider_name(self) -> str:
        return "GeminiProvider"

    # ========================================================
    # CONSTRUÇÃO DO PROMPT
    # ========================================================

    def build_prompt(self, context):

        context_json = json.dumps(
            context,
            ensure_ascii=False,
            indent=2
        )

        prompt = f"""
Você é um especialista em Quality Engineering,
automação de testes e análise de falhas de APIs.

Analise os dados abaixo referentes à execução
de testes do projeto SimulaBank.

Não invente informações que não estejam
presentes nos dados fornecidos.

Analise:

1. Resumo da execução
2. Falhas encontradas
3. Possível causa raiz
4. Impacto
5. Risco
6. Possibilidade de regressão
7. Recomendações
8. Testes adicionais recomendados
9. Interpretação do Quality Score

Dados da execução:

{context_json}

Responda de forma objetiva e técnica.
"""

        return prompt

    # ========================================================
    # ANÁLISE
    # ========================================================

    def analyze(self, context):

        try:

            # ------------------------------------------------
            # TESTE ISOLADO
            # ------------------------------------------------
            # Nesta etapa estamos validando apenas
            # a comunicação entre o Provider e a API Gemini.
            #
            # O contexto recebido ainda não é utilizado.
            # ------------------------------------------------

            prompt = (
                "Responda apenas: Gemini funcionando."
            )

            # ------------------------------------------------
            # URL DA API
            # ------------------------------------------------

            url = (
                f"{self.base_url}/"
                f"{self.model}:generateContent"
            )

            # ------------------------------------------------
            # HEADERS
            # ------------------------------------------------

            headers = {
                "Content-Type": "application/json",
                "x-goog-api-key": self.api_key
            }

            # ------------------------------------------------
            # PAYLOAD
            # ------------------------------------------------

            payload = {
                "contents": [
                    {
                        "parts": [
                            {
                                "text": prompt
                            }
                        ]
                    }
                ]
            }

            # ------------------------------------------------
            # CHAMADA HTTP
            # ------------------------------------------------

            response = requests.post(
                url,
                headers=headers,
                json=payload,
                timeout=180
            )

            # ------------------------------------------------
            # DEBUG TEMPORÁRIO
            # ------------------------------------------------

            print()
            print("HTTP STATUS:", response.status_code)

            print()
            print("RESPONSE:")
            print(response.text)

            print()

            # ------------------------------------------------
            # VALIDAR STATUS HTTP
            # ------------------------------------------------

            response.raise_for_status()

            # ------------------------------------------------
            # CONVERTER RESPOSTA PARA JSON
            # ------------------------------------------------

            data = response.json()

            # ------------------------------------------------
            # EXTRAIR RESPOSTA DO GEMINI
            # ------------------------------------------------

            analysis = (
                data
                .get("candidates", [{}])[0]
                .get("content", {})
                .get("parts", [{}])[0]
                .get("text")
            )

            # ------------------------------------------------
            # VALIDAR CONTEÚDO
            # ------------------------------------------------

            if not analysis:
                raise ValueError(
                    "Gemini retornou uma resposta sem conteúdo."
                )

            # ------------------------------------------------
            # RETORNO PADRONIZADO
            # ------------------------------------------------

            return {
                "provider": self.get_provider_name(),
                "model": self.model,
                "status": "success",
                "engine_status": "success",
                "analysis": analysis,
                "response_status": "success"
            }

        except Exception as error:

            return {
                "provider": self.get_provider_name(),
                "model": self.model,
                "status": "failed",
                "engine_status": "failed",
                "analysis": None,
                "response_status": "failed",
                "error": str(error)
            }


# ============================================================
# TESTE ISOLADO
# ============================================================

if __name__ == "__main__":

    print()
    print("=" * 60)
    print("MÓDULO 8.10.17.1 - GEMINI PROVIDER")
    print("=" * 60)
    print()

    # --------------------------------------------------------
    # CONTEXTO DE TESTE
    # --------------------------------------------------------

    context = {
        "test": "CT-PIX-013",
        "status": "FAILED",
        "error": "400 != 250"
    }

    # --------------------------------------------------------
    # CRIAR PROVIDER
    # --------------------------------------------------------

    try:

        provider = GeminiProvider(
            model=os.getenv(
                "AI_MODEL",
                "gemini-3.7-flash"
            )
        )

        print(
            f"Provider: {provider.get_provider_name()}"
        )

        print(
            f"Model:    {provider.model}"
        )

        print()

        # ----------------------------------------------------
        # EXECUTAR TESTE
        # ----------------------------------------------------

        result = provider.analyze(context)

        print("Status:")
        print(result["status"])

        print()

        # ----------------------------------------------------
        # RESULTADO
        # ----------------------------------------------------

        if result["status"] == "success":

            print("RESPOSTA DO GEMINI")
            print("-" * 60)
            print(result["analysis"])

        else:

            print("ERRO NA INTEGRAÇÃO COM GEMINI")
            print("-" * 60)
            print(result["error"])

    except Exception as error:

        print("ERRO AO INICIALIZAR GEMINI PROVIDER")
        print("-" * 60)
        print(error)

    print()
    print("=" * 60)

