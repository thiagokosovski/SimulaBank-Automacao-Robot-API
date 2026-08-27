"""
============================================================
MÓDULO 8.10.1 - AI PROVIDER INTERFACE
============================================================

Responsabilidade:

Definir o contrato que todos os motores de IA deverão seguir.

Este módulo NÃO realiza chamadas para nenhuma IA.

Ele apenas define uma interface comum.

Exemplos de futuros providers:

    OpenAI
    Azure
    IA Corporativa
    Modelo Local
    Ollama
    Outro fornecedor

Objetivo:

Desacoplar o AI Engine do fornecedor de IA.

Assim:

    AI Engine
         |
         v
    AI Provider
         |
    +----+-----+---------+
    |          |         |
  OpenAI     Azure    Corporate
============================================================
"""

from abc import ABC, abstractmethod
from typing import Dict, Any


class BaseAIProvider(ABC):
    """
    Interface base para qualquer provedor de IA.
    """

    def __init__(self, model: str):
        """
        Inicializa o provider.

        Args:
            model:
                Nome do modelo que será utilizado.
        """

        self.model = model

    @abstractmethod
    def analyze(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analisa os dados de qualidade.

        Cada provider deverá implementar este método.

        Args:
            context:
                Dados preparados para análise da IA.

        Returns:
            Dicionário contendo a análise.
        """

        raise NotImplementedError

    @abstractmethod
    def get_provider_name(self) -> str:
        """
        Retorna o nome do provider.
        """

        raise NotImplementedError