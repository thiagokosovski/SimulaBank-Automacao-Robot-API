"""
============================================================
SIMULABANK - AI QUALITY INTELLIGENCE
MÓDULO: Robot Collector
============================================================

Responsabilidade:

Este módulo é responsável por ler o arquivo:

    results/output.xml

gerado pelo Robot Framework e transformar os resultados
dos testes em dados que poderão ser analisados posteriormente
pelo módulo de Inteligência de Qualidade.

IMPORTANTE:

Este módulo NÃO altera o resultado do Robot Framework.

Ele apenas lê as informações existentes.
============================================================
"""

from pathlib import Path
import xml.etree.ElementTree as ET


# ============================================================
# CAMINHO PADRÃO DO RESULTADO DO ROBOT
# ============================================================

DEFAULT_OUTPUT_FILE = Path("results/output.xml")


def collect_robot_results(output_file=DEFAULT_OUTPUT_FILE):
    """
    Lê o output.xml gerado pelo Robot Framework.

    Parâmetros:
        output_file:
            Caminho do arquivo output.xml.

    Retorno:
        Um dicionário contendo os resultados básicos
        da execução.
    """

    # --------------------------------------------------------
    # 1. Verificar se o arquivo existe
    # --------------------------------------------------------

    if not output_file.exists():

        raise FileNotFoundError(
            f"Arquivo do Robot Framework não encontrado: {output_file}"
        )

    # --------------------------------------------------------
    # 2. Ler o XML
    # --------------------------------------------------------

    tree = ET.parse(output_file)

    root = tree.getroot()

    # --------------------------------------------------------
    # 3. Estrutura que armazenará os resultados
    # --------------------------------------------------------

    results = {

        "total": 0,

        "passed": 0,

        "failed": 0,

        "skipped": 0,

        "tests": []

    }

    # --------------------------------------------------------
    # 4. Localizar todos os casos de teste
    # --------------------------------------------------------

    for test in root.iter("test"):

        # ----------------------------------------------------
        # Nome do teste
        # ----------------------------------------------------

        test_name = test.get("name", "Teste sem nome")

        # ----------------------------------------------------
        # Status
        # ----------------------------------------------------

        status_element = test.find("status")

        if status_element is None:

            continue

        status = status_element.get("status", "UNKNOWN")

        # ----------------------------------------------------
        # Mensagem de erro
        # ----------------------------------------------------

        message = status_element.get("message", "")

        # ----------------------------------------------------
        # Atualizar contador total
        # ----------------------------------------------------

        results["total"] += 1

        # ----------------------------------------------------
        # Classificar resultado
        # ----------------------------------------------------

        if status == "PASS":

            results["passed"] += 1

        elif status == "FAIL":

            results["failed"] += 1

        else:

            results["skipped"] += 1

        # ----------------------------------------------------
        # Guardar informações individuais do teste
        # ----------------------------------------------------

        results["tests"].append({

            "name": test_name,

            "status": status,

            "message": message

        })

    # --------------------------------------------------------
    # 5. Calcular taxa de sucesso
    # --------------------------------------------------------

    if results["total"] > 0:

        results["success_rate"] = round(
            (results["passed"] / results["total"]) * 100,
            2
        )

    else:

        results["success_rate"] = 0.0

    # --------------------------------------------------------
    # 6. Retornar resultados
    # --------------------------------------------------------

    return results