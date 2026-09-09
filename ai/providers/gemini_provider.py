"""
============================================================
MÓDULO 8.10.17.3 - GEMINI + CONTEXTO REAL
============================================================

Objetivo:
Enviar o contexto real do SimulaBank para o Gemini
e obter uma análise real de Quality Engineering.

Características:
- Não utiliza google-genai
- Utiliza requests
- API Key carregada através do .env
- Utiliza Gemini via REST API
- Envia contexto real da execução
- Possui retry para erro HTTP 503
- Mantém compatibilidade com BaseAIProvider
- Teste isolado nesta etapa

============================================================
"""

import json
import os
import time

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

Analise a execução de testes do projeto SimulaBank
utilizando exclusivamente os dados fornecidos.

Não invente informações.

Analise os seguintes pontos:

1. Resumo da execução
2. Falhas encontradas
3. Possível causa
4. Impacto
5. Risco
6. Possibilidade de regressão
7. Recomendações
8. Testes adicionais recomendados
9. Interpretação do Quality Score

Regras:

- Utilize somente informações presentes no contexto.
- Diferencie fatos de hipóteses.
- Não invente endpoints ou comportamentos da aplicação.
- Se a causa raiz não puder ser determinada,
  informe que ela precisa ser investigada.
- Considere o impacto da falha para Quality Engineering.
- Seja objetivo e técnico.
- Responda em português.

Dados da execução:

{context_json}

Apresente a análise de forma organizada.
"""

        return prompt


    # ========================================================
    # ANÁLISE
    # ========================================================

    def analyze(self, context):

        try:

            # ------------------------------------------------
            # CONSTRUIR PROMPT
            # ------------------------------------------------

            prompt = self.build_prompt(context)


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
            # CONFIGURAÇÃO DO RETRY
            # ------------------------------------------------

            max_attempts = 3

            retry_delays = [2, 4, 8]


            # ------------------------------------------------
            # EXECUTAR TENTATIVAS
            # ------------------------------------------------

            for attempt in range(
                1,
                max_attempts + 1
            ):

                print(
                    f"Tentativa {attempt}/{max_attempts}"
                )


                # ------------------------------------------------
                # CHAMADA HTTP
                # ------------------------------------------------

                response = requests.post(

                    url,

                    headers=headers,

                    json=payload,

                    timeout=180

                )


                print(
                    f"HTTP STATUS: {response.status_code}"
                )


                # ------------------------------------------------
                # SUCESSO
                # ------------------------------------------------

                if response.status_code == 200:

                    print()
                    print("Gemini respondeu com sucesso.")


                    data = response.json()


                    # ------------------------------------------------
                    # EXTRAIR RESPOSTA
                    # ------------------------------------------------

                    analysis = (
                        data
                        .get("candidates", [{}])[0]
                        .get("content", {})
                        .get("parts", [{}])[0]
                        .get("text")
                    )


                    # ------------------------------------------------
                    # VALIDAR RESPOSTA
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


                # ------------------------------------------------
                # ERRO HTTP 503
                # ------------------------------------------------

                if response.status_code == 503:

                    print(
                        "Gemini indisponível temporariamente."
                    )


                    if attempt < max_attempts:

                        delay = retry_delays[attempt - 1]


                        print(
                            f"Aguardando {delay} segundos "
                            "antes da próxima tentativa..."
                        )


                        time.sleep(delay)

                        continue


                    response.raise_for_status()


                # ------------------------------------------------
                # OUTROS ERROS HTTP
                # ------------------------------------------------

                response.raise_for_status()


            # ------------------------------------------------
            # SEGURANÇA
            # ------------------------------------------------

            raise RuntimeError(
                "Gemini não retornou uma resposta válida."
            )


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
    print("MÓDULO 8.10.17.3 - GEMINI + CONTEXTO REAL")
    print("=" * 60)
    print()


    # --------------------------------------------------------
    # CONTEXTO REAL DO SIMULABANK
    # --------------------------------------------------------

    context = {

        "execution": {

            "total": 37,

            "passed": 36,

            "failed": 1,

            "skipped": 0,

            "success_rate": 97.3

        },

        "failure": {

            "test": "CT-PIX-013",

            "category": "Product defects",

            "impact": "Medium",

            "layer": "api",

            "error_type": "http",

            "message": "400 != 250"

        },

        "quality_score": {

            "score": 84.11,

            "level": "BOM"

        }

    }


    # --------------------------------------------------------
    # CRIAR PROVIDER
    # --------------------------------------------------------

    try:

        provider = GeminiProvider(

            model=os.getenv(

                "AI_MODEL",

                "gemini-3.8-flash"

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
        # EXECUTAR ANÁLISE
        # ----------------------------------------------------

        result = provider.analyze(context)


        print()
        print("Status:")
        print(result["status"])
        print()


        # ----------------------------------------------------
        # RESULTADO
        # ----------------------------------------------------

        if result["status"] == "success":

            print("ANÁLISE REAL DO GEMINI")

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