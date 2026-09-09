"""
============================================================
MÓDULO 8.10.8 - AI PROVIDER CLIENT
============================================================

Responsabilidade:

Centralizar a comunicação HTTP com um serviço de IA.

Este módulo é genérico e não conhece regras de negócio.

Responsabilidades:

    receber payload
          ↓
    validar configuração
          ↓
    montar headers
          ↓
    enviar HTTP POST
          ↓
    tratar erros
          ↓
    retornar resposta JSON

Pode ser utilizado futuramente com:

- IA corporativa;
- Azure OpenAI;
- Gateway interno;
- OpenAI-compatible API;
- LLM privado;
- outro serviço HTTP.

SEGURANÇA:

Credenciais nunca ficam no código.

Configurações:

    AI_CORPORATE_URL
    AI_CORPORATE_API_KEY
    AI_CORPORATE_TIMEOUT

============================================================
"""

import os
from typing import Dict, Any

import requests


class AIProviderClient:
    """
    Cliente HTTP genérico para serviços de IA.
    """

    def __init__(
        self,
        url: str = None,
        api_key: str = None,
        timeout: int = None
    ):
        """
        Inicializa o cliente.

        Args:
            url:
                URL da API de IA.

            api_key:
                Chave de autenticação.

            timeout:
                Tempo máximo de espera da requisição.
        """

        self.url = url or os.getenv(
            "AI_CORPORATE_URL",
            ""
        )

        self.api_key = api_key or os.getenv(
            "AI_CORPORATE_API_KEY",
            ""
        )

        timeout_value = timeout or os.getenv(
            "AI_CORPORATE_TIMEOUT",
            "60"
        )

        try:

            self.timeout = int(timeout_value)

        except ValueError:

            raise ValueError(
                "AI_CORPORATE_TIMEOUT deve ser um número inteiro."
            )

        if self.timeout <= 0:

            raise ValueError(
                "AI_CORPORATE_TIMEOUT deve ser maior que zero."
            )


    # ========================================================
    # VALIDAÇÃO
    # ========================================================

    def _validate(self):
        """
        Valida as configurações necessárias.
        """

        if not self.url:

            raise ValueError(
                "AI_CORPORATE_URL não configurada."
            )


    # ========================================================
    # HEADERS
    # ========================================================

    def _build_headers(self) -> Dict[str, str]:
        """
        Cria os headers HTTP da requisição.

        A API Key nunca é retornada em logs.
        """

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        if self.api_key:

            headers["Authorization"] = (
                f"Bearer {self.api_key}"
            )

        return headers


    # ========================================================
    # ENVIO
    # ========================================================

    def send(
        self,
        payload: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Envia um payload para o serviço de IA.

        Args:
            payload:
                Dados que serão enviados para a IA.

        Returns:
            Resposta JSON da API.
        """

        self._validate()

        try:

            response = requests.post(
                self.url,
                json=payload,
                headers=self._build_headers(),
                timeout=self.timeout
            )

        except requests.exceptions.Timeout as error:

            raise RuntimeError(
                "Timeout ao comunicar com o AI Provider."
            ) from error

        except requests.exceptions.ConnectionError as error:

            raise RuntimeError(
                "Não foi possível conectar ao AI Provider."
            ) from error

        except requests.exceptions.RequestException as error:

            raise RuntimeError(
                "Erro durante a comunicação com o AI Provider."
            ) from error


        # ====================================================
        # HTTP ERROR
        # ====================================================

        try:

            response.raise_for_status()

        except requests.exceptions.HTTPError as error:

            raise RuntimeError(
                f"AI Provider retornou HTTP "
                f"{response.status_code}."
            ) from error


        # ====================================================
        # JSON
        # ====================================================

        try:

            return response.json()

        except ValueError as error:

            raise RuntimeError(
                "AI Provider retornou uma resposta "
                "que não é JSON válido."
            ) from error


# ============================================================
# TESTE DIRETO
# ============================================================

if __name__ == "__main__":

    print("==========================================")
    print("MÓDULO 8.10.8 - AI PROVIDER CLIENT")
    print("==========================================")
    print()

    try:

        client = AIProviderClient()

        client._validate()

        print("URL configurada.")

        print(
            f"Timeout: {client.timeout}s"
        )

        print()
        print(
            "AI Provider Client validado."
        )

        print()
        print(
            "Pronto para comunicação com "
            "a API corporativa."
        )

    except ValueError as error:

        print(
            f"Configuração: {error}"
        )

    except Exception as error:

        print(
            f"Erro: {error}"
        )