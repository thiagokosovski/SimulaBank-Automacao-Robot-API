from xml.etree import ElementTree as ET
from pathlib import Path
import os

output_file = Path("results/output.xml")

summary_file = os.environ.get("GITHUB_STEP_SUMMARY")

if not output_file.exists():
    print("Arquivo output.xml não encontrado.")
    exit(0)

tree = ET.parse(output_file)
root = tree.getroot()

statistics = root.find("statistics")

total = 0
passed = 0
failed = 0

if statistics is not None:
    total_node = statistics.find("./total/stat")

    if total_node is not None:
        passed = int(total_node.attrib.get("pass", 0))
        failed = int(total_node.attrib.get("fail", 0))
        total = passed + failed

with open(summary_file, "a", encoding="utf-8") as f:

    f.write("\n")

    f.write("## 📊 Test Statistics\n\n")

    f.write("| Item | Value |\n")
    f.write("|------|-------|\n")

    f.write(f"| Total Tests | {total} |\n")
    f.write(f"| Passed | ✅ {passed} |\n")
    f.write(f"| Failed | ❌ {failed} |\n")

    if failed == 0:
        status = "✅ SUCCESS"
    else:
        status = "❌ FAILURE"

    f.write(f"| Result | {status} |\n")