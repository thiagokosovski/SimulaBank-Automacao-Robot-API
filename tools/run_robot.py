from pathlib import Path
from datetime import datetime
import subprocess
import sys


sys.path.append(
    str(Path(__file__).parent)
)


from robot_summary import RobotSummary



class RobotRunner:
    """
    Responsável por controlar toda execução do framework.
    """


    def __init__(self):

        # Pasta principal dos resultados
        self.results_root = Path("results")


        # Cria caso não exista
        self.results_root.mkdir(
            exist_ok=True
        )


        # Nome único da execução
        execution_name = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )


        # Pasta desta execução
        self.execution_dir = (
            self.results_root /
            execution_name
        )



    # ==========================================================
    # Executa Robot Framework
    # ==========================================================

    def execute_robot(self):

        command = [
            "robot",
            "--outputdir",
            str(self.execution_dir),
            "tests"
        ]


        result = subprocess.run(
            command
        )


        if result.returncode == 0:

            print(
                "\nRobot execution finished successfully."
            )

        else:

            print(
                "\nRobot execution finished with failures."
            )

            print(
                "Reports were generated successfully."
            )



    # ==========================================================
    # Gera summary.md
    # ==========================================================

    def generate_summary(self):


        summary = RobotSummary()


        summary.run()



    # ==========================================================
    # Fluxo principal
    # ==========================================================

    def run(self):


        self.execute_robot()


        self.generate_summary()



if __name__ == "__main__":


    RobotRunner().run()