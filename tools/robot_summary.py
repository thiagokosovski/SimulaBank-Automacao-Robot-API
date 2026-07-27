from pathlib import Path
from datetime import datetime
import xml.etree.ElementTree as ET
import os
import platform


class RobotSummary:

    # ==========================================================
    # Informações do ambiente GitHub Actions
    # ==========================================================

    def generate_environment_info(self):

        return f"""

        ## Workflow Information

        | Item | Value |
        |------|-------|
        | Workflow | {os.getenv('GITHUB_WORKFLOW','Local Execution')} |
        | Repository | {os.getenv('GITHUB_REPOSITORY','Local')} |
        | Branch | {os.getenv('GITHUB_REF_NAME','Local')} |
        | Commit | {os.getenv('GITHUB_SHA','Local')[:7]} |
        | Runner | {os.getenv('RUNNER_OS','Local')} |
        | Python | {platform.python_version()} |


        ## Environment Variables

        | Variable | Status |
        |----------|--------|
        | BASE_URL | ✅ Configured |
        | API_USERNAME | ✅ Configured |
        | API_PASSWORD | ✅ Configured |


        ## 🖥 Runtime

        | Item | Value |
        |------|-------|
        | Python | Python {platform.python_version()} |
        | Platform | {platform.system()} |
        | Architecture | {platform.machine()} |

        """

    """
    Responsável por ler o output.xml do Robot Framework
    e gerar um resumo da execução em Markdown.
    """

    def __init__(self):

        # Diretório principal dos resultados
        self.results_root = Path("results")

        # Pasta da última execução
        self.results_dir = None

        # Arquivo output.xml da última execução
        self.output_file = None

        self.tree = None
        self.root = None

        # Estatísticas da execução
        self.total = 0
        self.passed = 0
        self.failed = 0
        self.suites = 0
        self.success_rate = 0.0

        # Lista contendo todos os testes executados
        self.executed_tests = []

    # ==========================================================
    # Carrega o arquivo output.xml
    # ==========================================================

    def load_output(self):

        self.find_latest_execution()

        if not self.output_file.exists():
            raise FileNotFoundError(
                self.output_file
            )

        self.tree = ET.parse(self.output_file)
        self.root = self.tree.getroot()

    # ==========================================================
    # Conta testes executados
    # ==========================================================

    def count_tests(self):

        tests = self.root.findall(".//test")

        self.total = len(tests)

        self.passed = 0
        self.failed = 0

        self.executed_tests = []

        for test in tests:

            # Obtém o nome do caso de teste
            test_name = test.attrib.get("name", "Unknown Test")

            status = test.find("status")

            if status is None:
                continue

            if status.attrib["status"] == "PASS":

                self.passed += 1

                # Armazena o cenário aprovado
                self.executed_tests.append(
                    ("PASS", test_name)
                )

            elif status.attrib["status"] == "FAIL":

                self.failed += 1

                # Armazena o cenário reprovado
                self.executed_tests.append(
                    ("FAIL", test_name)
                )

    # ==========================================================
    # Conta suítes executadas
    # ==========================================================

    def count_suites(self):

        suites = self.root.findall("./suite/suite")

        self.suites = len(suites)

    # ==========================================================
    # Calcula a taxa de sucesso
    # ==========================================================

    def calculate_success_rate(self):

        if self.total == 0:
            self.success_rate = 0
            return

        self.success_rate = round(
            (self.passed / self.total) * 100,
            2
        )

    # ==========================================================
    # Gera o conteúdo Markdown do Dashboard
    # ==========================================================

    # ==========================================================
    # Gera o conteúdo Markdown do Dashboard
    # ==========================================================

    def generate_markdown(self):

        generated_at = datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

        markdown = f"""# 🤖 Robot Framework API Execution

    {self.generate_environment_info()}  

    ## 📁 Execution Information

    | Item | Value |
    |------|-------|
    | Execution Folder | {self.results_dir} |
    | Generated At | {generated_at} |

    ---

    ## 📊 Test Execution Summary

    | Item | Value |
    |------|-------|
    | Suites | {self.suites} |
    | Total Tests | {self.total} |
    | Passed | ✅ {self.passed} |
    | Failed | ❌ {self.failed} |
    | Success Rate | {self.success_rate}% |

    ---

    ## ✅ Executed Test Cases

    | Status | Test Case |
    |--------|-----------|
    """

        for status, test_name in self.executed_tests:

            icon = "✅" if status == "PASS" else "❌"

            markdown += (
                f"| {icon} {status} | {test_name} |\n"
            )

        return markdown

    # ==========================================================
    # Salva o Dashboard em summary.md
    # ==========================================================

    def save_summary(self):

        summary = self.generate_markdown()

        summary_file = self.results_dir / "summary.md"

        summary_file.write_text(
            summary,
            encoding="utf-8"
        )


    # ==========================================================
    # Exibe um resumo da execução no terminal
    # ==========================================================

    def print_console_summary(self):

        print()

        print("=" * 60)
        print("             ROBOT FRAMEWORK EXECUTION SUMMARY")
        print("=" * 60)

        print()

        print(f"Execution Folder : {self.results_dir}")

        print()

        print(f"Suites           : {self.suites}")
        print(f"Total Tests      : {self.total}")
        print(f"Passed           : {self.passed}")
        print(f"Failed           : {self.failed}")
        print(f"Success Rate     : {self.success_rate}%")

        print()

        print("-" * 60)
        print("Executed Test Cases")
        print("-" * 60)

        print()

        for status, name in self.executed_tests:

            print(f"{status:<5} {name}")

        print()

        print("=" * 60)    


    def find_latest_execution(self):

        if not self.results_root.exists():
            raise FileNotFoundError(
                "Directory 'results' not found."
            )

        executions = [
            folder
            for folder in self.results_root.iterdir()
            if folder.is_dir()
        ]

        if not executions:
            raise FileNotFoundError(
                "No Robot execution found."
            )

        self.results_dir = max(
            executions,
            key=lambda folder: folder.stat().st_mtime
        )

        self.output_file = (
            self.results_dir / "output.xml"
        )       

    # ==========================================================
    # Fluxo principal da aplicação
    # ==========================================================

    def run(self):

        self.load_output()

        self.count_tests()

        self.count_suites()

        self.calculate_success_rate()

        self.save_summary()

        self.calculate_success_rate()
        
        self.print_console_summary()

# ==========================================================
# Ponto de entrada da aplicação
# ==========================================================

if __name__ == "__main__":

    RobotSummary().run()