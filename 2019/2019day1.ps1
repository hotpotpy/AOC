Param(
[string]$file = 'input_day1.txt'
)
$ErrorActionPreference='Stop'

$data = Get-Content $file
### Part One ###

$ans1 = ($data | ForEach-Object {[Math]::Floor($_ / 3) - 2} | Measure-Object -Sum).sum
Write-Host "Answer to Part One: " $ans1
######

### Part Two ###
$total = 0

    for($i=0; $i -le $data.length; $i++){
    $x = $data[$i]
    while($true) {
        $x = [Math]::Floor($x / 3) - 2
        if($x -le 0){break}
        $total += $x
    } 
    }
Write-host "Answer to Part Two: " $total
