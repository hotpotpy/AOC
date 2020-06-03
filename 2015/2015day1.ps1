Param(
[string]$file = 'input_day1.txt'
)
$ErrorActionPreference='Stop'

$data = Get-Content $file
### Part one and two ###

$counter = 0
$first = $false
$bsmt_first = $null

for($i=0;$i -lt $data.length;$i++){
	if($data[$i] -eq '('){
		$counter += 1
	} elseif ($data[$i] -eq ')'){
		$counter -= 1
	}
	if(($first -eq $false) -and ($counter -eq -1)){
	$bsmt_first = $i+1
	$first = $true
	}
}
Write-Host "Answer to Part One: " $counter
Write-Host "Answer to Part Two: " $bsmt_first