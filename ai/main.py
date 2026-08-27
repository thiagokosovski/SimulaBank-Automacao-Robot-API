"""
============================================================
SIMULABANK - AI QUALITY INTELLIGENCE
MÓDULO 8
============================================================

Arquivo:
    main.py

Responsabilidade:

Este é o ponto de entrada do módulo de Inteligência
de Qualidade.

Neste primeiro estágio, ele apenas:

1. Executa o Robot Collector
2. Recebe os resultados do Robot Framework
3. Exibe um resumo da execução

IMPORTANTE:

Este módulo NÃO executa os testes.

Ele apenas analisa os resultados que já foram gerados.

Fluxo:

    Robot Framework
          ↓
    results/output.xml
          ↓
    robot_collector.py
          ↓
    main.py
============================================================
"""

from collectors.robot_collector import collect_robot_results


def main():
    """
    Função principal do módulo de IA.
    """

    # ========================================================
    # 1. COLETAR RESULTADOS DO ROBOT
    # ========================================================

    print("")
    print("=" * 60)
    print("SIMULABANK - AI QUALITY INTELLIGENCE")
    print("=" * 60)
    print("")

    print("Coletando resultados do Robot Framework...")
    print("")

    results = collect_robot_results()

    # ========================================================
    # 2. EXIBIR RESUMO
    # ========================================================

    print("RESULTADO DA EXECUÇÃO")
    print("-" * 60)

    print(f"Total de testes : {results['total']}")
    print(f"Testes aprovados: {results['passed']}")
    print(f"Testes falhos   : {results['failed']}")
    print(f"Testes ignorados: {results['skipped']}")
    print(f"Taxa de sucesso : {results['success_rate']}%")

    print("")

    # ========================================================
    # 3. EXIBIR FALHAS
    # ========================================================

    if results["failed"] > 0:

        print("TESTES COM FALHA")
        print("-" * 60)

        for test in results["tests"]:

            if test["status"] == "FAIL":

                print("")
                print(f"Teste: {test['name']}")
                print(f"Erro : {test['message']}")

    else:

        print("Nenhum teste falhou.")

    print("")
    print("=" * 60)
    print("ANÁLISE INICIAL FINALIZADA")
    print("=" * 60)
    print("")


# ============================================================
# EXECUÇÃO DO PROGRAMA
# ============================================================

if __name__ == "__main__":

    main()