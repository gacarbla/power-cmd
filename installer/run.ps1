function Write-Header(){
    Clear-Host
    Write-Host @"
[101;93m   POWER-CMD                         [0m
[107;30m   Made by gacarbla                  [0m
"@
}

function Get-FilePath(){
    $relativeDir = Get-Location
    $fileName = ".installation_data"
    $fileDir = Join-Path -Path $relativeDir -ChildPath $fileName
    return $fileDir
}

function Get-Installation(){
    $filePath = Get-FilePath
    if (Test-Path $filePath) {
        $fileContent = Get-Content $filePath -Raw
        if ($fileContent -match "installed") {
            return $true
        }
    }
    return $false
    
}

$successInstallation = Get-Installation
if ($successInstallation) {
    python main.py
} else {
    Write-Host @"
[31mInstallation error:[0m
    Please make sure you have successfully installed power-cmd and try again.

You can close this window.
"@
    Start-Sleep -Seconds 3600
}