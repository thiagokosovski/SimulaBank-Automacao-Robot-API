$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"


$folder = "results\$timestamp"


New-Item -ItemType Directory -Path $folder


robot `
--output $folder\output.xml `
--log $folder\log.html `
--report $folder\report.html `
tests