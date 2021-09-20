$SCR="main.py"
$proc = $null
$procs = Get-WmiObject Win32_Process -Filter "name = 'python3.exe' or name = 'python.exe'" | Select-Object Description,ProcessId,CommandLine,CreationDate

$procs | ForEach-Object { 
    if ( $_.CommandLine.IndexOf($SCR) -ne -1 ) { 
        if ( $null -eq $proc ) {
            $proc = $_
        }
    }
}

if ( $null -ne $proc ) {
    Write-Host "Process already running: $proc"
} else {
    py ./main.py
}