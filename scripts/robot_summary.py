"""
Robot Framework Summary Generator

Lê o arquivo output.xml do Robot Framework e publica
um resumo da execução na aba Summary do GitHub Actions.
"""

############################################################
# Imports
############################################################

from pathlib import Path
from xml.etree import ElementTree as ET
import os
import platform
import sys

############################################################
# Constantes
############################################################

OUTPUT_FILE = Path("results/output.xml")
REPORTS_DIR = Path("results")
SUMMARY_FILE = os.environ.get("GITHUB_STEP_SUMMARY")

############################################################
# Carrega o output.xml
############################################################

def load_robot_output():
    """
    Carrega o arquivo output.xml do Robot Framework.
    """

    if not OUTPUT_FILE.exists():
        raise FileNotFoundError(
            f"Arquivo não encontrado: {OUTPUT_FILE}"
        )

    return ET.parse(OUTPUT_FILE).getroot()


############################################################
# Extrai as estatísticas
############################################################

def get_statistics(root):
    """
    Obtém estatísticas da execução do Robot Framework.
    """

    statistics = root.find("statistics")

    if statistics is None:
        return None

    total_node = statistics.find("./total/stat")

    if total_node is None:
        return None

    passed = int(total_node.attrib.get("pass", 0))
    failed = int(total_node.attrib.get("fail", 0))
    total = passed + failed

    success_rate = (
        (passed / total) * 100
        if total > 0
        else 0
    )

    result = (
        "✅ SUCCESS"
        if failed == 0
        else "❌ FAILURE"
    )

    return {
        "total": total,
        "passed": passed,
        "failed": failed,
        "success_rate": success_rate,
        "result": result,
    }


############################################################
# Escreve uma tabela Markdown
############################################################

def write_table(file, data):
    """
    Escreve uma tabela Markdown.
    """

    file.write("| Item | Value |\n")
    file.write("|------|-------|\n")

    for key, value in data.items():
        file.write(f"| {key} | {value} |\n")

    file.write("\n")


############################################################
# Resumo da execução
############################################################

def write_execution_summary(file, stats):
    """
    Escreve o resumo da execução.
    """

    file.write("## 📊 Test Execution Summary\n\n")

    write_table(
        file,
        {
            "Total Tests": stats["total"],
            "Passed": f"✅ {stats['passed']}",
            "Failed": f"❌ {stats['failed']}",
            "Success Rate": f"{stats['success_rate']:.2f}%",
            "Final Result": stats["result"],
        },
    )


############################################################
# Informações do ambiente
############################################################

def write_runtime(file):
    """
    Escreve informações do ambiente de execução.
    """

    file.write("## 🖥 Runtime\n\n")

    write_table(
        file,
        {
            "Python": platform.python_version(),
            "Platform": platform.system(),
            "Architecture": platform.machine(),
        },
    )


############################################################
# Relatórios gerados
############################################################

def write_reports(file):
    """
    Lista os relatórios gerados pelo Robot Framework.
    """

    file.write("## 📂 Robot Reports\n\n")

    reports = [
        "output.xml",
        "log.html",
        "report.html",
    ]

    for report in reports:

        report_path = REPORTS_DIR / report

        if report_path.exists():
            file.write(f"- ✅ {report}\n")
        else:
            file.write(f"- ❌ {report}\n")

    file.write("\n")


############################################################
# Rodapé
############################################################

def write_footer(file):
    """
    Escreve o rodapé do Summary.
    """

    file.write("---\n\n")
    file.write("Job summary generated automatically by Robot Framework.\n")


############################################################
# Gera o Summary
############################################################

def write_summary(stats):
    """
    Escreve o resumo completo para o GitHub Actions.
    """

    if SUMMARY_FILE is None:
        print("GITHUB_STEP_SUMMARY não encontrado.")
        return

    with open(SUMMARY_FILE, "a", encoding="utf-8") as summary:

        summary.write("\n")

        summary.write("# 🤖 Robot Framework API Execution\n\n")

        write_execution_summary(summary, stats)

        write_runtime(summary)

        write_reports(summary)

        write_footer(summary)


############################################################
# Main
############################################################

def main():

    try:

        root = load_robot_output()

        stats = get_statistics(root)

        if stats is None:
            print("Não foi possível obter estatísticas.")
            sys.exit(1)

        write_summary(stats)

        print("Resumo gerado com sucesso.")

    except Exception as error:

        print(error)

        sys.exit(1)


############################################################
# Ponto de entrada
############################################################

if __name__ == "__main__":
    main()