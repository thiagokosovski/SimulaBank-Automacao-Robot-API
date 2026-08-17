# ============================================================
# Execução dos testes Robot Framework com Allure
#
# Objetivo:
# Executar os testes utilizando o listener do Allure,
# mantendo os relatórios tradicionais do Robot em results/
# e os artefatos do Allure em output/allure/.
#
# Este script NÃO altera os testes.
# ============================================================


# ============================================================
# Diretório raiz do projeto
# ============================================================

$ProjectRoot = Split-Path -Parent $PSScriptRoot

Set-Location $ProjectRoot


# ============================================================
# Diretórios de saída
# ============================================================

$RobotOutput = "results"

$AllureOutput = "output/allure"


# ============================================================
# Garantir que o diretório do Allure exista
# ============================================================

if (-not (Test-Path $AllureOutput)) {

    New-Item `
        -ItemType Directory `
        -Path $AllureOutput `
        -Force | Out-Null
}


# ============================================================
# Limpar resultados anteriores do Allure
#
# IMPORTANTE:
# Somente os resultados do Allure são removidos.
#
# Os arquivos tradicionais em results/ não são alterados.
# ============================================================

Remove-Item `
    "$AllureOutput\*" `
    -Recurse `
    -Force `
    -ErrorAction SilentlyContinue


# ============================================================
# Executar Robot Framework
# ============================================================

robot `
    --listener allure_robotframework `
    --outputdir $RobotOutput `
    tests


# ============================================================
# Capturar código de retorno
# ============================================================

$ExitCode = $LASTEXITCODE


# ============================================================
# Resultado da execução
# ============================================================

if ($ExitCode -eq 0) {

    Write-Host ""
    Write-Host "============================================================"
    Write-Host "TESTES EXECUTADOS COM SUCESSO"
    Write-Host "============================================================"
    Write-Host ""
    Write-Host "Relatorios Robot:"
    Write-Host "  $RobotOutput"
    Write-Host ""
    Write-Host "Resultados Allure:"
    Write-Host "  $AllureOutput"
    Write-Host ""
}
else {

    Write-Host ""
    Write-Host "============================================================"
    Write-Host "TESTES FINALIZADOS COM FALHA"
    Write-Host "============================================================"
    Write-Host ""
    Write-Host "Relatorios Robot:"
    Write-Host "  $RobotOutput"
    Write-Host ""
    Write-Host "Resultados Allure:"
    Write-Host "  $AllureOutput"
    Write-Host ""
}


# ============================================================
# Retornar o mesmo código do Robot Framework
#
# Isso é importante para CI/CD.
#
# 0 = sucesso
# diferente de 0 = falha
# ============================================================

exit $ExitCode