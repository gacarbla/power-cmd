function Manage_DataFile {
    param (
        [string]$filePath,
        [string]$githubRepo
    )

    # Comprobar si el archivo de datos existe
    if (Test-Path $filePath) {
        $fileContent = Get-Content $filePath -Raw

        # Comprobar el contenido del archivo
        if ($fileContent -match "installed") {
            Write-Host "El repositorio está instalado."
            $choice = Read-Host "¿Desea eliminar el repositorio (E) o actualizarlo (A)? [E/A]"
            if ($choice -eq "E") {
                Remove-Item -Path $filePath
                Remove-Item -Path $githubRepo -Force -Recurse
                Write-Host "Repositorio eliminado."
            }
            elseif ($choice -eq "A") {
                Remove-Item -Path $githubRepo -Force -Recurse
                # Descargar el repositorio nuevamente
                if (Download-GitHubRepo $githubRepo) {
                    Write-Host "Repositorio actualizado."
                    Set-Content -Path $filePath -Value "installed"
                }
                else {
                    Write-Host "Error al actualizar el repositorio."
                    Set-Content -Path $filePath -Value "error"
                }
            }
        }
        elseif ($fileContent -match "error") {
            Write-Host "El repositorio no pudo ser descargado anteriormente."
            $retry = Read-Host "¿Desea intentarlo de nuevo? [S/N]"
            if ($retry -eq "S") {
                if (Download-GitHubRepo $githubRepo) {
                    Write-Host "Repositorio descargado exitosamente."
                    Set-Content -Path $filePath -Value "installed"
                }
                else {
                    Write-Host "Error al descargar el repositorio."
                }
            }
        }
        else {
            Write-Host "Opciones disponibles: "
            Write-Host "1. Eliminar el repositorio"
            Write-Host "2. Actualizar el repositorio"
            Write-Host "3. Reintentar la descarga del repositorio"
        }
    }
    else {
        # Descargar el repositorio si el archivo no existe
        if (Download-GitHubRepo $githubRepo) {
            Write-Host "Repositorio descargado exitosamente."
            Set-Content -Path $filePath -Value "installed"
        }
        else {
            Write-Host "Error al descargar el repositorio."
            Set-Content -Path $filePath -Value "error"
        }
    }
}

function Download-GitHubRepo {
    param (
        [string]$repoURL
    )

    try {
        git clone $repoURL
        return $true
    }
    catch {
        return $false
    }
}
