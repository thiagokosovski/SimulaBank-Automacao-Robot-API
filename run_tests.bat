@echo off

echo ==========================================
echo SimulaBank - Robot Framework
echo Executando os testes...
echo ==========================================

robot ^
-d reports ^
-l ../logs/log.html ^
-r report.html ^
-o output.xml ^
tests

pause