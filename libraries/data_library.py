from robot.api.deco import keyword, library
import yaml
from pathlib import Path


@library(scope="GLOBAL")
class DataLibrary:


    """
    Biblioteca responsável por carregar
    dados de testes externos.
    """


    @keyword("Carregar Yaml")
    def carregar_yaml(self, arquivo):

        project_root = Path(__file__).parent.parent

        caminho = (
            project_root
            / "test_data"
            / arquivo
        )


        with open(
            caminho,
            encoding="utf-8"
        ) as arquivo_yaml:

            dados = yaml.safe_load(
                arquivo_yaml
            )


        return dados