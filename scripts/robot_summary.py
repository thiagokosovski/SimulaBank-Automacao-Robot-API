"""
Robot Framework Summary Generator

Lê o arquivo output.xml do Robot Framework e publica
um resumo da execução na aba Summary do GitHub Actions.
"""

from pathlib import Path
from xml.etree import ElementTree as ET
import os
import platform
import sys


OUTPUT_FILE = Path("results/output.xml")
SUMMARY_FILE = os.environ.get("GITHUB_STEP_SUMMARY")


def load_robot_output():
    """
    Carrega o output.xml do Robot Framework.
    """

    if not OUTPUT_FILE.exists():
        raise FileNotFoundError(
            f"Arquivo não encontrado: {OUTPUT_FILE}"
        )

    return ET.parse(OUTPUT_FILE).getroot()


def get_statistics(root):
    """
    Extrai estatísticas da execução.
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
        (passed / total) * 100 if total > 0 else 0
    )

    return {
        "total": total,
        "passed": passed,
        "failed": failed,
        "success_rate": success_rate,
    }


def write_table(file, data):
    """
    Escreve uma tabela Markdown.
    """

    file.write("| Item | Value |\n")
    file.write("|------|-------|\n")

    for key, value in data.items():
        file.write(f"| {key} | {value} |\n")


def write_summary(stats):
    """
    Escreve o resumo para o GitHub Actions.
    """

    if SUMMARY_FILE is None:
        print("GITHUB_STEP_SUMMARY não encontrado.")
        return

    status = (
        "✅ SUCCESS"
        if stats["failed"] == 0
        else "❌ FAILURE"
    )

    with open(SUMMARY_FILE, "a", encoding="utf-8") as summary:

        summary.write("\n")

        summary.write("# 📊 Robot Framework Statistics\n\n")

        write_table(
            summary,
            {
                "Total Tests": stats["total"],
                "Passed": f"✅ {stats['passed']}",
                "Failed": f"❌ {stats['failed']}",
                "Success Rate": f"{stats['success_rate']:.2f}%",
                "Result": status,
            },
        )

        summary.write("\n")

        summary.write("## 🖥 Runtime\n\n")

        write_table(
            summary,
            {
                "Python": platform.python_version(),
                "Platform": platform.system(),
                "Architecture": platform.machine(),
            },
        )

        summary.write("\n")

        summary.write("## 📂 Reports\n\n")

        reports = [
            "output.xml",
            "report.html",
            "log.html",
        ]

        for report in reports:

            report_path = Path("results") / report

            if report_path.exists():
                summary.write(f"- ✅ {report}\n")
            else:
                summary.write(f"- ❌ {report}\n")


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


if __name__ == "__main__":
    main()