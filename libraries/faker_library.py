from robot.api.deco import keyword, library
from faker import Faker


@library(scope="GLOBAL")
class FakerLibrary:


    """
    Biblioteca responsável por gerar
    dados dinâmicos para testes.
    """


    def __init__(self):

        self.faker = Faker("pt_BR")


    ############################################################
    # Gera nome completo aleatório
    ############################################################

    @keyword("Gerar Nome Aleatorio")
    def gerar_nome_aleatorio(self):

        return self.faker.name()



    ############################################################
    # Gera email aleatório
    ############################################################

    @keyword("Gerar Email Aleatorio")
    def gerar_email_aleatorio(self):

        return self.faker.email()



    ############################################################
    # Gera telefone aleatório
    ############################################################

    @keyword("Gerar Telefone Aleatorio")
    def gerar_telefone_aleatorio(self):

        return self.faker.phone_number()



    ############################################################
    # Gera CPF aleatório
    ############################################################

    @keyword("Gerar CPF Aleatorio")
    def gerar_cpf_aleatorio(self):

        return self.faker.cpf()



    ############################################################
    # Gera cliente completo
    ############################################################

    @keyword("Gerar Cliente Completo")
    def gerar_cliente_completo(self):

        cliente = {

            "nome": self.faker.name(),

            "email": self.faker.email(),

            "cpf": self.faker.cpf(),

            "telefone": self.faker.phone_number()

        }


        return cliente