"""
============================================================
MÓDULO 8.3
PREPARAÇÃO DOS DADOS PARA ANÁLISE DE IA
============================================================

Objetivo:

Ler diretamente os resultados gerados pelo Robot Framework
e transformar esses dados em um contexto estruturado para
a futura camada de Inteligência Artificial.

IMPORTANTE:

Este módulo NÃO depende do Allure.

Fonte principal:

    results/output.xml

Saída:

    ai/data/execution_context.json

Arquitetura:

    Robot Framework
          |
          v
    results/output.xml
          |
          v
    prepare_execution_data.py
          |
          v
    execution_context.json

============================================================
"""

import json
import sys
from pathlib import Path
import xml.etree.ElementTree as ET


# ============================================================
# CONFIGURAÇÃO DE CAMINHOS
# ============================================================

# Diretório raiz do projeto.
#
# O script está em:
#
#     ai/scripts/
#
# Portanto precisamos subir dois níveis:
#
#     scripts -> ai -> projeto
#


PROJECT_ROOT = Path(__file__).resolve().parents[2]


# Resultado produzido pelo Robot Framework.

RESULTS_DIR = PROJECT_ROOT / "results"

OUTPUT_XML = RESULTS_DIR / "output.xml"


# Diretório de dados da IA.

AI_DATA_DIR = PROJECT_ROOT / "ai" / "data"

EXECUTION_CONTEXT_FILE = AI_DATA_DIR / "execution_context.json"


# ============================================================
# FUNÇÕES AUXILIARES
# ============================================================


def get_text(element, tag, default=""):
    """
    Obtém o texto de um elemento XML.

    Caso o elemento não exista, retorna o valor default.
    """

    child = element.find(tag)

    if child is not None and child.text:
        return child.text.strip()

    return default


def get_status(test):
    """
    Obtém o status do teste Robot Framework.

    Possíveis valores:

        PASS
        FAIL
        SKIP
    """

    status = test.find("status")

    if status is None:
        return "UNKNOWN"

    return status.attrib.get("status", "UNKNOWN").upper()


def get_message(test):
    """
    Obtém a mensagem de erro do teste.

    O Robot Framework normalmente coloca a mensagem no
    elemento <status>.
    """

    status = test.find("status")

    if status is None:
        return ""

    return status.text.strip() if status.text else ""


def get_keywords(test):
    """
    Obtém as keywords executadas pelo teste.

    Isso será importante posteriormente para a IA entender
    em qual etapa ocorreu a falha.
    """

    keywords = []

    for keyword in test.findall(".//kw"):
        name = keyword.attrib.get("name", "").strip()

        if not name:
            continue

        status = keyword.find("status")

        keyword_status = "UNKNOWN"

        if status is not None:
            keyword_status = status.attrib.get(
                "status",
                "UNKNOWN"
            ).upper()

        keywords.append(
            {
                "name": name,
                "status": keyword_status
            }
        )

    return keywords


def parse_robot_results():
    """
    Lê o output.xml do Robot Framework.

    Retorna os dados estruturados da execução.
    """

    if not OUTPUT_XML.exists():

        print()
        print("ERRO: arquivo do Robot Framework não encontrado.")
        print()
        print(f"Esperado:")
        print(f"  {OUTPUT_XML}")
        print()

        sys.exit(1)


    print("Lendo resultados do Robot Framework...")

    print(f"Arquivo:")
    print(f"  {OUTPUT_XML}")

    print()


    # --------------------------------------------------------
    # Carrega XML
    # --------------------------------------------------------

    try:

        tree = ET.parse(OUTPUT_XML)

        root = tree.getroot()

    except ET.ParseError as error:

        print()
        print("ERRO: não foi possível interpretar o output.xml.")
        print()
        print(error)

        sys.exit(1)


    # --------------------------------------------------------
    # Localiza testes
    # --------------------------------------------------------

    tests = root.findall(".//test")


    print(f"Testes encontrados: {len(tests)}")


    # --------------------------------------------------------
    # Contadores
    # --------------------------------------------------------

    total = 0
    passed = 0
    failed = 0
    skipped = 0


    failures = []


    # ========================================================
    # PROCESSAR TESTES
    # ========================================================

    for test in tests:

        name = test.attrib.get(
            "name",
            "Teste sem nome"
        ).strip()


        status = get_status(test)

        message = get_message(test)

        keywords = get_keywords(test)


        total += 1


        # ----------------------------------------------------
        # PASS
        # ----------------------------------------------------

        if status == "PASS":

            passed += 1


        # ----------------------------------------------------
        # FAIL
        # ----------------------------------------------------

        elif status == "FAIL":

            failed += 1


            failures.append(
                {
                    "name": name,

                    "status": "failed",

                    "message": message,

                    "keywords": keywords
                }
            )


        # ----------------------------------------------------
        # SKIP
        # ----------------------------------------------------

        elif status in ("SKIP", "SKIPPED"):

            skipped += 1


        # ----------------------------------------------------
        # Outros estados
        # ----------------------------------------------------

        else:

            # Mantemos o teste contabilizado no total,
            # mas não classificamos como sucesso ou falha.

            pass


    # ========================================================
    # TAXA DE SUCESSO
    # ========================================================

    success_rate = 0.0


    if total > 0:

        success_rate = round(
            (passed / total) * 100,
            2
        )


    # ========================================================
    # CONTEXTO DA EXECUÇÃO
    # ========================================================

    execution_context = {

        "execution": {

            "total": total,

            "passed": passed,

            "failed": failed,

            "skipped": skipped,

            "success_rate": success_rate,

            "failures": failures
        },


        "environment": {

            "application": "SimulaBank",

            "framework": "Robot Framework"
        },


        "source": {

            "results_directory": str(
                RESULTS_DIR
            ),

            "robot_output": str(
                OUTPUT_XML
            )
        }
    }


    return execution_context


# ============================================================
# SALVAR CONTEXTO
# ============================================================


def save_execution_context(context):

    AI_DATA_DIR.mkdir(
        parents=True,
        exist_ok=True
    )


    with open(
        EXECUTION_CONTEXT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            context,
            file,
            indent=4,
            ensure_ascii=False
        )


# ============================================================
# EXECUÇÃO PRINCIPAL
# ============================================================


def main():

    print("=" * 42)

    print("MÓDULO 8.3 - PREPARAÇÃO DOS DADOS")

    print("=" * 42)

    print()

    print(f"Projeto: {PROJECT_ROOT}")

    print(f"Robot:   {OUTPUT_XML}")

    print()


    # --------------------------------------------------------
    # Processar Robot
    # --------------------------------------------------------

    context = parse_robot_results()


    # --------------------------------------------------------
    # Salvar resultado
    # --------------------------------------------------------

    save_execution_context(context)


    print()

    print("Contexto da execução criado:")

    print(
        EXECUTION_CONTEXT_FILE
    )


    # ========================================================
    # RESUMO
    # ========================================================

    execution = context["execution"]


    print()

    print("=" * 42)

    print("RESUMO")

    print("=" * 42)

    print(
        f"Total: {execution['total']}"
    )

    print(
        f"Passed: {execution['passed']}"
    )

    print(
        f"Failed: {execution['failed']}"
    )

    print(
        f"Skipped: {execution['skipped']}"
    )

    print(
        f"Success Rate: {execution['success_rate']}%"
    )


    print()


if __name__ == "__main__":

    main()