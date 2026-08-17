# ============================================================
# Execucao dos testes Robot Framework com Allure
#
# Objetivo:
# Executar os testes utilizando o listener do Allure,
# mantendo os relatorios tradicionais do Robot em results/
# e os artefatos do Allure em output/allure/.
#
# Responsabilidades:
# - Preparar resultados Allure
# - Restaurar historico anterior
# - Copiar configuracoes do Allure
# - Gerar executor.json
# - Executar Robot Framework
# - Gerar relatorio Allure
# - Atualizar historico persistente
#
# Este script NAO altera os testes.
# ============================================================


# ============================================================
# Diretorio raiz do projeto
# ============================================================

$ProjectRoot = Split-Path -Parent $PSScriptRoot

Set-Location $ProjectRoot


# ============================================================
# Diretorios
# ============================================================

$RobotOutput = "results"

$AllureOutput = "output/allure"

$AllureReport = "output/allure-report"

$AllureHistory = "output/allure-history"

$AllureConfig = "config/allure"


# ============================================================
# Arquivos de configuracao
# ============================================================

$CategoriesFile = "$AllureConfig/categories.json"

$EnvironmentFile = "$AllureConfig/environment.properties"

$BuildOrderFile = "$AllureHistory/.build-order"


# ============================================================
# Preparar diretorios
# ============================================================

New-Item `
    -ItemType Directory `
    -Path $AllureOutput `
    -Force | Out-Null


New-Item `
    -ItemType Directory `
    -Path $AllureHistory `
    -Force | Out-Null


# ============================================================
# Validar configuracoes
# ============================================================

if (-not (Test-Path $CategoriesFile)) {

    Write-Host ""
    Write-Host "ERRO: categories.json nao encontrado."
    Write-Host "  $CategoriesFile"
    Write-Host ""

    exit 1
}


if (-not (Test-Path $EnvironmentFile)) {

    Write-Host ""
    Write-Host "ERRO: environment.properties nao encontrado."
    Write-Host "  $EnvironmentFile"
    Write-Host ""

    exit 1
}


# ============================================================
# Limpar resultados anteriores do Allure
#
# IMPORTANTE:
# Somente output/allure e limpo.
#
# results/ NAO e alterado.
# output/allure-history NAO e alterado.
# ============================================================

Write-Host ""
Write-Host "============================================================"
Write-Host "PREPARANDO ALLURE"
Write-Host "============================================================"
Write-Host ""

Write-Host "Limpando resultados anteriores..."

Remove-Item `
    "$AllureOutput\*" `
    -Recurse `
    -Force `
    -ErrorAction SilentlyContinue


# ============================================================
# Restaurar historico anterior
#
# Somente arquivos JSON do historico sao copiados.
#
# O arquivo .build-order permanece fora da pasta history.
# ============================================================

$HistoryFiles = Get-ChildItem `
    $AllureHistory `
    -Filter "*.json" `
    -File `
    -ErrorAction SilentlyContinue


if ($HistoryFiles.Count -gt 0) {

    Write-Host "Restaurando historico anterior..."

    New-Item `
        -ItemType Directory `
        -Path "$AllureOutput/history" `
        -Force | Out-Null

    Copy-Item `
        "$AllureHistory\*.json" `
        "$AllureOutput\history\" `
        -Force
}
else {

    Write-Host "Nenhum historico anterior encontrado."
}


# ============================================================
# Copiar configuracoes do Allure
# ============================================================

Write-Host "Copiando configuracoes do Allure..."


Copy-Item `
    $CategoriesFile `
    "$AllureOutput/categories.json" `
    -Force


Copy-Item `
    $EnvironmentFile `
    "$AllureOutput/environment.properties" `
    -Force


# ============================================================
# Gerar numero incremental da execucao
#
# Exemplo:
#
# Execucao anterior = 1
# Nova execucao     = 2
#
# O contador fica persistido em:
#
# output/allure-history/.build-order
# ============================================================

$BuildOrder = 1


if (Test-Path $BuildOrderFile) {

    $BuildOrderContent = Get-Content `
        $BuildOrderFile `
        -Raw `
        -ErrorAction SilentlyContinue

    $ParsedBuildOrder = 0

    if ([int]::TryParse($BuildOrderContent.Trim(), [ref]$ParsedBuildOrder)) {

        $BuildOrder = $ParsedBuildOrder + 1
    }
}


Set-Content `
    -Path $BuildOrderFile `
    -Value $BuildOrder `
    -Encoding UTF8


# ============================================================
# Data e hora da execucao
# ============================================================

$ExecutionDateTime = Get-Date -Format "dd/MM/yyyy HH:mm"

$ReportName = "Execucao #$BuildOrder - $ExecutionDateTime"


# ============================================================
# Gerar executor.json
#
# O Allure utiliza este arquivo para identificar a execucao
# e alimentar o historico/trend.
# ============================================================

$Executor = @{
    name        = "Local"
    type        = "generic"
    buildName   = "SimulaBank Automation"
    buildOrder  = $BuildOrder
    reportName  = $ReportName
}


$ExecutorJson = $Executor | ConvertTo-Json -Depth 10


Set-Content `
    -Path "$AllureOutput/executor.json" `
    -Value $ExecutorJson `
    -Encoding UTF8


Write-Host ""
Write-Host "Execucao Allure:"
Write-Host "  $ReportName"
Write-Host ""


# ============================================================
# Executar Robot Framework
# ============================================================

Write-Host "============================================================"
Write-Host "EXECUTANDO TESTES"
Write-Host "============================================================"
Write-Host ""

robot `
    --listener allure_robotframework `
    --outputdir $RobotOutput `
    tests


# ============================================================
# Capturar codigo de retorno do Robot
# ============================================================

$ExitCode = $LASTEXITCODE


# ============================================================
# Gerar relatorio Allure
# ============================================================

Write-Host ""
Write-Host "============================================================"
Write-Host "GERANDO RELATORIO ALLURE"
Write-Host "============================================================"
Write-Host ""

allure generate `
    $AllureOutput `
    -o $AllureReport `
    --clean


# ============================================================
# Capturar codigo de retorno do Allure
# ============================================================

$AllureExitCode = $LASTEXITCODE


# ============================================================
# Atualizar historico persistente
#
# O Allure gera o historico atualizado em:
#
# output/allure-report/history/
# ============================================================

if ($AllureExitCode -eq 0) {

    $GeneratedHistory = "$AllureReport/history"

    if (Test-Path $GeneratedHistory) {

        Write-Host ""
        Write-Host "Atualizando historico do Allure..."

        Remove-Item `
            "$AllureHistory\*.json" `
            -Force `
            -ErrorAction SilentlyContinue

        Copy-Item `
            "$GeneratedHistory\*.json" `
            "$AllureHistory\" `
            -Force
    }
    else {

        Write-Host ""
        Write-Host "AVISO: Historico nao encontrado no relatorio Allure."
    }
}
else {

    Write-Host ""
    Write-Host "AVISO: Nao foi possivel atualizar o historico."
}


# ============================================================
# Resultado da execucao
# ============================================================

Write-Host ""

if ($ExitCode -eq 0) {

    Write-Host "============================================================"
    Write-Host "TESTES EXECUTADOS COM SUCESSO"
    Write-Host "============================================================"
}
else {

    Write-Host "============================================================"
    Write-Host "TESTES FINALIZADOS COM FALHA"
    Write-Host "============================================================"
}


Write-Host ""
Write-Host "Relatorios Robot:"
Write-Host "  $RobotOutput"
Write-Host ""

Write-Host "Resultados Allure:"
Write-Host "  $AllureOutput"
Write-Host ""

Write-Host "Relatorio Allure:"
Write-Host "  $AllureReport"
Write-Host ""

Write-Host "Historico:"
Write-Host "  $AllureHistory"
Write-Host ""

Write-Host "Build Order:"
Write-Host "  $BuildOrder"
Write-Host ""

# ============================================================
# Retornar o codigo do Robot Framework
#
# 0 = sucesso
# diferente de 0 = falha
#
# Importante para CI/CD.
# ============================================================

exit $ExitCode