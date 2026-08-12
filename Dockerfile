############################################################
# IMAGEM BASE
#
# Utilizamos Python 3.9 porque é a mesma versão utilizada
# atualmente no projeto e no GitHub Actions.
############################################################

FROM python:3.9-slim


############################################################
# DIRETÓRIO DE TRABALHO
#
# Tudo que será executado dentro do container ficará
# dentro deste diretório.
############################################################

WORKDIR /app


############################################################
# VARIÁVEIS DE AMBIENTE
#
# Evita que o Python gere arquivos .pyc e garante que os
# logs apareçam imediatamente no terminal.
############################################################

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1


############################################################
# COPIA O REQUIREMENTS
#
# Copiamos primeiro apenas o requirements.txt.
#
# Isso permite que o Docker aproveite o cache dessa camada
# quando o código dos testes mudar, mas as dependências
# continuarem iguais.
############################################################

COPY requirements.txt .


############################################################
# INSTALA AS DEPENDÊNCIAS
#
# Instala todas as bibliotecas utilizadas pelo projeto.
#
# O requirements.txt já possui:
#
# - Robot Framework
# - RequestsLibrary
# - JSONLibrary
# - JSON Schema
# - Faker
# - PyYAML
# - python-dotenv
#
############################################################

RUN pip install --no-cache-dir -r requirements.txt


############################################################
# COPIA O PROJETO
#
# Depois das dependências instaladas, copiamos os arquivos
# do projeto para dentro do container.
############################################################

COPY . .


############################################################
# CRIA DIRETÓRIO DE RESULTADOS
#
# O Robot utilizará esse diretório para armazenar:
#
# output.xml
# log.html
# report.html
# summary.md
#
############################################################

RUN mkdir -p results


############################################################
# COMANDO PADRÃO
#
# Quando o container for iniciado, executamos o mesmo
# script que já utilizamos localmente.
############################################################

CMD ["python", "tools/run_robot.py"]