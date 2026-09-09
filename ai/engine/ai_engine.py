"""
============================================================
MÓDULO 8.10.5 - AI ENGINE
============================================================

Responsabilidade:

Orquestrar a análise de qualidade utilizando o AI Provider
configurado no projeto.

O AI Engine NÃO conhece detalhes específicos de:

- OpenAI;
- Azure;
- IA Corporativa;
- modelo local;
- Ollama;
- outros fornecedores.

Ele trabalha exclusivamente através da interface
BaseAIProvider e da Provider Factory.

Fluxo:

    Quality Report
          |
          v
      AI Engine
          |
          v
    Provider Factory
          |
          v
    AI Provider
          |
          v
    AI Analysis Result

============================================================
"""

import json
from pathlib import Path
from typing import Dict, Any

from ai.providers.provider_factory import get_ai_provider


# ============================================================
# CAMINHOS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "ai" / "data"

INPUT_FILE = DATA_DIR / "ai_quality_report.json"

OUTPUT_FILE = DATA_DIR / "ai_engine_result.json"


# ============================================================
# LEITURA DO RELATÓRIO
# ============================================================

def load_quality_report() -> Dict[str, Any]:
    """
    Carrega o relatório de qualidade produzido pelos módulos
    anteriores.
    """

    if not INPUT_FILE.exists():

        raise FileNotFoundError(
            f"Relatório não encontrado: {INPUT_FILE}"
        )

    with open(
        INPUT_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


# ============================================================
# SALVAR RESULTADO
# ============================================================

def save_result(result: Dict[str, Any]) -> None:
    """
    Salva o resultado produzido pelo AI Provider.
    """

    DATA_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            result,
            file,
            indent=4,
            ensure_ascii=False
        )


# ============================================================
# EXECUÇÃO DO ENGINE
# ============================================================

def run_ai_engine() -> Dict[str, Any]:
    """
    Executa o processo de análise através do provider
    configurado.
    """

    print("Carregando relatório de qualidade...")

    context = load_quality_report()

    print("Obtendo AI Provider...")

    provider = get_ai_provider()

    print(
        f"Provider utilizado: "
        f"{provider.get_provider_name()}"
    )

    print(
        f"Modelo utilizado: "
        f"{provider.model}"
    )

    print("Enviando contexto para o AI Provider...")

    result = provider.analyze(context)

    save_result(result)

    return result


# ============================================================
# EXECUÇÃO DIRETA
# ============================================================

if __name__ == "__main__":

    print("==========================================")
    print("MÓDULO 8.10.5 - AI ENGINE")
    print("==========================================")
    print()

    result = run_ai_engine()

    print()
    print("Análise concluída.")
    print()
    print(f"Resultado:")
    print(OUTPUT_FILE)